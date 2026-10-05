# LeetCode 1724: Checking Existence of Edge Length Limited Paths II

**LeetCode Problem #1724 — Checking Existence of Edge Length Limited Paths II**
Solve LeetCode Checking Existence of Edge Length Limited Paths II using SQL and Database / SQL. This solution finds the optimal result using SQL Query / Relational Join & Grouping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Checking Existence of Edge Length Limited Paths II |
| LeetCode | #1724 |
| Difficulty | Hard |
| Language | SQL |
| Algorithm | SQL Query / Relational Join & Grouping |
| Data Structure | Relational Table |
| Pattern | Database / SQL |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
visit_id is the column with unique values for this table.

## Key Insight
Leverage **Database / SQL** with **Relational Table** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **SQL Query / Grouping**. By maintaining state efficiently in a **Relational Table**, we eliminate redundant operations.

## Algorithm
1. Initialize state variables / data structure (**Relational Table**).
2. Process elements sequentially using **SQL Query / Relational Join & Grouping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Checking Existence of Edge Length Limited Paths II**. Applying **SQL Query / Relational Join & Grouping** yields the target result step by step.

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
- [183. Customers Who Never Order](../0183-customers-who-never-order/)
- [584. Find Customer Referee](../0584-find-customer-referee/)
- [586. Customer Placing the Largest Number of Orders](../0586-customer-placing-the-largest-number-of-orders/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/)
