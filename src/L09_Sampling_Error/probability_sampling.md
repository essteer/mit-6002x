# Probability Sampling

- Each member of a population has a non-zero probability of being included in a sample.
- Simple random sampling: each member has an equal chance of being chosen.

Simple random sampling is not always appropriate, however.

**Stratified sampling**

- When there are small subgroups that should be represented.
- When it is important that subgroups be represented proportionally to their size in the population.
- Can be used to reduce the needed size of sample; variability of subgroups is less than that of the entire population.
- Requires care to do properly.

**Predicting election outcomes**

Approaches:

- Ask every voter.
- Draw multiple random samples and compute mean and confidence interval.
- Draw one sample and estimate mean weight and confidence interval using that.

But we can't actually ask every voter, so there is no obvious way to evalutae sampling techniques.

**Central Limit Theorem**

CLT says that:

1. Given a set of sufficiently large samples drawn from the same population, the sample means will be approximately normally distributed.
2. This normal distribution will have a mean close to the mean of the population.
3. The variance (computed using numpy.var) of the sample means will be close to the variance of the population divided by the sample size.

The third feature can be used to compute the Standard Error of the Mean (SE / SEM).

**Standard Error of the Mean**

- Once a sample reaches a reasonable size, sample standard deviation is a decent approximation to population standard deviation.
- The skew of the population does matter - whether normal, uniform, or exponential.
- The size of the population is much less critical.

**To estimate mean from a single sample**

1. Choose sample size basd on estimate of skew in population.
2. Choose a random sample from the population.
3. Compute the mean and standard deviation for that sample.
4. Use the sample standard deviation to estimate the standard error.
5. Use the estimated SE to generate confidence intervals around the sample mean.

This works well when independent random samples can be chosen from the population - but this is not always possible to do.
