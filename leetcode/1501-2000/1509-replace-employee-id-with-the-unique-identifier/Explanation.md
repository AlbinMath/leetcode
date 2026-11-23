# LeetCode 1378: Replace Employee ID With The Unique Identifier

**LeetCode Problem #1378 — Replace Employee ID With The Unique Identifier**
Solve LeetCode Replace Employee ID With The Unique Identifier using SQL and Database / SQL. This solution finds the optimal result using SQL Query / Relational Join & Window Function in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Replace Employee ID With The Unique Identifier |
| LeetCode | #1378 |
| Difficulty | Easy |
| Language | SQL |
| Algorithm | SQL Query / Relational Join & Window Function |
| Data Structure | Relational Table |
| Pattern | Database / SQL |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
+---------------+---------+

## Key Insight
Leverage **Database / SQL** with **Relational Table** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **SQL Query / Grouping**. By maintaining state efficiently in a **Relational Table**, we eliminate redundant operations.

## Algorithm
1. Initialize state variables / data structure (**Relational Table**).
2. Process elements sequentially using **SQL Query / Relational Join & Window Function**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Replace Employee ID With The Unique Identifier**. Applying **SQL Query / Relational Join & Window Function** yields the target result step by step.

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
SQL

## Source Code
- [solution.sql](./solution.sql)

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
- [648. Replace Words](../../0501-1000/0648-replace-words/)
- [833. Find And Replace in String](../../0501-1000/0862-find-and-replace-in-string/)
- [890. Find and Replace Pattern](../../0501-1000/0926-find-and-replace-pattern/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/)
