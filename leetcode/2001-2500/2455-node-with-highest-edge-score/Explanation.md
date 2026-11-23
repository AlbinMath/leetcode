# LeetCode 2374: Node With Highest Edge Score

**LeetCode Problem #2374 — Node With Highest Edge Score**
Solve LeetCode Node With Highest Edge Score using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Node With Highest Edge Score |
| LeetCode | #2374 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given a directed graph with  n  nodes labeled from  0  to  n - 1 , where each node has  exactly one  outgoing edge.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
We iterate through the input using **Pointer Traversal & Node Manipulation**. By maintaining state efficiently in a **Linked List**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Two Pointer Convergence & Scanning**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Node With Highest Edge Score**. Applying **Two Pointer Convergence & Scanning** yields the target result step by step.

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
- [2858. Minimum Edge Reversals So Every Node Is Reachable](../../3001-3500/3105-minimum-edge-reversals-so-every-node-is-reachable/)
- [2242. Maximum Score of a Node Sequence](../../2001-2500/2353-maximum-score-of-a-node-sequence/)
- [2049. Count Nodes With the Highest Score](../../2001-2500/2175-count-nodes-with-the-highest-score/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/node-with-highest-edge-score/)
