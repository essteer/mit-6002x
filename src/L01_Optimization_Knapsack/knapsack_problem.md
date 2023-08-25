# 0/1 knapsack problem

- Each item represented by a pair, <value, weight>
- Knapsack can accommodate items with a total weight <= w
- Vector I, of length n, represents set of available items; each vector element is an item
- Vector V, of length n, represents whether an item is taken:
- If V[i] = 1, item I[i] is taken; if V[i] = 0, item I[i] is not taken
- Find a V that maximises the value of the items, under the weight constraint

## Brute force algorithm

- Enumerate all possible combinations of items
- Remove all combinations for which total units > allowed weight
- From remaining combinations, pick any one with largest value

# Knapsack problem is inherently exponential

One alternative is an approximate solution - using a greedy algorithm.

## Greedy algorithm

- While knapsack not full, put best available item in knapsack
- "Best" could be the most valuable, cheapest, highest value/unit ratio
- Answers may differ due to local optima varying by constraints of what "best" is

- Greedy algorithms therefore do not necessarily result in the true optimum solution
