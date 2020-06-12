# Analysis of Algorithms

When running a program (either as a customer or programmer), it is natural to ask *How long will this take to run?* To answer this questions, we make use of the scientific method, to come up with an estimate, that will help answer that question. We apply mathematical analysis to develop concise models of costs and do experimental studies to validate these models.

The scientific method is made up of:
* Observe some feature of the natural world, generally with precise measurements.
* Hypothesize a model that is consistent with the observations.
* Predict events using the hypothesis.
* Verify the predictions by making further observations.
* Validate by repeating until the hypothesis and observations agree.

Every experiment needs to have two characteristics, 1) it must be reproducible and 2) it must be falsifiable.

## Observations

1. The running time of a program often varies with input
2. Some programs' running times don't seem to change with input, in such cases, running time is dominated by problem size.

### Example

