# LeetCode 2316: Count Unreachable Pairs of Nodes in an Undirected Graph

**LeetCode Problem #2316 — Count Unreachable Pairs of Nodes in an Undirected Graph**
Solve LeetCode Count Unreachable Pairs of Nodes in an Undirected Graph using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Unreachable Pairs of Nodes in an Undirected Graph |
| LeetCode | #2316 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given an integer  n . There is an  undirected  graph with  n  nodes, numbered from  0  to  n - 1 . You are given a 2D integer array  edges  where  edges[i] = [a i , b i ]  denotes that there exists an  undirected  edge connecting nodes  a i   and  b i  .

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
We iterate through the input using **Pointer Traversal & Node Manipulation**. By maintaining state efficiently in a **Linked List**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Two Pointer Convergence & Scanning**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Count Unreachable Pairs of Nodes in an Undirected Graph**. Applying **Two Pointer Convergence & Scanning** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

## Language
Python

## Source Code
- [solution.py](./solution.py)

## Why This Works
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [2876. Count Visited Nodes in a Directed Graph](../../3001-3500/3140-count-visited-nodes-in-a-directed-graph/)
- [1782. Count Pairs Of Nodes](../../1501-2000/1891-count-pairs-of-nodes/)
- [882. Reachable Nodes In Subdivided Graph](../../0501-1000/0918-reachable-nodes-in-subdivided-graph/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/)
