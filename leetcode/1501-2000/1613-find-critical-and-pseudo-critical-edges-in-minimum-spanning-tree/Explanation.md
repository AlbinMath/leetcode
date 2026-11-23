# LeetCode 1489: Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree

**LeetCode Problem #1489 — Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree**
Solve LeetCode Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree using Python and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree |
| LeetCode | #1489 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given a weighted undirected connected graph with  n  vertices numbered from  0  to  n - 1 , and an array  edges  where  edges[i] = [a i , b i , weight i ]  represents a bidirectional and weighted edge between nodes  a i   and  b i  . A minimum spanning tree (MST) is a subset of the graph&#39;s edges that connects all vertices without cycles and with the minimum possible total edge weight.

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
We iterate through the input using **Depth-First Search (DFS) / Breadth-First Search (BFS)**. By maintaining state efficiently in a **Tree / Graph / Grid**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Sorted Array**).
2. Process elements sequentially using **Modified Binary Search**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree**. Applying **Modified Binary Search** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Binary Search**

## Topics
- Binary Search
- Divide and Conquer
- Search Space

## Language
Python

## Source Code
- [solution.py](./solution.py)

## Why This Works
By utilizing **Binary Search**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Applying standard binary search without accounting for array rotation or duplicates.
2. Off-by-one errors when updating boundary pointers (`left = mid + 1` vs `right = mid - 1`).
3. Integer overflow during midpoint calculation (use `mid = left + (right - left) // 2`).

## Interview Notes
- **Tests:** Logarithmic search space reduction, boundary handling, and invariant preservation.
- **Follow-up:** How does performance change if the array contains duplicate elements?

## Related Problems
- [2058. Find the Minimum and Maximum Number of Nodes Between Critical Points](../../2001-2500/2182-find-the-minimum-and-maximum-number-of-nodes-between-critical-points/)
- [3123. Find Edges in Shortest Paths](../../3001-3500/3386-find-edges-in-shortest-paths/)
- [3924. Minimum Threshold Path With Limited Heavy Edges](../../4001-4500/4102-minimum-threshold-path-with-limited-heavy-edges/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/)
