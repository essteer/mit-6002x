# R Squared

- Instead of mean square error (see mean_square_error.md), we can calculate the absolute goodness of a fit - if the fit is generated via linear regression - using the coefficient of determination.
- Coefficient of determination is usually written as _R^2_.

_R^2_ = 1 - (sum(yi - pi)^2 / sum(yi - mu)^2)

Where:

- yi = measured values
- pi = predicted values
- mu = the mean

- The numerator therefore captures the amount of error in the estimates.
- The denominator captures the variability in the estimates - how much they differ from the mean.
- 1 would be a perfect score; the close to 0, the worse the fit.

By comparing the estimation errors (numerator) with the variability of the original values (denominator), R^2 is intended to capture the proportion of variability in a data set that is accounted for by the statistical model provided by the fit.

R^2 is always between 0 and 1 when the fit is generated by a linear regression, and tested on training data.

- If R^2 = 1, model explains all variability in the data.
- If R^2 = 0, model explains none of the variability in the data.