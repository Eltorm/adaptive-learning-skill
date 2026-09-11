#!/usr/bin/env python3
"""Validate an opt-in Adaptive Learning state directory without modifying it."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

import yaml


ALLOWED_STATUS = {
    "established", "widely_accepted", "emerging", "contested",
    "uncertain", "superseded", "retracted",
}
ALLOWED_DIMENSIONS = {"concept", "mechanism", "formal", "application", "limits", "transfer"}


def load_yaml(path: Path) -> dict[str, Any] | list[Any] | None:
    if not path.exists():
        return None
    value = yaml.safe_load(path.read_text(encoding="utf-8"))
    if value is None:
        return {}
    if not isinstance(value, (dict, list)):
        raise ValueError(f"{path}: top-level YAML value must be a mapping or list")
    return value


def mapping(value: Any, label: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ValueError(f"{label}: expected a mapping")
    return value


def validate(state_dir: Path) -> list[str]:
    errors: list[str] = []
    profile = load_yaml(state_dir / "profile.yaml")
    graph = load_yaml(state_dir / "knowledge-graph.yaml")
    mastery = load_yaml(state_dir / "mastery.yaml")
    queue = load_yaml(state_dir / "review-queue.yaml")

    if profile is not None:
        p = mapping(profile, "profile.yaml")
        if p.get("schema_version") != 1:
            errors.append("profile.yaml: schema_version must be 1")

    node_ids: set[str] = set()
    prereq_edges: dict[str, list[str]] = {}
    if graph is not None:
        g = mapping(graph, "knowledge-graph.yaml")
        if g.get("schema_version") != 1:
            errors.append("knowledge-graph.yaml: schema_version must be 1")
        nodes = g.get("nodes", [])
        if not isinstance(nodes, list):
            errors.append("knowledge-graph.yaml: nodes must be a list")
            nodes = []
        for i, raw in enumerate(nodes):
            try:
                node = mapping(raw, f"knowledge-graph.yaml.nodes[{i}]")
                node_id = node.get("id")
                if not isinstance(node_id, str) or not node_id.strip():
                    errors.append(f"knowledge-graph.yaml.nodes[{i}]: id is required")
                    continue
                if node_id in node_ids:
                    errors.append(f"knowledge-graph.yaml: duplicate node id {node_id}")
                node_ids.add(node_id)
                status = node.get("evidence_status")
                if status is not None and status not in ALLOWED_STATUS:
                    errors.append(f"{node_id}: invalid evidence_status {status}")
                prereq_edges.setdefault(node_id, [])
                for prereq in node.get("prerequisites", []) or []:
                    if isinstance(prereq, str):
                        prereq_edges[node_id].append(prereq)
                for edge in node.get("edges", []) or []:
                    if not isinstance(edge, dict):
                        errors.append(f"{node_id}: edge must be a mapping")
                        continue
                    target = edge.get("to")
                    if target not in node_ids:
                        # Defer duplicate/forward-reference resolution below.
                        if not isinstance(target, str) or not target.strip():
                            errors.append(f"{node_id}: edge target is required")
            except ValueError as exc:
                errors.append(str(exc))
        for src, targets in prereq_edges.items():
            for target in targets:
                if target not in node_ids:
                    errors.append(f"{src}: prerequisite target does not exist: {target}")
        for node in nodes:
            if not isinstance(node, dict):
                continue
            src = node.get("id")
            for edge in node.get("edges", []) or []:
                if isinstance(edge, dict) and edge.get("to") not in node_ids:
                    errors.append(f"{src}: edge target does not exist: {edge.get('to')}")

        visiting: set[str] = set()
        visited: set[str] = set()

        def visit(node_id: str) -> None:
            if node_id in visiting:
                errors.append(f"knowledge-graph.yaml: prerequisite cycle includes {node_id}")
                return
            if node_id in visited:
                return
            visiting.add(node_id)
            for target in prereq_edges.get(node_id, []):
                if target in node_ids:
                    visit(target)
            visiting.remove(node_id)
            visited.add(node_id)

        for node_id in node_ids:
            visit(node_id)

    if mastery is not None:
        records = mastery.get("records", mastery) if isinstance(mastery, dict) else mastery
        if isinstance(records, dict):
            records = [records]
        if not isinstance(records, list):
            errors.append("mastery.yaml: expected records list")
            records = []
        for i, raw in enumerate(records):
            try:
                record = mapping(raw, f"mastery.yaml[{i}]")
                if record.get("node_id") not in node_ids and node_ids:
                    errors.append(f"mastery.yaml[{i}]: unknown node_id {record.get('node_id')}")
                if record.get("dimension") not in ALLOWED_DIMENSIONS:
                    errors.append(f"mastery.yaml[{i}]: invalid dimension")
                evidence = record.get("evidence")
                score = evidence.get("rubric_score") if isinstance(evidence, dict) else None
                if score is not None and (not isinstance(score, (int, float)) or not 0 <= score <= 5):
                    errors.append(f"mastery.yaml[{i}]: rubric_score must be between 0 and 5")
            except ValueError as exc:
                errors.append(str(exc))

    if queue is not None:
        records = queue.get("items", queue) if isinstance(queue, dict) else queue
        if isinstance(records, dict):
            records = [records]
        if not isinstance(records, list):
            errors.append("review-queue.yaml: expected items list")
            records = []
        for i, raw in enumerate(records):
            try:
                item = mapping(raw, f"review-queue.yaml[{i}]")
                if item.get("node_id") not in node_ids and node_ids:
                    errors.append(f"review-queue.yaml[{i}]: unknown node_id {item.get('node_id')}")
                interval = item.get("interval_days")
                if interval is not None and (not isinstance(interval, (int, float)) or interval < 0):
                    errors.append(f"review-queue.yaml[{i}]: interval_days must be non-negative")
            except ValueError as exc:
                errors.append(str(exc))

    sessions_dir = state_dir / "sessions"
    if sessions_dir.exists():
        for path in sessions_dir.glob("*.yaml"):
            try:
                session = mapping(load_yaml(path), str(path))
                if session.get("schema_version") != 1:
                    errors.append(f"{path.name}: schema_version must be 1")
                for node_id in session.get("nodes_covered", []) or []:
                    if node_ids and node_id not in node_ids:
                        errors.append(f"{path.name}: unknown nodes_covered id {node_id}")
            except ValueError as exc:
                errors.append(str(exc))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("state_dir", type=Path)
    args = parser.parse_args()
    errors = validate(args.state_dir)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"PASS: state directory is valid (read-only): {args.state_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
