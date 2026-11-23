# LeetCode 3465: Find Products with Valid Serial Numbers

**LeetCode Problem #3465 — Find Products with Valid Serial Numbers**
Solve LeetCode Find Products with Valid Serial Numbers using SQL and Database / SQL. This solution finds the optimal result using SQL Query / Relational Join & Window Function in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Products with Valid Serial Numbers |
| LeetCode | #3465 |
| Difficulty | Easy |
| Language | SQL |
| Algorithm | SQL Query / Relational Join & Window Function |
| Data Structure | Relational Table |
| Pattern | Database / SQL |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Table: `products`

+--------------+------------+
| Column Name | Type |
+--------------+------------+
| product_id | int |
| product_name | varchar |
| description | varchar |
+--------------+------------+
(product_id) is the unique key for this table.
Each row in the table represents a product with its unique ID, name, and description.

Write a solution to find all products whose description **contains a valid serial number** pattern. A valid serial number follows these rules:

It starts with the letters **SN** (case-sensitive). 
 Followed by exactly `4` digits. 
 It must have a hyphen (-) **followed by exactly** `4` digits. 
 The serial number must be within the description (it may not necessarily start at the beginning).

Return *the result table ordered by* `product_id` *in **ascending** order*.

The result format is in the following example.

## Examples
Consider the standard input for **Find Products with Valid Serial Numbers**. Applying **SQL Query / Relational Join & Window Function** yields the target result step by step.

## Key Insight
Leverage **Database / SQL** with **Relational Table** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We solve **Find Products with Valid Serial Numbers** by formulating an SQL query that applies relational algebra and SQL aggregation clauses. Rows are filtered using `WHERE` / `HAVING` to satisfy the problem constraints. We order the final result set using `ORDER BY`.

## Algorithm
1. Filter records according to problem criteria.
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
    product_id,
    product_name,
    description
FROM products
WHERE REGEXP_LIKE(
    description,
    '(^|[^A-Za-z0-9])SN[0-9]{4}-[0-9]{4}([^A-Za-z0-9]|$)',
    'c'
)
ORDER BY product_id ASC;
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
- [448. Find All Numbers Disappeared in an Array](../../0001-0500/0448-find-all-numbers-disappeared-in-an-array/)
- [1295. Find Numbers with Even Number of Digits](../../1001-1500/1421-find-numbers-with-even-number-of-digits/)
- [1517. Find Users With Valid E-Mails](../../1501-2000/1664-find-users-with-valid-e-mails/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-products-with-valid-serial-numbers/)
