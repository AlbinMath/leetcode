# LeetCode 2074: Reverse Nodes in Even Length Groups

**LeetCode Problem #2074 — Reverse Nodes in Even Length Groups**
Solve LeetCode Reverse Nodes in Even Length Groups using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Reverse Nodes in Even Length Groups |
| LeetCode | #2074 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given the  head  of a linked list.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
We iterate through the input using **Pointer Traversal & Node Manipulation**. By maintaining state efficiently in a **Linked List**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Two Pointer Convergence & Scanning**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Reverse Nodes in Even Length Groups**. Applying **Two Pointer Convergence & Scanning** yields the target result step by step.

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
- [25. Reverse Nodes in k-Group](../../0001-0500/0025-reverse-nodes-in-k-group/)
- [1315. Sum of Nodes with Even-Valued Grandparent](../../1001-1500/1243-sum-of-nodes-with-even-valued-grandparent/)
- [2508. Add Edges to Make Degrees of All Nodes Even](../../2501-3000/2596-add-edges-to-make-degrees-of-all-nodes-even/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/reverse-nodes-in-even-length-groups/)
