# LeetCode 2625: Flatten Deeply Nested Array

**LeetCode Problem #2625 — Flatten Deeply Nested Array**
Solve LeetCode Flatten Deeply Nested Array using TypeScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Flatten Deeply Nested Array |
| LeetCode | #2625 |
| Difficulty | Medium |
| Language | TypeScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given a  multi-dimensional  array  arr  and a depth  n , return a  flattened  version of that array.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
Uses recursion: if depth > 0, iterate through elements. If an element is an array, recursively flatten it with `depth - 1`. Otherwise, add the element directly to the result.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Two Pointer Convergence & Scanning**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Flatten Deeply Nested Array**. Applying **Two Pointer Convergence & Scanning** yields the target result step by step.

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
TypeScript

## Source Code
- [solution.ts](./solution.ts)

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
- [341. Flatten Nested List Iterator](../../0001-0500/0341-flatten-nested-list-iterator/)
- [2649. Nested Array Generator](../../2501-3000/2783-nested-array-generator/)
- [114. Flatten Binary Tree to Linked List](../../0001-0500/0114-flatten-binary-tree-to-linked-list/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/flatten-deeply-nested-array/)
