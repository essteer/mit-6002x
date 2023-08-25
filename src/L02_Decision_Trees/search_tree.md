# Search tree implementation - with brute force

- Tree build from top down, starting with the root
- First element is selected from still to be considered items

- If there is room in the knapsack, a node is constructed that reflects the consequence of choosing to take that item
- This is drawn as the left child
- The right child explores the consequences of not taking that item

- The process is then applied recursively to non-leaf children

## Computational complexity

- Time based on number of nodes generated
- Number of levels is number of items to choose from
- Number of nodes at level i is 2^i

- O(2^(i+1)) - exponential complexity for brute force algorithm

# Memoization - dynamic programming

- Memoization is an efficient solution to the problem of exponential complexity for search trees
- Do not repeat the same calculations
- Make a memo of them and refer back to them

To work, dynamic programming requires:

- optimal substructure
- overlapping subproblems

- this can be adapted for the search tree used for 0/1 knapsack problems
- it does not work for merge sort, which does not have overlapping subproblems
