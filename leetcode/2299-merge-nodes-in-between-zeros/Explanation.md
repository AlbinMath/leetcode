# LeetCode 2181: Merge Nodes in Between Zeros

**LeetCode Problem #2181 — Merge Nodes in Between Zeros**
Solve LeetCode Merge Nodes in Between Zeros using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Merge Nodes in Between Zeros |
| LeetCode | #2181 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given the  head  of a linked list, which contains a series of integers  separated  by  0 &#39;s. The  beginning  and  end  of the linked list will have  Node.val == 0 .

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
We iterate through the input using **Pointer Traversal & Node Manipulation**. By maintaining state efficiently in a **Linked List**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Two Pointer Convergence & Scanning**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Merge Nodes in Between Zeros**. Applying **Two Pointer Convergence & Scanning** yields the target result step by step.

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
- [783. Minimum Distance Between BST Nodes](../0799-minimum-distance-between-bst-nodes/)
- [2058. Find the Minimum and Maximum Number of Nodes Between Critical Points](../2182-find-the-minimum-and-maximum-number-of-nodes-between-critical-points/)
- [2482. Difference Between Ones and Zeros in Row and Column](../2606-difference-between-ones-and-zeros-in-row-and-column/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/merge-nodes-in-between-zeros/)
