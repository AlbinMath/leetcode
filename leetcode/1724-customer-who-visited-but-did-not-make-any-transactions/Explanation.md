# LeetCode 1581: Customer Who Visited but Did Not Make Any Transactions

**LeetCode Problem #1581 — Customer Who Visited but Did Not Make Any Transactions**
Solve LeetCode Customer Who Visited but Did Not Make Any Transactions using SQL and Database / SQL. This solution finds the optimal result using SQL Query / Relational Join & Window Function in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Customer Who Visited but Did Not Make Any Transactions |
| LeetCode | #1581 |
| Difficulty | Easy |
| Language | SQL |
| Algorithm | SQL Query / Relational Join & Window Function |
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
2. Process elements sequentially using **SQL Query / Relational Join & Window Function**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Customer Who Visited but Did Not Make Any Transactions**. Applying **SQL Query / Relational Join & Window Function** yields the target result step by step.

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
- [1560. Most Visited Sector in  a Circular Track](../1682-most-visited-sector-in--a-circular-track/)
- [2617. Minimum Number of Visited Cells in a Grid](../2697-minimum-number-of-visited-cells-in-a-grid/)
- [2876. Count Visited Nodes in a Directed Graph](../3140-count-visited-nodes-in-a-directed-graph/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/)
