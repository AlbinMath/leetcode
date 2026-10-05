# LeetCode 812: Largest Triangle Area

**LeetCode Problem #812 — Largest Triangle Area**
Solve LeetCode Largest Triangle Area using C++ and Math & Logic. This solution finds the optimal result using Mathematical Simulation / Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Largest Triangle Area |
| LeetCode | #812 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | Mathematical Simulation / Modular Arithmetic |
| Data Structure | Primitive Data Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given two strings  s  and  goal , return  true   if and only if   s   can become   goal   after some number of  shifts  on   s .

## Key Insight
Leverage **Math & Logic** with **Primitive Data Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code uses a clever **string concatenation** trick:

1. **Length Check:** If the lengths differ, return `false` immediately.
2. **Concatenation:** It concatenates `s` with itself: `s + s`. This doubled string contains every possible rotation of `s` as a substring. For example, `"abcde" + "abcde" = "abcdeabcde"` contains `"cdeab"` as a substring.
3. **Find:** It checks if `goal` exists anywhere in `s + s` using `.find()`. If found, `goal` is a valid rotation.

Time complexity is $O(N)$ with an efficient string search and space complexity is $O(N)$ for the concatenated string.

## Algorithm
1. Initialize state variables / data structure (**Primitive Data Types**).
2. Process elements sequentially using **Mathematical Simulation / Modular Arithmetic**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Largest Triangle Area**. Applying **Mathematical Simulation / Modular Arithmetic** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Math & Logic**

## Topics
- Math
- Simulation

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)

## Why This Works
By utilizing **Math & Logic**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [48. Rotate Image](../0048-rotate-image/)
- [61. Rotate List](../0061-rotate-list/)
- [396. Rotate Function](../0396-rotate-function/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/rotate-string/)
