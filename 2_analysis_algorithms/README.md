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

## Mathematical models

It is possible, in principle, to estimate the running time of any program. The total running time of a program is determined by two primary factors:
* The cost of executing each statement
* The frequency of execution of each statement

The first one is a property of  the computer, the compiler/interpreter and the operating system.

The primary challenge is to determine the frequency of execution of the statements. Usually higher-level reasoning is required for this (as was done for the dynamic connectivity problem). Sometimes the frequency depends on the input data, for example, the number of times `ThreeSum().count` is precisely the number of triplets in the input, which can range from 0 to all of them. In this case, is is possible to do a probabilisti analysis to determine expected value of this quantity.

### Tilde approximations

Frequency analysis can lead to complicated mathematical expressions, like:
```
N(N-1)(N-1)/6 = N<sup>3</sup>/6 - N<sup>2</sup>/2 + N/3
```

It is typcial that the terms after the leading term are relatively small when `N` is large, which are the cases we are interested in. To allow us to ignore insignificant terms and therefore substantially simplify the mathematical formulas, we often use the *tilde-notation* (\~), where we allow low-order terms that complicate formulas to represent a negligeble contribution to values of interest.


>**Definition** We write \~f(N) to represent eny function that, when divided by f(N), approaches 1 as N grows, and we write g(N) \~ f(N) to indicate that >g(N)/f(N) approaches 1 as N grows.

**Examples**

|                 function                | tilde approximation | order of growth |
|:---------------------------------------:|:-------------------:|-----------------|
| N<sup>3</sup>/6 - N<sup>2</sup>/2 + N/3 |  \~N<sup>3</sup>/6  |  N<sup>3</sup>  |
|          N<sup>2</sup>/2 + N/2          | \~N<sup>2</sup>/2   |  N<sup>2</sup>  |
|                 lg(N) +1                |       \~log(N)      |      log(N)     |
|                    3                    |         \~3         |        1        |

**Commonly encountered order of growth functions**

|  description |     function     |
|:------------:|:----------------:|
|   constant   |         1        |
|  logarithmic |      log(N)      |
|    linear    |         N        |
| linearithmic |     N log(N)     |
|   quadratic  |   N<sup>2</sup>  |
|     cubic    | N <sup> 3 </sup> |
|  exponential | 2 <sup> N </sup> |


### Analysis of algorithms

Working with the order of growth allows us to separate a program from the algorithm it implements. The algorithm that you are using determines the order of growth. Separating the algorithm from the implementation is a powerful concept, allowing us to develop knowledge about the performance of the algorithm and then apply on any computer.

### Cost model

>**Definition** *property* refers to a hypothesis that needs to be validated through experimentation.

>**Definition** *proposition* referes to mathematical trugh about algorithms in terms of cost model.

We focus attention on properties of algorithms by articulating a *cost model* that defines the basic operations used by the algorithms. With the appropiate cost model (such as number of array accesses, as in the dynamic connnectivity problem), we can make precise mathematical statements about properties fo an algorithm.

Our intent is to articulate cost models such that the order of growth of the running time for a given implementation is the same as the order of growth  of the cost of the underlying algorithm (in other words, the cost model should include operations that fall within the inner loop).

### Summary

For many programs, developing a mathematical model of running time reduces to the following steps:

* Develop an *input model*, including a definition of the problem size.
* Identify the *inner loop*
* Define a *cost model* that includes operations in the inner loop.
* Determine the frequency of execution og those operations for the given input. Doing so migh require mathematical analysis.

## Designing faster algorithms

One of the primary reasons to study the order of growth of a program is to help design a faster algorithm to solve the same problem.

Some routes to consider:
* Reduce problem complexity (3sum to 2sum), and improve simpler version
* Translate new version to original problem.

Stratergy for addressing new problems:
* Implement and analyze a straighforward solution to the problem. Such solutions are referred as *brute-force* solutions.
* Examine algorithmic improvements, usually designed to reduce the order of growth of the running time.
* Run experiments to validate the hypotheses that the new algorithms are faster.

### Doubling ratio experiments

* Develop an input generator that produces inputs that model the inputs expected in practice.
* Run the [`DoublingRatio`](www.github.com) program, that calculates the ratio of each running time with the prvious.
* Run until the ratios approach a limit `2<sup>b</sup?`.

The tests is not effective if the ratios don't approach a limiting value, but they do for many programs implying the following conclusions:
* The *order of growth* of the running time is approximately `N<sup>b</sup?`.
* To predict running times, multiply the last observed running tyme by `2<sup>b</sup?` and double `N`, continuing as long as desired. If you want to predict for an input size that is not a power of 2 times `N`, you can adjust ratios accordingly.

Why does the ratio approach a constatn? A simple mathematical calculation shows that to be tha case

>**Proposition** If `T(N) \~ aN<sup>b</sup>lg(N)` then `T(2N)/T(N) \~ 2<sup>b</sup>`.
>**Proof** Immediate form calculation
```
> T(2N)/T(N) = a(2N)<sup>b</sup>lg(2N) / aN<sup>b</sup>lg(N)
>            = 2<sup>b</sup> (1 + lg(2) + lg(N))
>            \~ 2<sup>b</sup>
```

**YOU SHOULD ALWAYS RUN DOUBLING RATION EXPERIMENTS FOR EVERY PROGRAM THAT YOU WRITE WERE PERFORMANCE MATTERS** doing tos is a very simple way to estimate order of growth of the running time, perhaps revealing a performance bug where a program may turn out to be not as efficient as you might think.

### Estimating the feasibility of solving large problems.

You need to be able to answer the basic question for every program you write: *Will the program be able to process this given input in  a reasonable amount of time?* 

Knowing the order of growth of the running time of an algorithm provides precisely the information to understand limitaions on the size of the problems that you can solve. *Developing such understanding is the most important reason to study performance*.

## Caveats 

There are many reasons that you might get inconsistent or misleading re- sults when trying to analyze program performance in detail. All of them have to do with the idea that one or more of the basic assumptions underlying our hypotheses might be not quite correct. We can develop new hypotheses based on new assumptions, but the more details that we need to take into account, the more care is required in the analysis.

Some assumtions that might lead to inconsisten results:

* Large constants in lower-order terms
* Nondominang inner loop
* Instruction time
* System considerations
* Strong dependence on inputs
* Multiple problem parameters

## Memory


