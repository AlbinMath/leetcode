# LeetCode 2495: Number of Subarrays Having Even Product

**LeetCode Problem #2495 — Number of Subarrays Having Even Product**
Solve LeetCode Number of Subarrays Having Even Product using SQL and Database / SQL. This solution finds the optimal result using SQL Query / Relational Join & Grouping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Subarrays Having Even Product |
| LeetCode | #2495 |
| Difficulty | Medium |
| Language | SQL |
| Algorithm | SQL Query / Relational Join & Grouping |
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
2. Process elements sequentially using **SQL Query / Relational Join & Grouping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Number of Subarrays Having Even Product**. Applying **SQL Query / Relational Join & Grouping** yields the target result step by step.

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
- [1882. Process Tasks Using Servers](../1882-the-number-of-employees-which-report-to-each-employee/)
- [3820. Pythagorean Distance Nodes in a Tree](../3820-number-of-unique-xor-triplets-ii/)
- [3824. Minimum K to Reduce Array Within Limit](../3824-number-of-unique-xor-triplets-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-unique-subjects-taught-by-each-teacher/)
