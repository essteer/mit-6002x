# CLT

**Central Limit Theorem** (CLT) explains why it is possible to use a single sample drawn from a population to estimate the variability of the means of a set of hypothetical samples drawn from the same population.

A version of CLT was first published by Laplace in 1810, and refined by Poisson in the 1820s. The modern CLT emerged from the efforts of a sequence of mathematicians in the first half of the 20th century.

CLT says that:

1. Given a set of sufficiently large samples drawn from the same population, the sample means will be approximately normally distributed.
2. This normal distribution will have a mean close to the mean of the population.
3. The variance (computed using numpy.var) of the sample means will be close to the variance of the population divided by the sample size.

**Why is the CLT useful?**

The primary value of the CLT is that it allows us to compute confidence levels and intervals even when the underlying population distribution is not normal (see ch_19_423_central_limit_theorem.py for an example).

- It doesn't matter what the shape of the distribution of values happens to be
- If we are trying to estimate the mean of a population using sufficiently large samples
- The CLT allows us to use the empirical rule when computing confidence intervals.
