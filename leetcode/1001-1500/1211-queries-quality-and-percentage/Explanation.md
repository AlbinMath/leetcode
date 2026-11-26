# LeetCode 1211: Queries Quality and Percentage

**LeetCode Problem #1211 — Queries Quality and Percentage**
Solve LeetCode Queries Quality and Percentage using SQL and Database / SQL. This solution finds the optimal result using SQL Query / Relational Join & Window Function in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Queries Quality and Percentage |
| LeetCode | #1211 |
| Difficulty | Easy |
| Language | SQL |
| Algorithm | SQL Query / Relational Join & Window Function |
| Data Structure | Relational Table |
| Pattern | Database / SQL |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Table: `Queries`

+-------------+---------+
| Column Name | Type |
+-------------+---------+
| query_name | varchar |
| result | varchar |
| position | int |
| rating | int |
+-------------+---------+
This table may have duplicate rows.
This table contains information collected from some queries on a database.
The `position` column has a value from **1** to **500**.
The `rating` column has a value from **1** to **5**. Query with `rating` less than 3 is a poor query.

We define query `quality` as:

The average of the ratio between query rating and its position.

We also define `poor query percentage` as:

The percentage of all queries with rating less than 3.

Write a solution to find each `query_name`, the `quality` and `poor_query_percentage`.

Both `quality` and `poor_query_percentage` should be **rounded to 2 decimal places**.

Return the result table in **any order**.

The result format is in the following example.

## Examples
### Example 1
- **Input:** `Queries table:
+------------+-------------------+----------+--------+
| query_name | result | position | rating |
+------------+-------------------+----------+--------+
| Dog | Golden Retriever | 1 | 5 |
| Dog | German Shepherd | 2 | 5 |
| Dog | Mule | 200 | 1 |
| Cat | Shirazi | 5 | 2 |
| Cat | Siamese | 3 | 3 |
| Cat | Sphynx | 7 | 4 |
+------------+-------------------+----------+--------+`
- **Output:** `+------------+---------+-----------------------+
| query_name | quality | poor_query_percentage |
+------------+---------+-----------------------+
| Dog | 2.50 | 33.33 |
| Cat | 0.66 | 33.33 |
+------------+---------+-----------------------+`
- **Explanation:** Dog queries quality is ((5 / 1) + (5 / 2) + (1 / 200)) / 3 = 2.50
Dog queries poor_ query_percentage is (1 / 3) * 100 = 33.33

Cat queries quality equals ((2 / 5) + (3 / 3) + (4 / 7)) / 3 = 0.66
Cat queries poor_ query_percentage is (1 / 3) * 100 = 33.33

## Key Insight
Leverage **Database / SQL** with **Relational Table** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We solve **Queries Quality and Percentage** by formulating an SQL query that applies relational algebra and SQL aggregation clauses. We group records using `GROUP BY` and compute metrics with aggregate functions. Rows are filtered using `WHERE` / `HAVING` to satisfy the problem constraints.

## Algorithm
1. Group records and calculate aggregated summary metrics.
2. Filter records according to problem criteria.
3. Project and return the requested output columns.

## Example Walkthrough
1. **Input State:** We begin with `Queries table:
+------------+-------------------+----------+--------+
| query_name | result | position | rating |
+------------+-------------------+----------+--------+
| Dog | Golden Retriever | 1 | 5 |
| Dog | German Shepherd | 2 | 5 |
| Dog | Mule | 200 | 1 |
| Cat | Shirazi | 5 | 2 |
| Cat | Siamese | 3 | 3 |
| Cat | Sphynx | 7 | 4 |
+------------+-------------------+----------+--------+`.
2. **Processing Steps:** We apply **SQL Query / Relational Join & Window Function** using our **Relational Table**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `+------------+---------+-----------------------+
| query_name | quality | poor_query_percentage |
+------------+---------+-----------------------+
| Dog | 2.50 | 33.33 |
| Cat | 0.66 | 33.33 |
+------------+---------+-----------------------+`.
4. **Verification:** Dog queries quality is ((5 / 1) + (5 / 2) + (1 / 200)) / 3 = 2.50
Dog queries poor_ query_percentage is (1 / 3) * 100 = 33.33

Cat queries quality equals ((2 / 5) + (3 / 3) + (4 / 7)) / 3 = 0.66
Cat queries poor_ query_percentage is (1 / 3) * 100 = 33.33

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
    query_name,
    ROUND(AVG(CAST(rating AS FLOAT) / position), 2) AS quality,
    ROUND(
        100.0 * SUM(CASE WHEN rating < 3 THEN 1 ELSE 0 END) / COUNT(*),
        2
    ) AS poor_query_percentage
FROM Queries
WHERE query_name IS NOT NULL
GROUP BY query_name;
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
- [1633. Percentage of Users Attended a Contest](../../1501-2000/1633-percentage-of-users-attended-a-contest/)
- [1620. Coordinate With Maximum Network Quality](../../1501-2000/1620-coordinate-with-maximum-network-quality/)
- [2065. Maximum Path Quality of a Graph](../../2001-2500/2065-maximum-path-quality-of-a-graph/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/queries-quality-and-percentage/)
