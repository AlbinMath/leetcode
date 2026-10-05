# LeetCode 1327: List the Products Ordered in a Period

**LeetCode Problem #1327 — List the Products Ordered in a Period**
Solve LeetCode List the Products Ordered in a Period using SQL and Database / SQL. This solution finds the optimal result using SQL Query / Relational Join & Grouping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | List the Products Ordered in a Period |
| LeetCode | #1327 |
| Difficulty | Easy |
| Language | SQL |
| Algorithm | SQL Query / Relational Join & Grouping |
| Data Structure | Relational Table |
| Pattern | Database / SQL |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
person_id column contains unique values.

## Key Insight
Leverage **Database / SQL** with **Relational Table** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **SQL Query / Grouping**. By maintaining state efficiently in a **Relational Table**, we eliminate redundant operations.

## Algorithm
1. Initialize state variables / data structure (**Relational Table**).
2. Process elements sequentially using **SQL Query / Relational Join & Grouping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **List the Products Ordered in a Period**. Applying **SQL Query / Relational Join & Grouping** yields the target result step by step.

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
- [607. Sales Person](../0607-sales-person/)
- [2734. Lexicographically Smallest String After Substring Operation](../2734-array-prototype-last/)
- [2855. Minimum Right Shifts to Sort the Array](../2855-maximum-number-of-jumps-to-reach-the-last-index/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/last-person-to-fit-in-the-bus/)
