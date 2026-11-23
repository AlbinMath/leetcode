# LeetCode 341: Flatten Nested List Iterator

**LeetCode Problem #341 — Flatten Nested List Iterator**
Solve LeetCode Flatten Nested List Iterator using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Flatten Nested List Iterator |
| LeetCode | #341 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given a nested list of integers  nestedList . Each element is either an integer or a list whose elements may also be integers or other lists. Implement an iterator to flatten it.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Flatten Nested List Iterator**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Array / General**

## Topics
- Array

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)

## Why This Works
By utilizing **Array / General**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [114. Flatten Binary Tree to Linked List](../0114-flatten-binary-tree-to-linked-list/)
- [430. Flatten a Multilevel Doubly Linked List](../0766-flatten-a-multilevel-doubly-linked-list/)
- [2625. Flatten Deeply Nested Array](../2759-flatten-deeply-nested-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/flatten-nested-list-iterator/)
