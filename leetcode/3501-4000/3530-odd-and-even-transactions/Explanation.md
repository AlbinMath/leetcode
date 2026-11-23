# LeetCode 3220: Odd and Even Transactions

**LeetCode Problem #3220 — Odd and Even Transactions**
Solve LeetCode Odd and Even Transactions using SQL and Database / SQL. This solution finds the optimal result using SQL Query / Relational Join & Window Function in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Odd and Even Transactions |
| LeetCode | #3220 |
| Difficulty | Medium |
| Language | SQL |
| Algorithm | SQL Query / Relational Join & Window Function |
| Data Structure | Relational Table |
| Pattern | Database / SQL |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Table: `transactions`

+------------------+------+
| Column Name | Type | 
+------------------+------+
| transaction_id | int |
| amount | int |
| transaction_date | date |
+------------------+------+
The transactions_id column uniquely identifies each row in this table.
Each row of this table contains the transaction id, amount and transaction date.

Write a solution to find the **sum of amounts** for **odd** and **even** transactions for each day. If there are no odd or even transactions for a specific date, display as `0`.

Return *the result table ordered by* `transaction_date` *in **ascending** order*.

The result format is in the following example.

## Examples
Consider the standard input for **Odd and Even Transactions**. Applying **SQL Query / Relational Join & Window Function** yields the target result step by step.

## Key Insight
Leverage **Database / SQL** with **Relational Table** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We solve **Odd and Even Transactions** by formulating an SQL query that applies relational algebra and SQL aggregation clauses. We group records using `GROUP BY` and compute metrics with aggregate functions. We order the final result set using `ORDER BY`.

## Algorithm
1. Group records and calculate aggregated summary metrics.
2. Sort the projected result.
3. Project and return the requested output columns.

## Example Walkthrough
Applying **SQL Query / Relational Join & Window Function** step by step to the input yields the expected result.

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
SELECT
    transaction_date,
    SUM(CASE
        WHEN amount % 2 = 1 THEN amount
        ELSE 0
    END) AS odd_sum,
    SUM(CASE
        WHEN amount % 2 = 0 THEN amount
        ELSE 0
    END) AS even_sum
FROM transactions
GROUP BY transaction_date
ORDER BY transaction_date ASC;
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
- [328. Odd Even Linked List](../../0001-0500/0328-odd-even-linked-list/)
- [975. Odd Even Jump](../../1001-1500/1017-odd-even-jump/)
- [1116. Print Zero Even Odd](../../1001-1500/1216-print-zero-even-odd/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/odd-and-even-transactions/)
