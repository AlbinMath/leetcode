# LeetCode 1193: Monthly Transactions I

**LeetCode Problem #1193 — Monthly Transactions I**
Solve LeetCode Monthly Transactions I using SQL and Database / SQL. This solution finds the optimal result using SQL Query / Relational Join & Window Function in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Monthly Transactions I |
| LeetCode | #1193 |
| Difficulty | Medium |
| Language | SQL |
| Algorithm | SQL Query / Relational Join & Window Function |
| Data Structure | Relational Table |
| Pattern | Database / SQL |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Table: `Transactions`

+---------------+---------+
| Column Name | Type |
+---------------+---------+
| id | int |
| country | varchar |
| state | enum |
| amount | int |
| trans_date | date |
+---------------+---------+
id is the primary key of this table.
The table has information about incoming transactions.
The state column is an enum of type ["approved", "declined"].

Write an SQL query to find for each month and country, the number of transactions and their total amount, the number of approved transactions and their total amount.

Return the result table in **any order**.

The query result format is in the following example.

## Examples
### Example 1
- **Input:** `Transactions table:
+------+---------+----------+--------+------------+
| id | country | state | amount | trans_date |
+------+---------+----------+--------+------------+
| 121 | US | approved | 1000 | 2018-12-18 |
| 122 | US | declined | 2000 | 2018-12-19 |
| 123 | US | approved | 2000 | 2019-01-01 |
| 124 | DE | approved | 2000 | 2019-01-07 |
+------+---------+----------+--------+------------+`
- **Output:** `+----------+---------+-------------+----------------+--------------------+-----------------------+
| month | country | trans_count | approved_count | trans_total_amount | approved_total_amount |
+----------+---------+-------------+----------------+--------------------+-----------------------+
| 2018-12 | US | 2 | 1 | 3000 | 1000 |
| 2019-01 | US | 1 | 1 | 2000 | 2000 |
| 2019-01 | DE | 1 | 1 | 2000 | 2000 |
+----------+---------+-------------+----------------+--------------------+-----------------------+`

## Key Insight
Leverage **Database / SQL** with **Relational Table** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We solve **Monthly Transactions I** by formulating an SQL query that applies relational algebra and SQL aggregation clauses. We group records using `GROUP BY` and compute metrics with aggregate functions.

## Algorithm
1. Group records and calculate aggregated summary metrics.
2. Project and return the requested output columns.

## Example Walkthrough
1. **Input State:** We begin with `Transactions table:
+------+---------+----------+--------+------------+
| id | country | state | amount | trans_date |
+------+---------+----------+--------+------------+
| 121 | US | approved | 1000 | 2018-12-18 |
| 122 | US | declined | 2000 | 2018-12-19 |
| 123 | US | approved | 2000 | 2019-01-01 |
| 124 | DE | approved | 2000 | 2019-01-07 |
+------+---------+----------+--------+------------+`.
2. **Processing Steps:** We apply **SQL Query / Relational Join & Window Function** using our **Relational Table**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `+----------+---------+-------------+----------------+--------------------+-----------------------+
| month | country | trans_count | approved_count | trans_total_amount | approved_total_amount |
+----------+---------+-------------+----------------+--------------------+-----------------------+
| 2018-12 | US | 2 | 1 | 3000 | 1000 |
| 2019-01 | US | 1 | 1 | 2000 | 2000 |
| 2019-01 | DE | 1 | 1 | 2000 | 2000 |
+----------+---------+-------------+----------------+--------------------+-----------------------+`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Relational Table.

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


```sql
SELECT DATE_FORMAT(trans_date, '%Y-%m') AS month,
       country,
       COUNT(*) AS trans_count,
       SUM(state = 'approved') AS approved_count,
       SUM(amount) AS trans_total_amount,
       SUM(IF(state = 'approved', amount, 0)) AS approved_total_amount
FROM Transactions
GROUP BY month, country;
```

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
- [1169. Invalid Transactions](../../1001-1500/1272-invalid-transactions/)
- [1581. Customer Who Visited but Did Not Make Any Transactions](../../1501-2000/1724-customer-who-visited-but-did-not-make-any-transactions/)
- [3220. Odd and Even Transactions](../../3501-4000/3530-odd-and-even-transactions/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/monthly-transactions-i/)
