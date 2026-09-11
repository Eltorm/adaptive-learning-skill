#!/usr/bin/env python3
"""Small, explicit state operations for the opt-in Adaptive Learning protocol."""

from __future__ import annotations

import argparse
import copy
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Any
import zipfile

import yaml

from validate_state import validate


def read(path: Path, default: Any) -> Any:
    if not path.exists():
        return copy.deepcopy(default)
    value = yaml.safe_load(path.read_text(encoding="utf-8"))
    return default if value is None else value


def write(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(path.suffix + ".tmp")
    temp.write_text(yaml.safe_dump(value, sort_keys=False, allow_unicode=True), encoding="utf-8")
    temp.replace(path)


def parse_day(value: str) -> date:
    return datetime.fromisoformat(value).date()


def init_state(root: Path) -> None:
    root.mkdir(parents=True, exist_ok=True)
    defaults = {
        "profile.yaml": {"schema_version": 1, "learner_id": "", "language": "", "goals": [], "background": [], "constraints": {}, "preferences": []},
        "knowledge-graph.yaml": {"schema_version": 1, "nodes": []},
        "mastery.yaml": {"schema_version": 1, "records": []},
        "review-queue.yaml": {"schema_version": 1, "items": []},
    }
    for name, value in defaults.items():
        path = root / name
        if not path.exists():
            write(path, value)
    (root / "sessions").mkdir(exist_ok=True)
    print(f"Initialized opt-in state at {root}")


def record(args: argparse.Namespace) -> None:
    root = args.state_dir
    graph = read(root / "knowledge-graph.yaml", {"nodes": []})
    nodes = graph.get("nodes", []) if isinstance(graph, dict) else []
    known = {n.get("id") for n in nodes if isinstance(n, dict)}
    if args.node_id not in known:
        raise SystemExit(f"Unknown node_id: {args.node_id}; add it to knowledge-graph.yaml first")
    mastery = read(root / "mastery.yaml", {"schema_version": 1, "records": []})
    records = mastery.setdefault("records", [])
    score = float(args.score)
    if not 0 <= score <= 5:
        raise SystemExit("score must be between 0 and 5")
    now = parse_day(args.at)
    previous = [r for r in records if isinstance(r, dict) and r.get("node_id") == args.node_id and r.get("dimension") == args.dimension]
    old_interval = 1
    queue = read(root / "review-queue.yaml", {"schema_version": 1, "items": []})
    items = queue.setdefault("items", [])
    for item in items:
        if isinstance(item, dict) and item.get("node_id") == args.node_id:
            try:
                old_interval = max(1, int(item.get("interval_days", 1)))
            except (TypeError, ValueError):
                old_interval = 1
    interval = max(1, old_interval * 2) if score >= 4 else (old_interval if score >= 3 else 1)
    record_value = {
        "node_id": args.node_id,
        "dimension": args.dimension,
        "evidence": {"task_id": args.task_id, "response_summary": args.summary, "rubric_score": score, "evaluator_uncertainty": args.uncertainty},
        "attempted_at": args.at,
        "open_gaps": [] if score >= 3 else [args.dimension],
    }
    records.append(record_value)
    items[:] = [i for i in items if not (isinstance(i, dict) and i.get("node_id") == args.node_id)]
    items.append({"node_id": args.node_id, "due_at": (now + timedelta(days=interval)).isoformat(), "interval_days": interval, "priority": "high" if score < 3 else "medium", "reason": "weakness" if score < 3 else "due", "variation_prompt": args.variation})
    write(root / "mastery.yaml", mastery)
    write(root / "review-queue.yaml", queue)
    print(f"Recorded {args.node_id}/{args.dimension} score={score:g}; next review in {interval} day(s)")


def due(args: argparse.Namespace) -> None:
    cutoff = parse_day(args.at)
    queue = read(args.state_dir / "review-queue.yaml", {"items": []})
    items = queue.get("items", []) if isinstance(queue, dict) else []
    due_items = []
    for item in items:
        if not isinstance(item, dict) or not item.get("due_at"):
            continue
        try:
            if parse_day(str(item["due_at"])) <= cutoff:
                due_items.append(item)
        except ValueError:
            continue
    print(yaml.safe_dump(due_items, sort_keys=False, allow_unicode=True).rstrip() if due_items else "No items due.")


def merge_graph(args: argparse.Namespace) -> None:
    root = args.state_dir
    current = read(root / "knowledge-graph.yaml", {"schema_version": 1, "nodes": []})
    incoming = read(args.incoming, {"schema_version": 1, "nodes": []})
    current_nodes = current.setdefault("nodes", [])
    by_id = {n.get("id"): n for n in current_nodes if isinstance(n, dict) and n.get("id")}
    merged = 0
    conflicts = 0
    stamp = args.at
    for raw in incoming.get("nodes", []) if isinstance(incoming, dict) else []:
        if not isinstance(raw, dict) or not raw.get("id"):
            continue
        node_id = raw["id"]
        if node_id not in by_id:
            current_nodes.append(copy.deepcopy(raw)); by_id[node_id] = current_nodes[-1]; merged += 1; continue
        target = by_id[node_id]
        for key in ("prerequisites", "claim_sources", "edges"):
            if key in raw:
                target.setdefault(key, [])
                for value in raw[key] or []:
                    if value not in target[key]: target[key].append(copy.deepcopy(value))
        comparable = {k: raw.get(k) for k in ("name", "core_claim", "evidence_status") if raw.get(k) is not None}
        existing_comparable = {k: target.get(k) for k in comparable if target.get(k) is not None}
        if comparable and comparable != existing_comparable:
            target.setdefault("conflicts", []).append({"observed_at": stamp, "incoming": copy.deepcopy(raw), "resolution": "preserved for review"})
            target["evidence_status"] = "contested"
            conflicts += 1
        merged += 1
    write(root / "knowledge-graph.yaml", current)
    print(f"Merged {merged} node(s); preserved {conflicts} conflict(s) for review")


def export_state(args: argparse.Namespace) -> None:
    source = args.state_dir.resolve()
    output = args.output.resolve()
    if output.exists():
        raise SystemExit(f"Refusing to overwrite existing export: {output}")
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "x", zipfile.ZIP_DEFLATED) as archive:
        for path in source.rglob("*"):
            if path.is_file() and ".tmp" not in path.name:
                archive.write(path, path.relative_to(source).as_posix())
    print(f"Exported state to {output}")


def import_state(args: argparse.Namespace) -> None:
    destination = args.destination.resolve()
    if destination.exists():
        raise SystemExit(f"Refusing to overwrite existing destination: {destination}")
    destination.mkdir(parents=True)
    with zipfile.ZipFile(args.archive) as archive:
        for member in archive.infolist():
            target = (destination / member.filename).resolve()
            if destination not in target.parents:
                raise SystemExit(f"Unsafe archive member: {member.filename}")
        archive.extractall(destination)
    print(f"Imported state to {destination}; run validate before use")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    p_init = sub.add_parser("init"); p_init.add_argument("state_dir", type=Path)
    p_record = sub.add_parser("record"); p_record.add_argument("state_dir", type=Path); p_record.add_argument("--node-id", required=True); p_record.add_argument("--dimension", choices=sorted({"concept", "mechanism", "formal", "application", "limits", "transfer"}), required=True); p_record.add_argument("--score", required=True, type=float); p_record.add_argument("--task-id", required=True); p_record.add_argument("--summary", required=True); p_record.add_argument("--variation", default="reconstruct the principle in a novel case"); p_record.add_argument("--uncertainty", choices=["low", "medium", "high"], default="medium"); p_record.add_argument("--at", required=True)
    p_due = sub.add_parser("due"); p_due.add_argument("state_dir", type=Path); p_due.add_argument("--at", required=True)
    p_merge = sub.add_parser("merge-graph"); p_merge.add_argument("state_dir", type=Path); p_merge.add_argument("incoming", type=Path); p_merge.add_argument("--at", required=True)
    p_export = sub.add_parser("export"); p_export.add_argument("state_dir", type=Path); p_export.add_argument("output", type=Path)
    p_import = sub.add_parser("import"); p_import.add_argument("archive", type=Path); p_import.add_argument("destination", type=Path)
    p_validate = sub.add_parser("validate"); p_validate.add_argument("state_dir", type=Path)
    args = parser.parse_args()
    if args.command == "init": init_state(args.state_dir)
    elif args.command == "record": record(args)
    elif args.command == "due": due(args)
    elif args.command == "merge-graph": merge_graph(args)
    elif args.command == "export": export_state(args)
    elif args.command == "import": import_state(args)
    else:
        errors = validate(args.state_dir)
        if errors:
            for error in errors: print(f"ERROR: {error}")
            return 1
        print(f"PASS: state directory is valid (read-only): {args.state_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
