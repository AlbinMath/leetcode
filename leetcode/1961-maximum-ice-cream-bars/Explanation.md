# LeetCode 1961: Check If String Is a Prefix of Array

**LeetCode Problem #1961 — Check If String Is a Prefix of Array**
Solve LeetCode Check If String Is a Prefix of Array using Java and Database / SQL. This solution finds the optimal result using SQL Query / Relational Join & Grouping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Check If String Is a Prefix of Array |
| LeetCode | #1961 |
| Difficulty | Easy |
| Language | Java |
| Algorithm | SQL Query / Relational Join & Grouping |
| Data Structure | Relational Table |
| Pattern | Database / SQL |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
It is a sweltering summer day, and a boy wants to buy some ice cream bars.

## Key Insight
Leverage **Database / SQL** with **Relational Table** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
1. **Sort** the costs in ascending order.
2. **Greedy:** Buy the cheapest bars first. Iterate through sorted costs, subtracting each cost from coins. Stop when you can't afford the next bar.
3. Return the count.

Time complexity is $O(N \log N)$ and space complexity is $O(\log N)$.

## Algorithm
1. Initialize state variables / data structure (**Relational Table**).
2. Process elements sequentially using **SQL Query / Relational Join & Grouping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Check If String Is a Prefix of Array**. Applying **SQL Query / Relational Join & Grouping** yields the target result step by step.

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
Java

## Source Code
- [solution.java](./solution.java)

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
- [628. Maximum Product of Three Numbers](../0628-maximum-product-of-three-numbers/)
- [1208. Get Equal Substrings Within Budget](../1208-maximum-nesting-depth-of-two-valid-parentheses-strings/)
- [1297. Maximum Number of Occurrences of a Substring](../1297-maximum-number-of-balloons/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-ice-cream-bars/)
