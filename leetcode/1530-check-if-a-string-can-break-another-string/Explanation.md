# LeetCode 1433: Check If a String Can Break Another String

**LeetCode Problem #1433 — Check If a String Can Break Another String**
Solve LeetCode Check If a String Can Break Another String using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Check If a String Can Break Another String |
| LeetCode | #1433 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given two strings:  s1  and  s2  with the same size, check if some permutation of string  s1  can break some permutation of string  s2  or vice-versa. In other words  s2  can break  s1  or vice-versa.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Check If a String Can Break Another String**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [2267.  Check if There Is a Valid Parentheses String Path](../2349-check-if-there-is-a-valid-parentheses-string-path/)
- [1790. Check if One String Swap Can Make Strings Equal](../1915-check-if-one-string-swap-can-make-strings-equal/)
- [2116. Check if a Parentheses String Can Be Valid](../2221-check-if-a-parentheses-string-can-be-valid/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/check-if-a-string-can-break-another-string/)
