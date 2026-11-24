# LeetCode 1204: Last Person to Fit in the Bus

**LeetCode Problem #1204 — Last Person to Fit in the Bus**
Solve LeetCode Last Person to Fit in the Bus using SQL and Database / SQL. This solution finds the optimal result using SQL Query / Relational Join & Window Function in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Last Person to Fit in the Bus |
| LeetCode | #1204 |
| Difficulty | Medium |
| Language | SQL |
| Algorithm | SQL Query / Relational Join & Window Function |
| Data Structure | Relational Table |
| Pattern | Database / SQL |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Table: `Queue`

+-------------+---------+
| Column Name | Type |
+-------------+---------+
| person_id | int |
| person_name | varchar |
| weight | int |
| turn | int |
+-------------+---------+
person_id column contains unique values.
This table has the information about all people waiting for a bus.
The person_id and turn columns will contain all numbers from 1 to n, where n is the number of rows in the table.
turn determines the order of which the people will board the bus, where turn=1 denotes the first person to board and turn=n denotes the last person to board.
weight is the weight of the person in kilograms.

There is a queue of people waiting to board a bus. However, the bus has a weight limit of `1000`** kilograms**, so there may be some people who cannot board.

Write a solution to find the `person_name` of the **last person** that can fit on the bus without exceeding the weight limit. The test cases are generated such that the first person does not exceed the weight limit.

**Note** that *only one* person can board the bus at any given turn.

The result format is in the following example.

## Examples
### Example 1
- **Input:** `Queue table:
+-----------+-------------+--------+------+
| person_id | person_name | weight | turn |
+-----------+-------------+--------+------+
| 5 | Alice | 250 | 1 |
| 4 | Bob | 175 | 5 |
| 3 | Alex | 350 | 2 |
| 6 | John Cena | 400 | 3 |
| 1 | Winston | 500 | 6 |
| 2 | Marie | 200 | 4 |
+-----------+-------------+--------+------+`
- **Output:** `+-------------+
| person_name |
+-------------+
| John Cena |
+-------------+`
- **Explanation:** The folowing table is ordered by the turn for simplicity.
+------+----+-----------+--------+--------------+
| Turn | ID | Name | Weight | Total Weight |
+------+----+-----------+--------+--------------+
| 1 | 5 | Alice | 250 | 250 |
| 2 | 3 | Alex | 350 | 600 |
| 3 | 6 | John Cena | 400 | 1000 | (last person to board)
| 4 | 2 | Marie | 200 | 1200 | (cannot board)
| 5 | 4 | Bob | 175 | ___ |
| 6 | 1 | Winston | 500 | ___ |
+------+----+-----------+--------+--------------+

## Key Insight
Leverage **Database / SQL** with **Relational Table** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We solve **Last Person to Fit in the Bus** by formulating an SQL query that applies relational algebra and SQL aggregation clauses. Rows are filtered using `WHERE` / `HAVING` to satisfy the problem constraints. We order the final result set using `ORDER BY`.

## Algorithm
1. Filter records according to problem criteria.
2. Sort the projected result.
3. Project and return the requested output columns.

## Example Walkthrough
1. **Input State:** We begin with `Queue table:
+-----------+-------------+--------+------+
| person_id | person_name | weight | turn |
+-----------+-------------+--------+------+
| 5 | Alice | 250 | 1 |
| 4 | Bob | 175 | 5 |
| 3 | Alex | 350 | 2 |
| 6 | John Cena | 400 | 3 |
| 1 | Winston | 500 | 6 |
| 2 | Marie | 200 | 4 |
+-----------+-------------+--------+------+`.
2. **Processing Steps:** We apply **SQL Query / Relational Join & Window Function** using our **Relational Table**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `+-------------+
| person_name |
+-------------+
| John Cena |
+-------------+`.
4. **Verification:** The folowing table is ordered by the turn for simplicity.
+------+----+-----------+--------+--------------+
| Turn | ID | Name | Weight | Total Weight |
+------+----+-----------+--------+--------------+
| 1 | 5 | Alice | 250 | 250 |
| 2 | 3 | Alex | 350 | 600 |
| 3 | 6 | John Cena | 400 | 1000 | (last person to board)
| 4 | 2 | Marie | 200 | 1200 | (cannot board)
| 5 | 4 | Bob | 175 | ___ |
| 6 | 1 | Winston | 500 | ___ |
+------+----+-----------+--------+--------------+

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
SELECT person_name
FROM (
    SELECT
        person_name,
        total_weight,
        ROW_NUMBER() OVER (ORDER BY total_weight DESC) AS rn
    FROM (
        SELECT
            person_name,
            SUM(weight) OVER (ORDER BY turn) AS total_weight
        FROM Queue
    )
    WHERE total_weight <= 1000
)
WHERE rn = 1;
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
- [607. Sales Person](../../0501-1000/0607-sales-person/)
- [815. Bus Routes](../../0501-1000/0815-bus-routes/)
- [34. Find First and Last Position of Element in Sorted Array](../../0001-0500/0034-find-first-and-last-position-of-element-in-sorted-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/last-person-to-fit-in-the-bus/)
