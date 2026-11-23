# LeetCode 2192: All Ancestors of a Node in a Directed Acyclic Graph

**LeetCode Problem #2192 — All Ancestors of a Node in a Directed Acyclic Graph**
Solve LeetCode All Ancestors of a Node in a Directed Acyclic Graph using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | All Ancestors of a Node in a Directed Acyclic Graph |
| LeetCode | #2192 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given a positive integer  n  representing the number of nodes of a  Directed Acyclic Graph  (DAG). The nodes are numbered from  0  to  n - 1  ( inclusive ).

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
We iterate through the input using **Pointer Traversal & Node Manipulation**. By maintaining state efficiently in a **Linked List**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Two Pointer Convergence & Scanning**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **All Ancestors of a Node in a Directed Acyclic Graph**. Applying **Two Pointer Convergence & Scanning** yields the target result step by step.

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
- [1857. Largest Color Value in a Directed Graph](../1986-largest-color-value-in-a-directed-graph/)
- [2876. Count Visited Nodes in a Directed Graph](../3140-count-visited-nodes-in-a-directed-graph/)
- [3604. Minimum Time to Reach Destination in Directed Graph](../3916-minimum-time-to-reach-destination-in-directed-graph/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/)
