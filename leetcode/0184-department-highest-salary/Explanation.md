# LeetCode 184: Department Highest Salary

**LeetCode Problem #184 — Department Highest Salary**
Solve LeetCode Department Highest Salary using SQL and Database / SQL. This solution finds the optimal result using SQL Query / Relational Join & Window Function in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Department Highest Salary |
| LeetCode | #184 |
| Difficulty | Medium |
| Language | SQL |
| Algorithm | SQL Query / Relational Join & Window Function |
| Data Structure | Relational Table |
| Pattern | Database / SQL |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
+--------------+---------+

## Key Insight
Leverage **Database / SQL** with **Relational Table** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **SQL Query / Grouping**. By maintaining state efficiently in a **Relational Table**, we eliminate redundant operations.

## Algorithm
1. Initialize state variables / data structure (**Relational Table**).
2. Process elements sequentially using **SQL Query / Relational Join & Window Function**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Department Highest Salary**. Applying **SQL Query / Relational Join & Window Function** yields the target result step by step.

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
- [176. Second Highest Salary](../0176-second-highest-salary/)
- [177. Nth Highest Salary](../0177-nth-highest-salary/)
- [185. Department Top Three Salaries](../0185-department-top-three-salaries/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/department-highest-salary/)
