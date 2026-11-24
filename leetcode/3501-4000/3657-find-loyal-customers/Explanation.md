# LeetCode 3657: Find Loyal Customers

**LeetCode Problem #3657 — Find Loyal Customers**
Solve LeetCode Find Loyal Customers using SQL and Database / SQL. This solution finds the optimal result using SQL Query / Relational Join & Window Function in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Loyal Customers |
| LeetCode | #3657 |
| Difficulty | Medium |
| Language | SQL |
| Algorithm | SQL Query / Relational Join & Window Function |
| Data Structure | Relational Table |
| Pattern | Database / SQL |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Table: `customer_transactions`

+------------------+---------+
| Column Name | Type | 
+------------------+---------+
| transaction_id | int |
| customer_id | int |
| transaction_date | date |
| amount | decimal |
| transaction_type | varchar |
+------------------+---------+
transaction_id is the unique identifier for this table.
transaction_type can be either 'purchase' or 'refund'.

Write a solution to find **loyal customers**. A customer is considered **loyal** if they meet ALL the following criteria:

Made **at least** ` 3 ` purchase transactions. 
 Have been active for **at least** `30` days. 
 Their **refund rate** is less than `20%` .

*Refund rate* is the proportion of transactions that are refunds, calculated as the number of refund transactions divided by the total number of transactions (purchases plus refunds).

Return *the result table ordered by* `customer_id` *in **ascending** order*.

The result format is in the following example.

## Examples
Consider the standard input for **Find Loyal Customers**. Applying **SQL Query / Relational Join & Window Function** yields the target result step by step.

## Key Insight
Leverage **Database / SQL** with **Relational Table** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We solve **Find Loyal Customers** by formulating an SQL query that applies relational algebra and SQL aggregation clauses. We group records using `GROUP BY` and compute metrics with aggregate functions. Rows are filtered using `WHERE` / `HAVING` to satisfy the problem constraints. We order the final result set using `ORDER BY`.

## Algorithm
1. Group records and calculate aggregated summary metrics.
2. Filter records according to problem criteria.
3. Sort the projected result.
4. Project and return the requested output columns.

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
    customer_id
FROM customer_transactions
GROUP BY customer_id
HAVING
    -- At least 3 purchases
    SUM(
        CASE
            WHEN transaction_type = 'purchase' THEN 1
            ELSE 0
        END
    ) >= 3

    -- Active for at least 30 days
    AND DATEDIFF(
        day,
        MIN(transaction_date),
        MAX(transaction_date)
    ) >= 30

    -- Refund rate < 20%
    AND
    CAST(
        SUM(
            CASE
                WHEN transaction_type = 'refund' THEN 1
                ELSE 0
            END
        ) AS DECIMAL(10, 4)
    )
    / COUNT(*) < 0.20

ORDER BY
    customer_id ASC;
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
- [3705. Find Golden Hour Customers](../../3501-4000/3705-find-golden-hour-customers/)
- [3716. Find Churn Risk Customers](../../3501-4000/3716-find-churn-risk-customers/)
- [28. Find the Index of the First Occurrence in a String](../../0001-0500/0028-find-the-index-of-the-first-occurrence-in-a-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-loyal-customers/)
