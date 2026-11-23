# LeetCode 2858: Minimum Edge Reversals So Every Node Is Reachable

**LeetCode Problem #2858 — Minimum Edge Reversals So Every Node Is Reachable**
Solve LeetCode Minimum Edge Reversals So Every Node Is Reachable using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Edge Reversals So Every Node Is Reachable |
| LeetCode | #2858 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
There is a  simple directed graph  with  n  nodes labeled from  0  to  n - 1 . The graph would form a  tree  if its edges were bi-directional.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
We iterate through the input using **Pointer Traversal & Node Manipulation**. By maintaining state efficiently in a **Linked List**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Two Pointer Convergence & Scanning**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Minimum Edge Reversals So Every Node Is Reachable**. Applying **Two Pointer Convergence & Scanning** yields the target result step by step.

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
- [3650. Minimum Cost Path with Edge Reversals](../3887-minimum-cost-path-with-edge-reversals/)
- [671. Second Minimum Node In a Binary Tree](../0671-second-minimum-node-in-a-binary-tree/)
- [2374. Node With Highest Edge Score](../2455-node-with-highest-edge-score/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-edge-reversals-so-every-node-is-reachable/)
