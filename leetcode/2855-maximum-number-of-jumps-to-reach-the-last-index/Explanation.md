# LeetCode 2855: Minimum Right Shifts to Sort the Array

**LeetCode Problem #2855 — Minimum Right Shifts to Sort the Array**
Solve LeetCode Minimum Right Shifts to Sort the Array using C++ and Database / SQL. This solution finds the optimal result using SQL Query / Relational Join & Grouping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Right Shifts to Sort the Array |
| LeetCode | #2855 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | SQL Query / Relational Join & Grouping |
| Data Structure | Relational Table |
| Pattern | Database / SQL |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given a  0-indexed  array  nums  of  n  integers and an integer  target .

## Key Insight
Leverage **Database / SQL** with **Relational Table** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
Uses **DP** where `dp[i]` = max jumps to reach index `i`. For each `i`, check all `j < i` where the jump is valid and update `dp[i] = max(dp[i], dp[j] + 1)`. Return `dp[n-1]` or -1 if unreachable.

## Algorithm
1. Initialize state variables / data structure (**Relational Table**).
2. Process elements sequentially using **SQL Query / Relational Join & Grouping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Minimum Right Shifts to Sort the Array**. Applying **SQL Query / Relational Join & Grouping** yields the target result step by step.

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
- [1297. Maximum Number of Occurrences of a Substring](../1297-maximum-number-of-balloons/)
- [1644. Lowest Common Ancestor of a Binary Tree II](../1644-maximum-number-of-non-overlapping-substrings/)
- [2182. Construct String With Repeat Limit](../2182-find-the-minimum-and-maximum-number-of-nodes-between-critical-points/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index/)
