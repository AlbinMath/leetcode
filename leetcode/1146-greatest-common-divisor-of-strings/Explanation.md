# LeetCode 1071: Greatest Common Divisor of Strings

**LeetCode Problem #1071 — Greatest Common Divisor of Strings**
Solve LeetCode Greatest Common Divisor of Strings using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Greatest Common Divisor of Strings |
| LeetCode | #1071 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
For two strings  s  and  t , we say " t  divides  s " if and only if  s = t + t + t + ... + t + t  (i.e.,  t  is concatenated with itself one or more times).

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Greatest Common Divisor of Strings**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [1979. Find Greatest Common Divisor of Array](../2106-find-greatest-common-divisor-of-array/)
- [14. Longest Common Prefix](../0014-longest-common-prefix/)
- [43. Multiply Strings](../0043-multiply-strings/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/greatest-common-divisor-of-strings/)
