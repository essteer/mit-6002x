# Machine Learning

"Machine learning is the field of study that gives computers the ability to learn without being explicitly programmed." - Arthur Samuel

- In traditional programming, data and programs go into a computer, which produces output.
- In machine learning, data and output associated with that data go into a computer, which produces a program, into which new data can be fed that the computer "thinks" should be associated with that data.

**How are things learned?**

Memorisation:

- Accumulation of individual facts
- Limited by:
  - time to observe facts
  - memory to store facts

Generalisation:

- Deduce new facts from old facts
- Limited by accuracy of deduction process:
  - essentially a predictive activity
  - assumes that the past predicts the future

## Basic paradigm of machine learning

- Observe a set of examples (training data).
- Infer something about the process that generated that data.
- Use inference to make predictions about previously unseen data (test data).

All ML methods require:

- Representation of the features.
- Distance metric for feature vectors.
- Objective function and constraints.
- Optimisation method for learning the model.
- Evaluation method, to determine how much confidence we can place in the outcome, but also to enable us to fine-tune parameters.
