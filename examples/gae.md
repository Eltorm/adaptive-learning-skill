# Example: cognitive path and relationship budget (reinforcement learning)

**Request:** “I know policy gradients; explain what GAE does in PPO at L3.”

Select the formal/application path
`advantage -> TD error -> multi-step return -> lambda weighting -> GAE -> PPO`
as the mainline. Keep Monte Carlo, eligibility traces, and variance analysis as
foreshadowed or deferred branches unless the learner asks for the derivation.
The transitions should answer a real tension: one-step bootstrapping is stable
but biased by the value estimate; long returns reduce that bias but increase
variance; lambda interpolates the estimates; GAE sums weighted TD errors.

Use an implicit A-level connection for TD error -> GAE, a brief B-level anchor
that GAE is not an isolated trick, and a C-level “continue with” note for
eligibility traces. At L3, reconstruct the weighted sum and predict the limiting
behaviour as lambda approaches 0 or 1. At L4, implement the recurrence and
compare estimates on a toy trajectory; record which dimension was demonstrated.
