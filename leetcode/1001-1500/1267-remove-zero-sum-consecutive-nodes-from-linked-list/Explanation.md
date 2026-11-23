# LeetCode 1171: Remove Zero Sum Consecutive Nodes from Linked List

**LeetCode Problem #1171 — Remove Zero Sum Consecutive Nodes from Linked List**
Solve LeetCode Remove Zero Sum Consecutive Nodes from Linked List using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Remove Zero Sum Consecutive Nodes from Linked List |
| LeetCode | #1171 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given the  head  of a linked list, we repeatedly delete consecutive sequences of nodes that sum to  0  until there are no such sequences.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
We iterate through the input using **Pointer Traversal & Node Manipulation**. By maintaining state efficiently in a **Linked List**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Two Pointer Convergence & Scanning**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Remove Zero Sum Consecutive Nodes from Linked List**. Applying **Two Pointer Convergence & Scanning** yields the target result step by step.

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
- [2487. Remove Nodes From Linked List](../../2501-3000/2573-remove-nodes-from-linked-list/)
- [3217. Delete Nodes From Linked List Present in Array](../../3501-4000/3501-delete-nodes-from-linked-list-present-in-array/)
- [203. Remove Linked List Elements](../../0001-0500/0203-remove-linked-list-elements/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/)
