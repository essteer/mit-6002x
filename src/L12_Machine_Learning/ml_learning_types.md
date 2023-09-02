# Types of Machine Learning

**Supervised learning**

- Start with a set of feature vector/value pairs.
- Goal: find a model that predicts a value for a previously unseen feature vector.

- **Regression** models predict a real number

  - as with linear regression

- **Classification** models predict a label (chosen from a finite set of labels)

**Unsupervised learning**

- Start with a set of feature vectors (but no labels).
- Goal: uncover some latent structure in the set of feature vectors.

- **Clustering** is the most common technique
  - define some metric that captures how similar one feature vector is to antoher
  - group examples based on this metric.

## Choosing features

- Features never fully describe a situation.

- **Feature engineering**:

  - represent examples by feature vectors that will facilitate generalisation
  - suppose we want to use 100 past examples to predict which students will pass a final exam
  - some features will be helpful (e.g., midterm exam grades, assignment completion)
  - other features may cause overfit (e.g., birth month)

- Goal: maximise the ratio of useful input to irrelevant input:
  - **Signal-to-Noise Ratio (SNR)**
