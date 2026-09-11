# Example: focused concept module (machine learning)

**Request:** `/learn overfitting`; learner knows train/test split, wants to
diagnose it in practice; target L4.

**Right-sized contract:** concept-level module, not a machine-learning
textbook. Required: train/test distinction and loss; recommended: validation,
regularisation, model capacity.

**Cognitive spine:** A model can reduce training error while worsening unseen
error → the split exposes the generalisation question → capacity and data
noise explain the gap → validation/regularisation alter the trade-off → a
learning-curve exercise asks the learner to predict what changes with more data.

**L4 task (self-contained):** use the deterministic toy data
`x = 0,1,...,19; y = x + [0,0,1,-1,0,1,0,-1,0,0, 0,1,-1,0,1,0,-1,0,1,0]`,
fit a degree-1 and degree-12 polynomial on rows 0-13, and evaluate on rows
14-19. Record both losses, then apply ridge regularisation to the degree-12
model without tuning on a hidden test set. Success means the learner can state
which model overfits, show the train/validation evidence, and report whether
the intervention lowers validation loss. If no coding environment is
available, use the same table and hand-calculate a qualitative loss comparison.
Reveal the rubric only after the procedure is submitted.

**Checks:** distinguish underfitting from overfitting in a new curve; predict
the effect of adding noisy features; choose a validation protocol and explain
the leakage boundary. A wrong diagnosis maps back to model capacity, split
semantics, or loss/generalisation as the smallest repair. Progress record:
`application demonstrated if the learner reports both losses and a justified
intervention; transfer remains untested until a new dataset is diagnosed`.
