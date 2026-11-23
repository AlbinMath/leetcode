# LeetCode 2625: Flatten Deeply Nested Array

**LeetCode Problem #2625 — Flatten Deeply Nested Array**
Solve LeetCode Flatten Deeply Nested Array using TypeScript and Linked List. This solution finds the optimal result using Pointer Traversal & Node Manipulation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Flatten Deeply Nested Array |
| LeetCode | #2625 |
| Difficulty | Medium |
| Language | TypeScript |
| Algorithm | Pointer Traversal & Node Manipulation |
| Data Structure | Linked List |
| Pattern | Linked List |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given a  multi-dimensional  array  arr  and a depth  n , return a  flattened  version of that array.

## Key Insight
Leverage **Linked List** with **Linked List** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
Uses recursion: if depth > 0, iterate through elements. If an element is an array, recursively flatten it with `depth - 1`. Otherwise, add the element directly to the result.

## Algorithm
1. Initialize state variables / data structure (**Linked List**).
2. Process elements sequentially using **Pointer Traversal & Node Manipulation**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Flatten Deeply Nested Array**. Applying **Pointer Traversal & Node Manipulation** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Linked List**

## Topics
- Linked List
- Two Pointers

## Language
TypeScript

## Source Code
- [solution.ts](./solution.ts)

## Why This Works
By utilizing **Linked List**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [341. Flatten Nested List Iterator](../0341-flatten-nested-list-iterator/)
- [2649. Nested Array Generator](../2783-nested-array-generator/)
- [114. Flatten Binary Tree to Linked List](../0114-flatten-binary-tree-to-linked-list/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/flatten-deeply-nested-array/)
