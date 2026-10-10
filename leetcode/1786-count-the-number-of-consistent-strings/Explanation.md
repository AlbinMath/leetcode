# LeetCode 1684: Count the Number of Consistent Strings

**LeetCode Problem #1684 — Count the Number of Consistent Strings**
Solve LeetCode Count the Number of Consistent Strings using C++ and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count the Number of Consistent Strings |
| LeetCode | #1684 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given a string  allowed  consisting of  distinct  characters and an array of strings  words . A string is  consistent  if all characters in the string appear in the string  allowed .

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Count the Number of Consistent Strings**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [1967. Number of Strings That Appear as Substrings in Word](../2099-number-of-strings-that-appear-as-substrings-in-word/)
- [2685. Count the Number of Complete Components](../2793-count-the-number-of-complete-components/)
- [3120. Count the Number of Special Characters I](../3408-count-the-number-of-special-characters-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-the-number-of-consistent-strings/)
