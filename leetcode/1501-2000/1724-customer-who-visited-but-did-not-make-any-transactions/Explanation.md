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

## Problem Statement
Table: `Visits`

+-------------+---------+
| Column Name | Type |
+-------------+---------+
| visit_id | int |
| customer_id | int |
+-------------+---------+
visit_id is the column with unique values for this table.
This table contains information about the customers who visited the mall.

Table: `Transactions`

+----------------+---------+
| Column Name | Type |
+----------------+---------+
| transaction_id | int |
| visit_id | int |
| amount | int |
+----------------+---------+
transaction_id is column with unique values for this table.
This table contains information about the transactions made during the visit_id.

Write a solution to find the IDs of the users who visited without making any transactions and the number of times they made these types of visits.

Return the result table sorted in **any order**.

The result format is in the following example.

## Examples
### Example 1
- **Input:** `Visits
+----------+-------------+
| visit_id | customer_id |
+----------+-------------+
| 1 | 23 |
| 2 | 9 |
| 4 | 30 |
| 5 | 54 |
| 6 | 96 |
| 7 | 54 |
| 8 | 54 |
+----------+-------------+
Transactions
+----------------+----------+--------+
| transaction_id | visit_id | amount |
+----------------+----------+--------+
| 2 | 5 | 310 |
| 3 | 5 | 300 |
| 9 | 5 | 200 |
| 12 | 1 | 910 |
| 13 | 2 | 970 |
+----------------+----------+--------+`
- **Output:** `+-------------+----------------+
| customer_id | count_no_trans |
+-------------+----------------+
| 54 | 2 |
| 30 | 1 |
| 96 | 1 |
+-------------+----------------+`
- **Explanation:** Customer with id = 23 visited the mall once and made one transaction during the visit with id = 12.
Customer with id = 9 visited the mall once and made one transaction during the visit with id = 13.
Customer with id = 30 visited the mall once and did not make any transactions.
Customer with id = 54 visited the mall three times. During 2 visits they did not make any transactions, and during one visit they made 3 transactions.
Customer with id = 96 visited the mall once and did not make any transactions.
As we can see, users with IDs 30 and 96 visited the mall one time without making any transactions. Also, user 54 visited the mall twice and did not make any transactions.

## Key Insight
Leverage **Database / SQL** with **Relational Table** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We solve **Customer Who Visited but Did Not Make Any Transactions** by formulating an SQL query that applies relational algebra and SQL aggregation clauses. We join the tables on matching foreign and primary keys. We group records using `GROUP BY` and compute metrics with aggregate functions. Rows are filtered using `WHERE` / `HAVING` to satisfy the problem constraints.

## Algorithm
1. Join relevant tables on matching key columns.
2. Group records and calculate aggregated summary metrics.
3. Filter records according to problem criteria.
4. Project and return the requested output columns.

## Example Walkthrough
1. **Input State:** We begin with `Visits
+----------+-------------+
| visit_id | customer_id |
+----------+-------------+
| 1 | 23 |
| 2 | 9 |
| 4 | 30 |
| 5 | 54 |
| 6 | 96 |
| 7 | 54 |
| 8 | 54 |
+----------+-------------+
Transactions
+----------------+----------+--------+
| transaction_id | visit_id | amount |
+----------------+----------+--------+
| 2 | 5 | 310 |
| 3 | 5 | 300 |
| 9 | 5 | 200 |
| 12 | 1 | 910 |
| 13 | 2 | 970 |
+----------------+----------+--------+`.
2. **Processing Steps:** We apply **SQL Query / Relational Join & Window Function** using our **Relational Table**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `+-------------+----------------+
| customer_id | count_no_trans |
+-------------+----------------+
| 54 | 2 |
| 30 | 1 |
| 96 | 1 |
+-------------+----------------+`.
4. **Verification:** Customer with id = 23 visited the mall once and made one transaction during the visit with id = 12.
Customer with id = 9 visited the mall once and made one transaction during the visit with id = 13.
Customer with id = 30 visited the mall once and did not make any transactions.
Customer with id = 54 visited the mall three times. During 2 visits they did not make any transactions, and during one visit they made 3 transactions.
Customer with id = 96 visited the mall once and did not make any transactions.
As we can see, users with IDs 30 and 96 visited the mall one time without making any transactions. Also, user 54 visited the mall twice and did not make any transactions.

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
    v.customer_id,
    COUNT(*) AS count_no_trans
FROM Visits v
LEFT JOIN Transactions t
    ON v.visit_id = t.visit_id
WHERE t.transaction_id IS NULL
GROUP BY v.customer_id;
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
- [1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence](../../1501-2000/1566-check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/)
- [3591. Check if Any Element Has Prime Frequency](../../3501-4000/3914-check-if-any-element-has-prime-frequency/)
- [584. Find Customer Referee](../../0501-1000/0584-find-customer-referee/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/)
