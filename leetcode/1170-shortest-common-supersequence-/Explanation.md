# LeetCode 1092: Shortest Common Supersequence 

**LeetCode Problem #1092 — Shortest Common Supersequence **
Solve LeetCode Shortest Common Supersequence  using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Shortest Common Supersequence  |
| LeetCode | #1092 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given two strings  str1  and  str2 , return  the shortest string that has both   str1   and   str2   as  subsequences  . If there are multiple valid strings, return  any  of them.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Shortest Common Supersequence **. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [14. Longest Common Prefix](../0014-longest-common-prefix/)
- [235. Lowest Common Ancestor of a Binary Search Tree](../0235-lowest-common-ancestor-of-a-binary-search-tree/)
- [236. Lowest Common Ancestor of a Binary Tree](../0236-lowest-common-ancestor-of-a-binary-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/shortest-common-supersequence/)
