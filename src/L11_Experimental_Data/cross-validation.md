# What if we don't have a starting theory to guide our model?

- Use cross-validation on results to guide the choice of model complexity.

- For small datasets, use leave-one-out cross-validation.

- For large datasets, use k-fold cross-validation or repeated random-sampling validation.

**Leave-one-out cross-validation**

Let D be the original data set

`test_results = []`

`for i in range(len(D)):`
`   training = D[:].pop(i)`
`   model = build_model(training)`
`   test_results.append(test(model, D[i]))`

`Average test_results`

**K-fold cross-validation**

Similar to leave-one-out:

- D is partitioned into k equal size sets.
- Model trained on k-1, and tested on remaining.
- Repeat the process, and average the outcomes.

**Repeated random sampling**

- Leave out a random sample of the dataset - rarely more than half, often as little as 20%.

`Let D be the original data set`
`Let n be the number of random samples`

`test_results = []`
`for i in range(n):`
`   randomly partition D into two sets:`
`       training and test`
`   model = build_model(training)`
`   test_results.append(test(model, test))`

`Average test_results`
