# Bayesian Reasoning

The previous examples examined thus far have followed the **frequentist** approach to statistics - drawing conclusions with regards to data from samples based on the frequency or proportion of the data.

In some cases, a different approach, **Bayesian statistics**, is more appropriate.

**Conditional probability**

The key idea underlying Bayesian reasoning is conditional probability.

Earlier, we relied on assumptions that events were independent when calculating probability - e.g., in the case of coin flips, whether a flip returns head or tails is independent of the prior result.

Conditional probability asks the question, what is the probability of A, given B?

This is notated as P(A|B) - the probability of A, given the assumption that B is true.

Example: P(male) \* P(weight > 197 | male)

If P(A) and P(B) are independent, then P(A|B) == P(A).

For the above example, B is male and A is weight > 197.

In general, if P(B) != 0:
P(A|B) = P(A and B) / P(B)

As with conventional probabilities, conditional probabilities lie between 0 and 1.

Furthermore, if ^A stands for not A, P(A|B) + P(^A|B) = 1.s

Also, P(A|B) does not imply that P(B|A).
