# LeetCode 2349: Design a Number Container System

**LeetCode Problem #2349 — Design a Number Container System**
Solve LeetCode Design a Number Container System using C++ and Database / SQL. This solution finds the optimal result using SQL Query / Relational Join & Grouping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Design a Number Container System |
| LeetCode | #2349 |
| Difficulty | Medium |
| Language | C++ |
| Algorithm | SQL Query / Relational Join & Grouping |
| Data Structure | Relational Table |
| Pattern | Database / SQL |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
A parentheses string is a  non-empty  string consisting only of  &#39;(&#39;  and  &#39;)&#39; . It is  valid  if  any  of the following conditions is  true :

## Key Insight
Leverage **Database / SQL** with **Relational Table** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
Uses **DP with state tracking**. At each cell, track the set of possible open-parenthesis counts. Moving right or down, increment count for `(` and decrement for `)`. A path is valid if we reach the bottom-right with count exactly 0. Prune states where count goes negative.

## Algorithm
1. Initialize state variables / data structure (**Relational Table**).
2. Process elements sequentially using **SQL Query / Relational Join & Grouping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Design a Number Container System**. Applying **SQL Query / Relational Join & Grouping** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

## Pattern
**Database / SQL**

## Topics
- Database
- SQL
- Data Aggregation

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)

## Why This Works
By utilizing **Database / SQL**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [20. Valid Parentheses](../0020-valid-parentheses/)
- [1208. Get Equal Substrings Within Budget](../1208-maximum-nesting-depth-of-two-valid-parentheses-strings/)
- [1878. Get Biggest Three Rhombus Sums in a Grid](../1878-check-if-array-is-sorted-and-rotated/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/check-if-there-is-a-valid-parentheses-string-path/)
