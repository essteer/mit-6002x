# DFS and BFS

**Depth-first search (DFS)**

- similar to left-first depth-first method of enumerating a search tree
- main difference is that graph might have cycles, so we must keep track of the nodes we have visited

**Breadth-first search (BFS)**

- explores multiple paths simultaneously
- concludes once (if) one of those paths reaches the destination
- explore all paths with n hops before exploring any path with >n hops
- the first path found is therefore a shortest path

**Weighted shortest path**

- want to minimise the sum of edge weights, not the number of edges
- DFS can be modified for this
- BFS cannot - because it works simply on the number of nodes / edges; the shortest weighted path may have more than the permitted number of hops
