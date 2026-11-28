# LeetCode 1327: List the Products Ordered in a Period

**LeetCode Problem #1327 — List the Products Ordered in a Period**
Solve LeetCode List the Products Ordered in a Period using SQL and Database / SQL. This solution finds the optimal result using SQL Query / Relational Join & Window Function in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | List the Products Ordered in a Period |
| LeetCode | #1327 |
| Difficulty | Easy |
| Language | SQL |
| Algorithm | SQL Query / Relational Join & Window Function |
| Data Structure | Relational Table |
| Pattern | Database / SQL |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Table: `Products`

+------------------+---------+
| Column Name | Type |
+------------------+---------+
| product_id | int |
| product_name | varchar |
| product_category | varchar |
+------------------+---------+
product_id is the primary key (column with unique values) for this table.
This table contains data about the company's products.

Table: `Orders`

+---------------+---------+
| Column Name | Type |
+---------------+---------+
| product_id | int |
| order_date | date |
| unit | int |
+---------------+---------+
This table may have duplicate rows.
product_id is a foreign key (reference column) to the Products table.
unit is the number of products ordered in order_date.

Write a solution to get the names of products that have at least `100` units ordered in **February 2020** and their amount.

Return the result table in **any order**.

The result format is in the following example.

## Examples
### Example 1
- **Input:** `Products table:
+-------------+-----------------------+------------------+
| product_id | product_name | product_category |
+-------------+-----------------------+------------------+
| 1 | Leetcode Solutions | Book |
| 2 | Jewels of Stringology | Book |
| 3 | HP | Laptop |
| 4 | Lenovo | Laptop |
| 5 | Leetcode Kit | T-shirt |
+-------------+-----------------------+------------------+
Orders table:
+--------------+--------------+----------+
| product_id | order_date | unit |
+--------------+--------------+----------+
| 1 | 2020-02-05 | 60 |
| 1 | 2020-02-10 | 70 |
| 2 | 2020-01-18 | 30 |
| 2 | 2020-02-11 | 80 |
| 3 | 2020-02-17 | 2 |
| 3 | 2020-02-24 | 3 |
| 4 | 2020-03-01 | 20 |
| 4 | 2020-03-04 | 30 |
| 4 | 2020-03-04 | 60 |
| 5 | 2020-02-25 | 50 |
| 5 | 2020-02-27 | 50 |
| 5 | 2020-03-01 | 50 |
+--------------+--------------+----------+`
- **Output:** `+--------------------+---------+
| product_name | unit |
+--------------------+---------+
| Leetcode Solutions | 130 |
| Leetcode Kit | 100 |
+--------------------+---------+`
- **Explanation:** Products with product_id = 1 is ordered in February a total of (60 + 70) = 130.
Products with product_id = 2 is ordered in February a total of 80.
Products with product_id = 3 is ordered in February a total of (2 + 3) = 5.
Products with product_id = 4 was not ordered in February 2020.
Products with product_id = 5 is ordered in February a total of (50 + 50) = 100.

## Key Insight
Leverage **Database / SQL** with **Relational Table** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We solve **List the Products Ordered in a Period** by formulating an SQL query that applies relational algebra and SQL aggregation clauses. We join the tables on matching foreign and primary keys. We group records using `GROUP BY` and compute metrics with aggregate functions. Rows are filtered using `WHERE` / `HAVING` to satisfy the problem constraints.

## Algorithm
1. Join relevant tables on matching key columns.
2. Group records and calculate aggregated summary metrics.
3. Filter records according to problem criteria.
4. Project and return the requested output columns.

## Example Walkthrough
1. **Input State:** We begin with `Products table:
+-------------+-----------------------+------------------+
| product_id | product_name | product_category |
+-------------+-----------------------+------------------+
| 1 | Leetcode Solutions | Book |
| 2 | Jewels of Stringology | Book |
| 3 | HP | Laptop |
| 4 | Lenovo | Laptop |
| 5 | Leetcode Kit | T-shirt |
+-------------+-----------------------+------------------+
Orders table:
+--------------+--------------+----------+
| product_id | order_date | unit |
+--------------+--------------+----------+
| 1 | 2020-02-05 | 60 |
| 1 | 2020-02-10 | 70 |
| 2 | 2020-01-18 | 30 |
| 2 | 2020-02-11 | 80 |
| 3 | 2020-02-17 | 2 |
| 3 | 2020-02-24 | 3 |
| 4 | 2020-03-01 | 20 |
| 4 | 2020-03-04 | 30 |
| 4 | 2020-03-04 | 60 |
| 5 | 2020-02-25 | 50 |
| 5 | 2020-02-27 | 50 |
| 5 | 2020-03-01 | 50 |
+--------------+--------------+----------+`.
2. **Processing Steps:** We apply **SQL Query / Relational Join & Window Function** using our **Relational Table**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `+--------------------+---------+
| product_name | unit |
+--------------------+---------+
| Leetcode Solutions | 130 |
| Leetcode Kit | 100 |
+--------------------+---------+`.
4. **Verification:** Products with product_id = 1 is ordered in February a total of (60 + 70) = 130.
Products with product_id = 2 is ordered in February a total of 80.
Products with product_id = 3 is ordered in February a total of (2 + 3) = 5.
Products with product_id = 4 was not ordered in February 2020.
Products with product_id = 5 is ordered in February a total of (50 + 50) = 100.

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
    p.product_name,
    SUM(o.unit) AS unit
FROM Products p
JOIN Orders o
    ON p.product_id = o.product_id
WHERE o.order_date >= '2020-02-01'
  AND o.order_date < '2020-03-01'
GROUP BY
    p.product_id,
    p.product_name
HAVING SUM(o.unit) >= 100;
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
- [1604. Alert Using Same Key-Card Three or More Times in a One Hour Period](../../1501-2000/1604-alert-using-same-key-card-three-or-more-times-in-a-one-hour-period/)
- [19. Remove Nth Node From End of List](../../0001-0500/0019-remove-nth-node-from-end-of-list/)
- [61. Rotate List](../../0001-0500/0061-rotate-list/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/list-the-products-ordered-in-a-period/)
