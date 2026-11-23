# LeetCode 1754: Largest Merge Of Two Strings

**LeetCode Problem #1754 — Largest Merge Of Two Strings**
Solve LeetCode Largest Merge Of Two Strings using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Largest Merge Of Two Strings |
| LeetCode | #1754 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given two strings  word1  and  word2 . You want to construct a string  merge  in the following way: while either  word1  or  word2  are non-empty, choose  one  of the following options:

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Largest Merge Of Two Strings**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Array / General**

## Topics
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)

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
- [21. Merge Two Sorted Lists](../0021-merge-two-sorted-lists/)
- [617. Merge Two Binary Trees](../0617-merge-two-binary-trees/)
- [1768. Merge Strings Alternately](../1894-merge-strings-alternately/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/largest-merge-of-two-strings/)
