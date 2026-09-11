# Anti-pattern: fluent but empty

> “Overfitting is when a model is too complex and fails to generalise. It is a
> balance between bias and variance.”

Why this fails: it gives no observable symptom, mechanism, assumptions,
intervention, boundary, or way to predict what changes. A better module ties
the train–validation gap to capacity/data/noise, shows a curve or concrete
case, and tests diagnosis and transfer.
