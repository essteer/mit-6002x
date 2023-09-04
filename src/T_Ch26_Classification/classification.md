# Classification Methods

A classification model, or classifier, is used to label an example as belonging to one of a finite set of categories.

**One-class learning**

- Training set contains examples drawn from only one class.
- Goal: learn a model that predicts whether an example belongs to that class.
- Useful when it is difficult to find training examples that lie outside the class.
- Frequently used to build anomaly detectors, e.g. previously unseen kinds of attacks on a computer network.

**Two-class learning / binary classification**

- Training set contains examples drawn from exactly two classes (typically named "positive" and "negative").
- Goal: find a boundary that separates the two classes.

**Multi-class learning**

- Involves finding boundaries that separate more than two classes from each other.

**Classifier formula**

(See ch_26_p590_classification.py for implementations.)

- Sensitivity is the true positive rate, the % of positives correctly identified as such:
  sensitivity = true positive / (true positive + false negative)

- Specificity is the true negative rate, the % of negatives correctly identified as such:
  specificity = true negative / (true negative + false positive)

- Positive predictive value is the probability that an example classified as positive is truly positive:
  positive predictive value = true positive / (true positive + false positive)

- Negative predictive value is the probability that an example classified as negative is truly negative:
  negative predictive value = true negative / (true negative + false negative)
