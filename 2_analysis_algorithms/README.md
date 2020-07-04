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
To observe the lifecycle of the analysis of an algorithm, we are playing with the 3sum problem. Which counts the number of triples in a file of N integers that sum to 0 (assum- ing that overflow plays no role).

To reliably measure the amount of time of a given program I use the python function `time.time()`. The implementation can be found [here](https://github.com/Nerdrigo/algorithms/blob/master/2_analysis_algorithms/1_3sum.py).

One can then proceed to plot the input size `N` on the *x-axis*, and the time it takes `T(N)` in the *y-axis*. You can use a regular plot, or a log-log plot.

### Mathematical models

It is possible, in principle, to estimate the running time of any program. The total running time of a program is determined by two primary factors:
* The cost of executing each statement
* The frequency of execution of each statement

The first one is a property of  the computer, the compiler/interpreter and the operating system.

The primary challenge is to determine the frequency of execution of the statements. Usually higher-level reasoning is required for this (as was done for the dynamic connectivity problem). Sometimes the frequency depends on the input data, for example, the number of times `ThreeSum().count` is precisely the number of triplets in the input, which can range from 0 to all of them. In this case, is is possible to do a probabilisti analysis to determine expected value of this quantity.

#### Tilde approximations

Frequency analysis can lead to complicated mathematical expressions, like:
```
N(N-1)(N-1)/6 = N<sup>3</sup>/6 - N<sup>2</sup>/2 + N/3
```

It is typcial that the terms after the leading term are relatively small when `N` is large, which are the cases we are interested in. To allow us to ignore insignificant terms and therefore substantially simplify the mathematical formulas, we often use the *tilde-notation* (\~), where we allow low-order terms that complicate formulas to represent a negligeble contribution to values of interest.

```
**Definition** We write \~f(N) to represent eny function that, when divided by f(N), approaches 1 as N grows, and we write g(N) \~ f(N) to indicate that g(N)/f(N) approaches 1 as N grows.
```

