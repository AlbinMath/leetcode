# LeetCode 341: Flatten Nested List Iterator

**LeetCode Problem #341 — Flatten Nested List Iterator**
Solve LeetCode Flatten Nested List Iterator using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Flatten Nested List Iterator |
| LeetCode | #341 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given a nested list of integers  nestedList . Each element is either an integer or a list whose elements may also be integers or other lists. Implement an iterator to flatten it.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Two Pointer Convergence & Scanning**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Flatten Nested List Iterator**. Applying **Two Pointer Convergence & Scanning** yields the target result step by step.

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
- [114. Flatten Binary Tree to Linked List](../../0001-0500/0114-flatten-binary-tree-to-linked-list/)
- [430. Flatten a Multilevel Doubly Linked List](../../0501-1000/0766-flatten-a-multilevel-doubly-linked-list/)
- [2625. Flatten Deeply Nested Array](../../2501-3000/2759-flatten-deeply-nested-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/flatten-nested-list-iterator/)
