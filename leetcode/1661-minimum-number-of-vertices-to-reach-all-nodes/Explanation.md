# LeetCode 1557: Minimum Number of Vertices to Reach All Nodes

**LeetCode Problem #1557 — Minimum Number of Vertices to Reach All Nodes**
Solve LeetCode Minimum Number of Vertices to Reach All Nodes using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Number of Vertices to Reach All Nodes |
| LeetCode | #1557 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given a  directed acyclic graph , with  n  vertices numbered from  0  to  n-1 , and an array  edges  where  edges[i] = [from i , to i ]  represents a directed edge from node  from i   to node  to i  .

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
We iterate through the input using **Pointer Traversal & Node Manipulation**. By maintaining state efficiently in a **Linked List**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Two Pointer Convergence & Scanning**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Minimum Number of Vertices to Reach All Nodes**. Applying **Two Pointer Convergence & Scanning** yields the target result step by step.

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
- [2058. Find the Minimum and Maximum Number of Nodes Between Critical Points](../2182-find-the-minimum-and-maximum-number-of-nodes-between-critical-points/)
- [1769. Minimum Number of Operations to Move All Balls to Each Box](../1895-minimum-number-of-operations-to-move-all-balls-to-each-box/)
- [1850. Minimum Adjacent Swaps to Reach the Kth Smallest Number](../1978-minimum-adjacent-swaps-to-reach-the-kth-smallest-number/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/)
