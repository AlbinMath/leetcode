# LeetCode 1179: Reformat Department Table

**LeetCode Problem #1179 — Reformat Department Table**
Solve LeetCode Reformat Department Table using SQL and Database / SQL. This solution finds the optimal result using SQL Query / Relational Join & Window Function in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Reformat Department Table |
| LeetCode | #1179 |
| Difficulty | Easy |
| Language | SQL |
| Algorithm | SQL Query / Relational Join & Window Function |
| Data Structure | Relational Table |
| Pattern | Database / SQL |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Table: `Department`

+-------------+---------+
| Column Name | Type |
+-------------+---------+
| id | int |
| revenue | int |
| month | varchar |
+-------------+---------+
In SQL,(id, month) is the primary key of this table.
The table has information about the revenue of each department per month.
The month has values in ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"].

Reformat the table such that there is a department id column and a revenue column **for each month**.

Return the result table in **any order**.

The result format is in the following example.

## Examples
### Example 1
- **Input:** `Department table:
+------+---------+-------+
| id | revenue | month |
+------+---------+-------+
| 1 | 8000 | Jan |
| 2 | 9000 | Jan |
| 3 | 10000 | Feb |
| 1 | 7000 | Feb |
| 1 | 6000 | Mar |
+------+---------+-------+`
- **Output:** `+------+-------------+-------------+-------------+-----+-------------+
| id | Jan_Revenue | Feb_Revenue | Mar_Revenue | ... | Dec_Revenue |
+------+-------------+-------------+-------------+-----+-------------+
| 1 | 8000 | 7000 | 6000 | ... | null |
| 2 | 9000 | null | null | ... | null |
| 3 | null | 10000 | null | ... | null |
+------+-------------+-------------+-------------+-----+-------------+`
- **Explanation:** The revenue from Apr to Dec is null.
Note that the result table has 13 columns (1 for the department id + 12 for the months).

## Key Insight
Leverage **Database / SQL** with **Relational Table** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We solve **Reformat Department Table** by formulating an SQL query that applies relational algebra and SQL aggregation clauses. We group records using `GROUP BY` and compute metrics with aggregate functions.

## Algorithm
1. Group records and calculate aggregated summary metrics.
2. Project and return the requested output columns.

## Example Walkthrough
1. **Input State:** We begin with `Department table:
+------+---------+-------+
| id | revenue | month |
+------+---------+-------+
| 1 | 8000 | Jan |
| 2 | 9000 | Jan |
| 3 | 10000 | Feb |
| 1 | 7000 | Feb |
| 1 | 6000 | Mar |
+------+---------+-------+`.
2. **Processing Steps:** We apply **SQL Query / Relational Join & Window Function** using our **Relational Table**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `+------+-------------+-------------+-------------+-----+-------------+
| id | Jan_Revenue | Feb_Revenue | Mar_Revenue | ... | Dec_Revenue |
+------+-------------+-------------+-------------+-----+-------------+
| 1 | 8000 | 7000 | 6000 | ... | null |
| 2 | 9000 | null | null | ... | null |
| 3 | null | 10000 | null | ... | null |
+------+-------------+-------------+-------------+-----+-------------+`.
4. **Verification:** The revenue from Apr to Dec is null.
Note that the result table has 13 columns (1 for the department id + 12 for the months).

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
    id,
    MAX(CASE WHEN month = 'Jan' THEN revenue END) AS "Jan_Revenue",
    MAX(CASE WHEN month = 'Feb' THEN revenue END) AS "Feb_Revenue",
    MAX(CASE WHEN month = 'Mar' THEN revenue END) AS "Mar_Revenue",
    MAX(CASE WHEN month = 'Apr' THEN revenue END) AS "Apr_Revenue",
    MAX(CASE WHEN month = 'May' THEN revenue END) AS "May_Revenue",
    MAX(CASE WHEN month = 'Jun' THEN revenue END) AS "Jun_Revenue",
    MAX(CASE WHEN month = 'Jul' THEN revenue END) AS "Jul_Revenue",
    MAX(CASE WHEN month = 'Aug' THEN revenue END) AS "Aug_Revenue",
    MAX(CASE WHEN month = 'Sep' THEN revenue END) AS "Sep_Revenue",
    MAX(CASE WHEN month = 'Oct' THEN revenue END) AS "Oct_Revenue",
    MAX(CASE WHEN month = 'Nov' THEN revenue END) AS "Nov_Revenue",
    MAX(CASE WHEN month = 'Dec' THEN revenue END) AS "Dec_Revenue"
FROM Department
GROUP BY id;
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
- [1417. Reformat The String](../../1501-2000/1532-reformat-the-string/)
- [1507. Reformat Date](../../1001-1500/1283-reformat-date/)
- [1694. Reformat Phone Number](../../1501-2000/1812-reformat-phone-number/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/reformat-department-table/)
