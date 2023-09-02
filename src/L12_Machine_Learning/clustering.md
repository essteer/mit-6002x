# Clustering

A form of unsupervised learning.

- Partition examples into groups (clusters) such that examples in a group are more similar to each other than to examples in other groups.

- Unlike classification, there is not typically a "correct answer":
  - the answer is dictated by feature vector and distance metric, not by a ground truth label.

Clustering is best posed as an **optimisation problem**.

- Begin by examining the variability of a single cluster, c:

variability(c) = sum(distance(mean(c), e)^2)
dissimilarity(C) = sum(variability(c))

(capitalised C refers to all clusters)

- "variability" here resembles variance, but it is not variance: why not divide variability by the size of the cluster?

- The reason is that we want an objective function that penalises large, incoherent clusters, more than it penalises small incoherent clusters.

- Is the optimisation problem one of finding a set of clusters, C that minimises dissimilarity(C)?

  - No, otherwise we could put each example in its own cluster.
  - In that case, the distance between the mean(c) and e (in its own cluster) would be zero.

- Need a constraint, e.g.:
  - minimum distance between clusters
  - number of clusters

**K-means clustering**

If we choose the number of clusters as the constraint, a useful greedy algorithm is k-means clustering.

- Constraint: exactly k non-empty clusters
- Use greedy algorithm to find an approximation to minimising the objective function
- This does not always find the most optimal solution, but often finds a good approximation to it

Algorithm in pseudocode:

Note: centroid is akin to the geographical centre of a given cluster.
Only in the first iteration will the centroid represent actual data points: from there they will become averages.

`randomly choose k examples as initial centroids`
`while True:`
`   create k clusters by assigning each example to closest centroid`
`   compute k new centroids by averaging examples in each cluster`
`   if centroids don't change:`
`       break`

- Beware that greedy algorithms can result in local optima far from the global optimum.
- To mitigate this, run repeated k-means tests, and choose the one that does the best job of minimising the objective function.

Algorithm in pseudocode:

`best = k_means(points)`
`for t in range(num_trials):`
`    C = k_means(points)`
`    if dissimilarity(C) < dissimilarity(best):`
`        best = C`
`return best`
