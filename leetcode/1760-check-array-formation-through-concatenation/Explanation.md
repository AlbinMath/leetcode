# LeetCode 1640: Check Array Formation Through Concatenation

**LeetCode Problem #1640 — Check Array Formation Through Concatenation**
Solve LeetCode Check Array Formation Through Concatenation using C++ and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Check Array Formation Through Concatenation |
| LeetCode | #1640 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given an array of  distinct  integers  arr  and an array of integer arrays  pieces , where the integers in  pieces  are  distinct . Your goal is to form  arr  by concatenating the arrays in  pieces   in any order . However, you are  not  allowed to reorder the integers in each array  pieces[i] .

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Check Array Formation Through Concatenation**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [1752. Check if Array Is Sorted and Rotated](../1878-check-if-array-is-sorted-and-rotated/)
- [1929. Concatenation of Array](../2058-concatenation-of-array/)
- [1961. Check If String Is a Prefix of Array](../2093-check-if-string-is-a-prefix-of-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/check-array-formation-through-concatenation/)
