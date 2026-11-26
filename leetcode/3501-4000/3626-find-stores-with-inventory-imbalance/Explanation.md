# LeetCode 3626: Find Stores with Inventory Imbalance

**LeetCode Problem #3626 — Find Stores with Inventory Imbalance**
Solve LeetCode Find Stores with Inventory Imbalance using SQL and Database / SQL. This solution finds the optimal result using SQL Query / Relational Join & Window Function in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Stores with Inventory Imbalance |
| LeetCode | #3626 |
| Difficulty | Medium |
| Language | SQL |
| Algorithm | SQL Query / Relational Join & Window Function |
| Data Structure | Relational Table |
| Pattern | Database / SQL |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Table: `stores`

+-------------+---------+
| Column Name | Type |
+-------------+---------+
| store_id | int |
| store_name | varchar |
| location | varchar |
+-------------+---------+
store_id is the unique identifier for this table.
Each row contains information about a store and its location.

Table: `inventory`

+-------------+---------+
| Column Name | Type |
+-------------+---------+
| inventory_id| int |
| store_id | int |
| product_name| varchar |
| quantity | int |
| price | decimal |
+-------------+---------+
inventory_id is the unique identifier for this table.
Each row represents the inventory of a specific product at a specific store.

Write a solution to find stores that have **inventory imbalance** - stores where the most expensive product has lower stock than the cheapest product.

For each store, identify the **most expensive product** (highest price) and its quantity 
 For each store, identify the **cheapest product** (lowest price) and its quantity 
 A store has inventory imbalance if the most expensive product's quantity is **less than** the cheapest product's quantity 
 Calculate the **imbalance ratio** as (cheapest_quantity / most_expensive_quantity) 
 **Round** the imbalance ratio to **2** decimal places 
 Only include stores that have **at least **`3`** different products**

Return *the result table ordered by imbalance ratio in **descending** order, then by store name in **ascending** order*.

The result format is in the following example.

## Examples
Consider the standard input for **Find Stores with Inventory Imbalance**. Applying **SQL Query / Relational Join & Window Function** yields the target result step by step.

## Key Insight
Leverage **Database / SQL** with **Relational Table** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We solve **Find Stores with Inventory Imbalance** by formulating an SQL query that applies relational algebra and SQL aggregation clauses. We join the tables on matching foreign and primary keys. We group records using `GROUP BY` and compute metrics with aggregate functions. Rows are filtered using `WHERE` / `HAVING` to satisfy the problem constraints. We order the final result set using `ORDER BY`.

## Algorithm
1. Join relevant tables on matching key columns.
2. Group records and calculate aggregated summary metrics.
3. Filter records according to problem criteria.
4. Sort the projected result.
5. Project and return the requested output columns.

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
WITH ranked_inventory AS (
    SELECT
        i.*,
        COUNT(*) OVER (
            PARTITION BY i.store_id
        ) AS product_count,

        ROW_NUMBER() OVER (
            PARTITION BY i.store_id
            ORDER BY i.price DESC, i.inventory_id
        ) AS expensive_rank,

        ROW_NUMBER() OVER (
            PARTITION BY i.store_id
            ORDER BY i.price ASC, i.inventory_id
        ) AS cheap_rank
    FROM inventory i
),

store_data AS (
    SELECT
        store_id,

        MAX(CASE
            WHEN expensive_rank = 1
            THEN product_name
        END) AS most_exp_product,

        MAX(CASE
            WHEN expensive_rank = 1
            THEN quantity
        END) AS expensive_quantity,

        MAX(CASE
            WHEN cheap_rank = 1
            THEN product_name
        END) AS cheapest_product,

        MAX(CASE
            WHEN cheap_rank = 1
            THEN quantity
        END) AS cheapest_quantity,

        MAX(product_count) AS product_count
    FROM ranked_inventory
    GROUP BY store_id
)

SELECT
    s.store_id,
    s.store_name,
    s.location,
    sd.most_exp_product,
    sd.cheapest_product,
    ROUND(
        CAST(sd.cheapest_quantity AS DECIMAL(10, 2))
        / sd.expensive_quantity,
        2
    ) AS imbalance_ratio
FROM store_data sd
JOIN stores s
    ON s.store_id = sd.store_id
WHERE sd.product_count >= 3
  AND sd.expensive_quantity < sd.cheapest_quantity
ORDER BY
    imbalance_ratio DESC,
    s.store_name ASC;
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
- [3679.  Minimum Discards to Balance Inventory](../../3501-4000/3679-minimum-discards-to-balance-inventory/)
- [2763. Sum of Imbalance Numbers of All Subarrays](../../2501-3000/2763-sum-of-imbalance-numbers-of-all-subarrays/)
- [28. Find the Index of the First Occurrence in a String](../../0001-0500/0028-find-the-index-of-the-first-occurrence-in-a-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-stores-with-inventory-imbalance/)
