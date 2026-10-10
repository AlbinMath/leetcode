# LeetCode 1790: Check if One String Swap Can Make Strings Equal

**LeetCode Problem #1790 — Check if One String Swap Can Make Strings Equal**
Solve LeetCode Check if One String Swap Can Make Strings Equal using C++ and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Check if One String Swap Can Make Strings Equal |
| LeetCode | #1790 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given two strings  s1  and  s2  of equal length. A  string swap  is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Check if One String Swap Can Make Strings Equal**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [1784. Check if Binary String Has at Most One Segment of Ones](../1910-check-if-binary-string-has-at-most-one-segment-of-ones/)
- [1662. Check If Two String Arrays are Equivalent](../1781-check-if-two-string-arrays-are-equivalent/)
- [1897. Redistribute Characters to Make All Strings Equal](../2025-redistribute-characters-to-make-all-strings-equal/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/)
