# Standard Error of the Mean

The standard error of the mean (SE or SEM) provides a way to estimate a confidence interval using a single example.

The SEM of sample size n is the standard deviation of the means of an infinite number of samples of size n, drawn from the same population.

- It depends on both n and the standard deviation of the population.

**If we have only a single sample, we don't know the standard deviation of the population.**

Typically, we assume the std dev of the sample is a reasonable proxy for the std dev of the population. This will be so, as long as the population distribution is not especially skewed.

In practice, the sample std dev is used in place of the population std dev to estimate the SEM.

If the sample size is large enough, and the population distribution is not too far from normal, it is safe to use this estimate to compute confidence intervals using the empirical rule.

This implies that we can use a sample to:

1. Compute the mean and std dev of that sample.
2. Use the std dev of that sample to estimate the SEM.
3. Use the estimated SEM to generate confidence intervals around the sample mean.
