# Complexity

**Increasing complexity**

What happens when we increase order of polynomial?

- Can we get a worse fit to training data?

If the extra term is useless, the coefficient will merely be zero.

But if the data is noisy, it may fit the noise rather than the underlying pattern in the data.

- The higher the order of the polynomial, the more likely it is to fit the noise.

**Key points**

- Choosing an over-complex model leads to overfitting to the training data.

- Increases the risk of a model that works poorly on data not included in the training set.

- However, choosing an insufficiently complex model has other problems:
  - E.g. when we tried to fit a line to data that was parabolic.

"Everything should be made as simple as possible, but not simpler." - Einstein
