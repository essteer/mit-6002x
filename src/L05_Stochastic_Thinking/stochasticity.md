# Stochasticity

**Models**

A **deterministic model** is one whose behavior is entirely predictable. Every set of variable states is uniquely determined by parameters in the model and by sets of previous states of these variables. Therefore, these models perform the same way for a given set of initial conditions, and it is possible to predict precisely what will happen.

A **stochastic model** is one in which randomness is present, and variable states are not described by unique values, but rather by probability distributions. The behavior of this model cannot be entirely predicted.

A **static model** does not account for the element of time. In this type of model, a simulation will give us a snapshot at a single point in time.

A **dynamic model** does account for the element of time. This type of model often contains state variables that change over time.

A **discrete model** does not take into account the function of time. The state variables change only at a countable number of points in time, abruptly from one state to another.

A **continuous model** does take into account the function of time, typically by modelling a function f(t) and the changes reflected over time intervals. The state variables change in an unbroken way through an infinite number of states.

**Predictive nondeterminism (Lecture 5 Segment 1)**

- Our inability to make accurate measurements about the physical world, makes it impossible to make precise predictions about future states.
- This is in contrast to the notion of causal nondeterminism: the belief that not every event is caused by previous events.
- It is of no practical importance whether we can't make such predictions because they are simply not possible, or because we lack sufficient information to make them.

**Stochastic processes**

- A stochastic process is an ongoing process where the next state might depend on both the previous states and some random element.

**Specfications and implementations**

- Specification allows but does not require, a nondeterministic implementation.
- It can be difficult when debugging a programme that uses it.
