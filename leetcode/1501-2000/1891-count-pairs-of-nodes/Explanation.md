# LeetCode 1782: Count Pairs Of Nodes

**LeetCode Problem #1782 — Count Pairs Of Nodes**
Solve LeetCode Count Pairs Of Nodes using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Pairs Of Nodes |
| LeetCode | #1782 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given an undirected graph defined by an integer  n , the number of nodes, and a 2D integer array  edges , the edges in the graph, where  edges[i] = [u i , v i ]  indicates that there is an  undirected  edge between  u i   and  v i  . You are also given an integer array  queries .

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
We iterate through the input using **Pointer Traversal & Node Manipulation**. By maintaining state efficiently in a **Linked List**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Two Pointer Convergence & Scanning**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Count Pairs Of Nodes**. Applying **Two Pointer Convergence & Scanning** yields the target result step by step.

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
JavaScript

## Source Code
- [solution.js](./solution.js)

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
- [2316. Count Unreachable Pairs of Nodes in an Undirected Graph](../../2001-2500/2403-count-unreachable-pairs-of-nodes-in-an-undirected-graph/)
- [24. Swap Nodes in Pairs](../../0001-0500/0024-swap-nodes-in-pairs/)
- [222. Count Complete Tree Nodes](../../0001-0500/0222-count-complete-tree-nodes/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-pairs-of-nodes/)
