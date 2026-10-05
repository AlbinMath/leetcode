# LeetCode 115: Distinct Subsequences

**LeetCode Problem #115 — Distinct Subsequences**
Solve LeetCode Distinct Subsequences using JavaScript and Database / SQL. This solution finds the optimal result using SQL Query / Relational Join & Grouping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Distinct Subsequences |
| LeetCode | #115 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | SQL Query / Relational Join & Grouping |
| Data Structure | Relational Table |
| Pattern | Database / SQL |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Given two strings s and t, return  the number of distinct    subsequences    of  s  which equals  t.

## Key Insight
Leverage **Database / SQL** with **Relational Table** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code uses **1D Dynamic Programming** with space optimization.

1. **DP Definition:** `dp[j]` represents the number of distinct subsequences of `s[0..i-1]` that equal `t[0..j-1]`.
2. **Base Case:** `dp[0] = 1` because the empty string `""` is always a subsequence of any string (by deleting all characters).
3. **Iteration:** For each character `s[i-1]` (outer loop over `s`):
   - It iterates **backwards** over `j` (from `n` down to `1`) to avoid overwriting values that are still needed.
   - If `s[i-1] === t[j-1]`, then `dp[j] += dp[j-1]`. This means: the number of ways to form `t[0..j-1]` includes both (a) the ways without using `s[i-1]` (existing `dp[j]`) and (b) the ways that use `s[i-1]` to match `t[j-1]` (which is `dp[j-1]`).
4. The answer is `dp[n]` — the number of ways to form the entire string `t`.

Time complexity is $O(M \times N)$ where $M$ and $N$ are the lengths of `s` and `t`. Space complexity is $O(N)$.

## Algorithm
1. Initialize state variables / data structure (**Relational Table**).
2. Process elements sequentially using **SQL Query / Relational Join & Grouping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Distinct Subsequences**. Applying **SQL Query / Relational Join & Grouping** yields the target result step by step.

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
JavaScript

## Source Code
- [solution.js](./solution.js)

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
- [977. Squares of a Sorted Array](../0977-distinct-subsequences-ii/)
- [1159. Market Analysis II](../1159-smallest-subsequence-of-distinct-characters/)
- [3608. Minimum Time for K Connected Components](../3608-find-the-number-of-subsequences-with-equal-gcd/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/distinct-subsequences/)
