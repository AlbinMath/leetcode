# LeetCode 1633: Percentage of Users Attended a Contest

**LeetCode Problem #1633 — Percentage of Users Attended a Contest**
Solve LeetCode Percentage of Users Attended a Contest using SQL and Database / SQL. This solution finds the optimal result using SQL Query / Relational Join & Window Function in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Percentage of Users Attended a Contest |
| LeetCode | #1633 |
| Difficulty | Easy |
| Language | SQL |
| Algorithm | SQL Query / Relational Join & Window Function |
| Data Structure | Relational Table |
| Pattern | Database / SQL |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Table: `Users`

+-------------+---------+
| Column Name | Type |
+-------------+---------+
| user_id | int |
| user_name | varchar |
+-------------+---------+
user_id is the primary key (column with unique values) for this table.
Each row of this table contains the name and the id of a user.

Table: `Register`

+-------------+---------+
| Column Name | Type |
+-------------+---------+
| contest_id | int |
| user_id | int |
+-------------+---------+
(contest_id, user_id) is the primary key (combination of columns with unique values) for this table.
Each row of this table contains the id of a user and the contest they registered into.

Write a solution to find the percentage of the users registered in each contest rounded to **two decimals**.

Return the result table ordered by `percentage` in **descending order**. In case of a tie, order it by `contest_id` in **ascending order**.

The result format is in the following example.

## Examples
### Example 1
- **Input:** `Users table:
+---------+-----------+
| user_id | user_name |
+---------+-----------+
| 6 | Alice |
| 2 | Bob |
| 7 | Alex |
+---------+-----------+
Register table:
+------------+---------+
| contest_id | user_id |
+------------+---------+
| 215 | 6 |
| 209 | 2 |
| 208 | 2 |
| 210 | 6 |
| 208 | 6 |
| 209 | 7 |
| 209 | 6 |
| 215 | 7 |
| 208 | 7 |
| 210 | 2 |
| 207 | 2 |
| 210 | 7 |
+------------+---------+`
- **Output:** `+------------+------------+
| contest_id | percentage |
+------------+------------+
| 208 | 100.0 |
| 209 | 100.0 |
| 210 | 100.0 |
| 215 | 66.67 |
| 207 | 33.33 |
+------------+------------+`
- **Explanation:** All the users registered in contests 208, 209, and 210. The percentage is 100% and we sort them in the answer table by contest_id in ascending order.
Alice and Alex registered in contest 215 and the percentage is ((2/3) * 100) = 66.67%
Bob registered in contest 207 and the percentage is ((1/3) * 100) = 33.33%

## Key Insight
Leverage **Database / SQL** with **Relational Table** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We solve **Percentage of Users Attended a Contest** by formulating an SQL query that applies relational algebra and SQL aggregation clauses. We group records using `GROUP BY` and compute metrics with aggregate functions. We order the final result set using `ORDER BY`.

## Algorithm
1. Group records and calculate aggregated summary metrics.
2. Sort the projected result.
3. Project and return the requested output columns.

## Example Walkthrough
1. **Input State:** We begin with `Users table:
+---------+-----------+
| user_id | user_name |
+---------+-----------+
| 6 | Alice |
| 2 | Bob |
| 7 | Alex |
+---------+-----------+
Register table:
+------------+---------+
| contest_id | user_id |
+------------+---------+
| 215 | 6 |
| 209 | 2 |
| 208 | 2 |
| 210 | 6 |
| 208 | 6 |
| 209 | 7 |
| 209 | 6 |
| 215 | 7 |
| 208 | 7 |
| 210 | 2 |
| 207 | 2 |
| 210 | 7 |
+------------+---------+`.
2. **Processing Steps:** We apply **SQL Query / Relational Join & Window Function** using our **Relational Table**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `+------------+------------+
| contest_id | percentage |
+------------+------------+
| 208 | 100.0 |
| 209 | 100.0 |
| 210 | 100.0 |
| 215 | 66.67 |
| 207 | 33.33 |
+------------+------------+`.
4. **Verification:** All the users registered in contests 208, 209, and 210. The percentage is 100% and we sort them in the answer table by contest_id in ascending order.
Alice and Alex registered in contest 215 and the percentage is ((2/3) * 100) = 66.67%
Bob registered in contest 207 and the percentage is ((1/3) * 100) = 33.33%

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
    contest_id,
    ROUND(
        COUNT(*) * 100.0 / (SELECT COUNT(*) FROM Users),
        2
    ) AS percentage
FROM Register
GROUP BY contest_id
ORDER BY
    percentage DESC,
    contest_id ASC;
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
- [262. Trips and Users](../../0001-0500/0262-trips-and-users/)
- [1517. Find Users With Valid E-Mails](../../1501-2000/1517-find-users-with-valid-e-mails/)
- [1817. Finding the Users Active Minutes](../../1501-2000/1817-finding-the-users-active-minutes/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/percentage-of-users-attended-a-contest/)
