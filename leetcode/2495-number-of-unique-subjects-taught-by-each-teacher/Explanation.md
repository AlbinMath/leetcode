# LeetCode 2356: Number of Unique Subjects Taught by Each Teacher

**LeetCode Problem #2356 — Number of Unique Subjects Taught by Each Teacher**
Solve LeetCode Number of Unique Subjects Taught by Each Teacher using SQL and Database / SQL. This solution finds the optimal result using SQL Query / Relational Join & Window Function in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Unique Subjects Taught by Each Teacher |
| LeetCode | #2356 |
| Difficulty | Easy |
| Language | SQL |
| Algorithm | SQL Query / Relational Join & Window Function |
| Data Structure | Relational Table |
| Pattern | Database / SQL |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
(subject_id, dept_id) is the primary key (combinations of columns with unique values) of this table.

## Key Insight
Leverage **Database / SQL** with **Relational Table** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **SQL Query / Relational Join & Grouping**. By maintaining state efficiently in a **Relational Table**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Relational Table**).
2. Process elements sequentially using **SQL Query / Relational Join & Window Function**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Number of Unique Subjects Taught by Each Teacher**. Applying **SQL Query / Relational Join & Window Function** yields the target result step by step.

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
- [1207. Unique Number of Occurrences](../1319-unique-number-of-occurrences/)
- [1731. The Number of Employees Which Report to Each Employee](../1882-the-number-of-employees-which-report-to-each-employee/)
- [3513. Number of Unique XOR Triplets I](../3824-number-of-unique-xor-triplets-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-unique-subjects-taught-by-each-teacher/)
