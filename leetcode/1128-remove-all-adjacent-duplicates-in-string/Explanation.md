# LeetCode 1047: Remove All Adjacent Duplicates In String

**LeetCode Problem #1047 — Remove All Adjacent Duplicates In String**
Solve LeetCode Remove All Adjacent Duplicates In String using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Remove All Adjacent Duplicates In String |
| LeetCode | #1047 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given a string  s  consisting of lowercase English letters. A  duplicate removal  consists of choosing two  adjacent  and  equal  letters and removing them.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Remove All Adjacent Duplicates In String**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [26. Remove Duplicates from Sorted Array](../0026-remove-duplicates-from-sorted-array/)
- [80. Remove Duplicates from Sorted Array II](../0080-remove-duplicates-from-sorted-array-ii/)
- [82. Remove Duplicates from Sorted List II](../0082-remove-duplicates-from-sorted-list-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/)
