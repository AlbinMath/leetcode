# LeetCode 3120: Count the Number of Special Characters I

**LeetCode Problem #3120 — Count the Number of Special Characters I**
Solve LeetCode Count the Number of Special Characters I using C++ and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count the Number of Special Characters I |
| LeetCode | #3120 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given a string  word . A letter is called  special  if it appears  both  in lowercase and uppercase in  word .

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Iterative Traversal**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Count the Number of Special Characters I**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [1995. Count Special Quadruplets](../../2001-2500/2122-count-special-quadruplets/)
- [2844. Minimum Operations to Make a Special Number](../../3001-3500/3046-minimum-operations-to-make-a-special-number/)
- [3233. Find the Count of Numbers Which Are Not Special](../../3501-4000/3507-find-the-count-of-numbers-which-are-not-special/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-the-number-of-special-characters-i/)
