# LeetCode 1910: Remove All Occurrences of a Substring

**LeetCode Problem #1910 — Remove All Occurrences of a Substring**
Solve LeetCode Remove All Occurrences of a Substring using C++ and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Remove All Occurrences of a Substring |
| LeetCode | #1910 |
| Difficulty | Medium |
| Language | C++ |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given two strings  s  and  part , perform the following operation on  s  until  all  occurrences of the substring  part  are removed:

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Remove All Occurrences of a Substring**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Array / General**

## Topics
- Array

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)

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
- [1297. Maximum Number of Occurrences of a Substring](../../1001-1500/1423-maximum-number-of-occurrences-of-a-substring/)
- [1941. Check if All Characters Have Equal Number of Occurrences](../../2001-2500/2053-check-if-all-characters-have-equal-number-of-occurrences/)
- [3090. Maximum Length Substring With Two Occurrences](../../3001-3500/3349-maximum-length-substring-with-two-occurrences/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/remove-all-occurrences-of-a-substring/)
