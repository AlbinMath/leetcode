# LeetCode 1045: Customers Who Bought All Products

**LeetCode Problem #1045 — Customers Who Bought All Products**
Solve LeetCode Customers Who Bought All Products using SQL and Database / SQL. This solution finds the optimal result using SQL Query / Relational Join & Window Function in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Customers Who Bought All Products |
| LeetCode | #1045 |
| Difficulty | Medium |
| Language | SQL |
| Algorithm | SQL Query / Relational Join & Window Function |
| Data Structure | Relational Table |
| Pattern | Database / SQL |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Table: `Customer`

+-------------+---------+
| Column Name | Type |
+-------------+---------+
| customer_id | int |
| product_key | int |
+-------------+---------+
This table may contain duplicates rows. 
`customer_id` is not NULL`.`
product_key is a foreign key (reference column) to `Product` table.

Table: `Product`

+-------------+---------+
| Column Name | Type |
+-------------+---------+
| product_key | int |
+-------------+---------+
product_key is the primary key (column with unique values) for this table.

Write a solution to report the customer ids from the `Customer` table that bought all the products in the `Product` table.

Return the result table in **any order**.

The result format is in the following example.

## Examples
### Example 1
- **Input:** `Customer table:
+-------------+-------------+
| customer_id | product_key |
+-------------+-------------+
| 1 | 5 |
| 2 | 6 |
| 3 | 5 |
| 3 | 6 |
| 1 | 6 |
+-------------+-------------+
Product table:
+-------------+
| product_key |
+-------------+
| 5 |
| 6 |
+-------------+`
- **Output:** `+-------------+
| customer_id |
+-------------+
| 1 |
| 3 |
+-------------+`
- **Explanation:** The customers who bought all the products (5 and 6) are customers with IDs 1 and 3.

## Key Insight
Leverage **Database / SQL** with **Relational Table** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We solve **Customers Who Bought All Products** by formulating an SQL query that applies relational algebra and SQL aggregation clauses. We group records using `GROUP BY` and compute metrics with aggregate functions. Rows are filtered using `WHERE` / `HAVING` to satisfy the problem constraints.

## Algorithm
1. Group records and calculate aggregated summary metrics.
2. Filter records according to problem criteria.
3. Project and return the requested output columns.

## Example Walkthrough
1. **Input State:** We begin with `Customer table:
+-------------+-------------+
| customer_id | product_key |
+-------------+-------------+
| 1 | 5 |
| 2 | 6 |
| 3 | 5 |
| 3 | 6 |
| 1 | 6 |
+-------------+-------------+
Product table:
+-------------+
| product_key |
+-------------+
| 5 |
| 6 |
+-------------+`.
2. **Processing Steps:** We apply **SQL Query / Relational Join & Window Function** using our **Relational Table**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `+-------------+
| customer_id |
+-------------+
| 1 |
| 3 |
+-------------+`.
4. **Verification:** The customers who bought all the products (5 and 6) are customers with IDs 1 and 3.

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
SELECT customer_id
FROM Customer
GROUP BY customer_id
HAVING COUNT(DISTINCT product_key) = (
    SELECT COUNT(*) FROM Product
);
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
- [183. Customers Who Never Order](../../0001-0500/0183-customers-who-never-order/)
- [1327. List the Products Ordered in a Period](../../1001-1500/1462-list-the-products-ordered-in-a-period/)
- [1484. Group Sold Products By The Date](../../1501-2000/1625-group-sold-products-by-the-date/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/customers-who-bought-all-products/)
