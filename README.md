# goit-algo-hw-06

# Graph Pathfinding with DFS and BFS

This project demonstrates the use of Depth-First Search (DFS) and Breadth-First Search (BFS) algorithms to find paths in a graph. The graph is represented as an adjacency list.

## Results

### DFS Results

**Nodes Visited:**
A B E H I J G D F C


**DFS Path Dictionary:**
{
'A': 'A',
'C': 'F',
'B': 'A',
'D': 'G',
'E': 'B',
'H': 'E',
'I': 'H',
'F': 'I',
'J': 'I',
'G': 'J'
}


### BFS Results

**Nodes Visited:**
A C B F D E I G H J


**BFS Path Dictionary:**
{
'A': 'A',
'C': 'A',
'B': 'A',
'F': 'C',
'D': 'B',
'E': 'B',
'I': 'F',
'G': 'D',
'H': 'I',
'J': 'G'
}


### Path from A to I

**DFS Path:**
I H E B A


**BFS Path:**
I F C A


## Explanation of Results

### DFS (Depth-First Search)

DFS explores as far down a branch as possible before backtracking to explore other branches. Therefore, the order of visiting nodes is `A B E H I J G D F C`.

- The path dictionary shows how each node is discovered by DFS. For example, node `I` was found via `H`, which was found via `E`, and so on.
- The path from `A` to `I` using DFS is `I H E B A`. This demonstrates deep traversal until the node `I` is found.

### BFS (Breadth-First Search)

BFS explores all neighboring nodes at the present depth level before moving on to nodes at the next depth level. Therefore, the order of visiting nodes is `A C B F D E I G H J`.

- The path dictionary shows how each node is discovered by BFS. For example, node `I` was found via `F`, which was found via `C`, and so on.
- The path from `A` to `I` using BFS is `I F C A`. This demonstrates a broad, level-by-level traversal until the node `I` is found.

### Comparison and Conclusions

- **DFS** finds a path by deeply traversing one branch of the graph before backtracking and exploring other branches. This results in paths that may be longer in terms of the sequence of nodes but are more direct in terms of traversal.
- **BFS** finds the shortest path in terms of the number of steps between the start and end nodes because it explores all neighbors at each level before moving deeper. This results in shorter paths in terms of steps, but these paths might be less direct.

The paths found by these algorithms differ due to their fundamental approaches to graph exploration: DFS tends to explore deeper first, while BFS explores more broadly at each level.
