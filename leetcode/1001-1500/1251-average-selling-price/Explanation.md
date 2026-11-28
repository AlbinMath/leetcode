# LeetCode 1251: Average Selling Price

**LeetCode Problem #1251 — Average Selling Price**
Solve LeetCode Average Selling Price using SQL and Database / SQL. This solution finds the optimal result using SQL Query / Relational Join & Window Function in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Average Selling Price |
| LeetCode | #1251 |
| Difficulty | Easy |
| Language | SQL |
| Algorithm | SQL Query / Relational Join & Window Function |
| Data Structure | Relational Table |
| Pattern | Database / SQL |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Table: `Prices`

+---------------+---------+
| Column Name | Type |
+---------------+---------+
| product_id | int |
| start_date | date |
| end_date | date |
| price | int |
+---------------+---------+
(product_id, start_date, end_date) is the primary key (combination of columns with unique values) for this table.
Each row of this table indicates the price of the product_id in the period from start_date to end_date.
For each product_id there will be no two overlapping periods. That means there will be no two intersecting periods for the same product_id.

Table: `UnitsSold`

+---------------+---------+
| Column Name | Type |
+---------------+---------+
| product_id | int |
| purchase_date | date |
| units | int |
+---------------+---------+
This table may contain duplicate rows.
Each row of this table indicates the date, units, and product_id of each product sold.

Write a solution to find the average selling price for each product. `average_price` should be **rounded to 2 decimal places**. If a product does not have any sold units, its average selling price is assumed to be 0.

Return the result table in **any order**.

The result format is in the following example.

## Examples
### Example 1
- **Input:** `Prices table:
+------------+------------+------------+--------+
| product_id | start_date | end_date | price |
+------------+------------+------------+--------+
| 1 | 2019-02-17 | 2019-02-28 | 5 |
| 1 | 2019-03-01 | 2019-03-22 | 20 |
| 2 | 2019-02-01 | 2019-02-20 | 15 |
| 2 | 2019-02-21 | 2019-03-31 | 30 |
+------------+------------+------------+--------+
UnitsSold table:
+------------+---------------+-------+
| product_id | purchase_date | units |
+------------+---------------+-------+
| 1 | 2019-02-25 | 100 |
| 1 | 2019-03-01 | 15 |
| 2 | 2019-02-10 | 200 |
| 2 | 2019-03-22 | 30 |
+------------+---------------+-------+`
- **Output:** `+------------+---------------+
| product_id | average_price |
+------------+---------------+
| 1 | 6.96 |
| 2 | 16.96 |
+------------+---------------+`
- **Explanation:** Average selling price = Total Price of Product / Number of products sold.
Average selling price for product 1 = ((100 * 5) + (15 * 20)) / 115 = 6.96
Average selling price for product 2 = ((200 * 15) + (30 * 30)) / 230 = 16.96

## Key Insight
Leverage **Database / SQL** with **Relational Table** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We solve **Average Selling Price** by formulating an SQL query that applies relational algebra and SQL aggregation clauses. We join the tables on matching foreign and primary keys. We group records using `GROUP BY` and compute metrics with aggregate functions.

## Algorithm
1. Join relevant tables on matching key columns.
2. Group records and calculate aggregated summary metrics.
3. Project and return the requested output columns.

## Example Walkthrough
1. **Input State:** We begin with `Prices table:
+------------+------------+------------+--------+
| product_id | start_date | end_date | price |
+------------+------------+------------+--------+
| 1 | 2019-02-17 | 2019-02-28 | 5 |
| 1 | 2019-03-01 | 2019-03-22 | 20 |
| 2 | 2019-02-01 | 2019-02-20 | 15 |
| 2 | 2019-02-21 | 2019-03-31 | 30 |
+------------+------------+------------+--------+
UnitsSold table:
+------------+---------------+-------+
| product_id | purchase_date | units |
+------------+---------------+-------+
| 1 | 2019-02-25 | 100 |
| 1 | 2019-03-01 | 15 |
| 2 | 2019-02-10 | 200 |
| 2 | 2019-03-22 | 30 |
+------------+---------------+-------+`.
2. **Processing Steps:** We apply **SQL Query / Relational Join & Window Function** using our **Relational Table**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `+------------+---------------+
| product_id | average_price |
+------------+---------------+
| 1 | 6.96 |
| 2 | 16.96 |
+------------+---------------+`.
4. **Verification:** Average selling price = Total Price of Product / Number of products sold.
Average selling price for product 1 = ((100 * 5) + (15 * 20)) / 115 = 6.96
Average selling price for product 2 = ((200 * 15) + (30 * 30)) / 230 = 16.96

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
    p.product_id,
    CAST(
        ROUND(
            COALESCE(SUM(p.price * u.units) * 1.0 / NULLIF(SUM(u.units), 0), 0),
            2
        ) AS DECIMAL(10, 2)
    ) AS average_price
FROM Prices p
LEFT JOIN UnitsSold u
    ON p.product_id = u.product_id
    AND u.purchase_date BETWEEN p.start_date AND p.end_date
GROUP BY p.product_id;
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
- [637. Average of Levels in Binary Tree](../../0501-1000/0637-average-of-levels-in-binary-tree/)
- [643. Maximum Average Subarray I](../../0501-1000/0643-maximum-average-subarray-i/)
- [805. Split Array With Same Average](../../0501-1000/0805-split-array-with-same-average/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/average-selling-price/)
