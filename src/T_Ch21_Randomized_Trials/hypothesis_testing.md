# Hypothesis Testing

**Significance testing**

1. State a null hypothesis and an alternative hypothesis, which can only be true if the null hypothesis is false.
2. Understand statistical assumptions about the sample being evaluated.
3. Compute a relevant test statistic.
4. Derive the probability of that test statistic under the null hypothesis.
5. Decide whether that probability is sufficiently small that you are willing to assume the null hypothesis is false, i.e. to reject the null hypothesis.

Common values chosen for the rejection level - which should be decided in advance - are 0.05 and 0.01.

**α**

A threshold for statistical significance, α, is chosen, and we try to show that the probability of the data having been drawn from distributions consistent with the null hypothesis is less than α; we accept the negation of the null hypothesis with a probability of 1 - α.

The choice of α affects the kind of errors made:

- A higher α means a true null hypothesis will be rejected more often (type I errors);
- A lower α means a false null hypothesis will be accepted more often (type II errors).

Typically an α of α = 0.05 is chosen.

However, depending on the consequences of being wrong, a larger or smaller α may be selected. E.g., for risk of death caused by a new drug, α should be very small (e.g. α = 0.001) to reduce the risk of approving a drug that is harmful.

**Test statistic**

The most common test statistic is the t-statistic, which tells us how different the estimate derived from the data is from the null hypothesis, measured in units of standard error.

The larger the t-statistic, the more likely the null hypothesis can be rejected.

Recall that to compute confidence intervals, we use standard deviations from the mean; for a normal distribution, the probability of an example lying within a fixed number of standard deviations of the mean is fixed.

For the t-statistic, we assume a t-distribution rather than a normal distribution.

**Degrees of freedom** describes the amount of independent information used to derive the t-statistic.

A t-distribution resembles a normal distribution; the larger the degrees of freedom, the closer the t-distribution is to a normal distribution, and the higher probability that the sample statistic is representative of the population.

Small degrees of freedom result in fatter tails.

**Bonferroni correction**

When running an experiment involving multiple **hypotheses**, the simplest and most conservative approach is to use the Bonferroni correction.

Intuition: when checking a family of m hypotheses, one way of maintaining an appropriate family-wise error rate is to test each individual hypothesis at a level of (1/m)\*α.

E.g., with 10 samples, and α = 0.05, we should check whether the p-value is less than 0.05/10 = 0.005. (1/10 = 0.1, 0.1 \* 0.05 = 0.005.)

Bonferroni correction is conservative - it fails to reject the null hypothesis more often than necessary - if there are many tests or the test statistics for the tests are positively correlated.

There is also no generally acceptable definition for "family of hypotheses".
