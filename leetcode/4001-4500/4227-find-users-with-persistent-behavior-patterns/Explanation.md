# LeetCode 3832: Find Users with Persistent Behavior Patterns

**LeetCode Problem #3832 — Find Users with Persistent Behavior Patterns**
Solve LeetCode Find Users with Persistent Behavior Patterns using SQL and Database / SQL. This solution finds the optimal result using SQL Query / Relational Join & Window Function in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Users with Persistent Behavior Patterns |
| LeetCode | #3832 |
| Difficulty | Hard |
| Language | SQL |
| Algorithm | SQL Query / Relational Join & Window Function |
| Data Structure | Relational Table |
| Pattern | Database / SQL |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Table: `activity`

+--------------+---------+
| Column Name | Type |
+--------------+---------+
| user_id | int |
| action_date | date |
| action | varchar |
+--------------+---------+
(user_id, action_date, action) is the primary key (unique value) for this table.
Each row represents a user performing a specific action on a given date.

Write a solution to identify **behaviorally stable users** based on the following definition:

A user is considered **behaviorally stable** if there exists a sequence of **at least **`5`** consecutive days** such that:

The user performed **exactly one action per day** during that period. 
 The **action is the same** on all those consecutive days. 
 
 
 If a user has multiple qualifying sequences, only consider the sequence with the **maximum length**.

Return *the result table ordered by* `streak_length` *in **descending** order*,* then by *`user_id` *in **ascending** order*.

The result format is in the following example.

## Examples
Consider the standard input for **Find Users with Persistent Behavior Patterns**. Applying **SQL Query / Relational Join & Window Function** yields the target result step by step.

## Key Insight
Leverage **Database / SQL** with **Relational Table** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We solve **Find Users with Persistent Behavior Patterns** by formulating an SQL query that applies relational algebra and SQL aggregation clauses. We group records using `GROUP BY` and compute metrics with aggregate functions. Rows are filtered using `WHERE` / `HAVING` to satisfy the problem constraints. We order the final result set using `ORDER BY`.

## Algorithm
1. Group records and calculate aggregated summary metrics.
2. Filter records according to problem criteria.
3. Sort the projected result.
4. Project and return the requested output columns.

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
WITH DailyActivity AS (
    SELECT
        user_id,
        action_date,
        MIN(action) AS action
    FROM activity
    GROUP BY user_id, action_date
    HAVING COUNT(*) = 1
),
Grouped AS (
    SELECT
        user_id,
        action,
        action_date,
        DATEADD(
            DAY,
            -ROW_NUMBER() OVER (
                PARTITION BY user_id, action
                ORDER BY action_date
            ),
            action_date
        ) AS grp
    FROM DailyActivity
),
Streaks AS (
    SELECT
        user_id,
        action,
        COUNT(*) AS streak_length,
        MIN(action_date) AS start_date,
        MAX(action_date) AS end_date
    FROM Grouped
    GROUP BY
        user_id,
        action,
        grp
),
Ranked AS (
    SELECT
        user_id,
        action,
        streak_length,
        start_date,
        end_date,
        ROW_NUMBER() OVER (
            PARTITION BY user_id
            ORDER BY streak_length DESC, start_date ASC
        ) AS rn
    FROM Streaks
    WHERE streak_length >= 5
)
SELECT
    user_id,
    action,
    streak_length,
    start_date,
    end_date
FROM Ranked
WHERE rn = 1
ORDER BY
    streak_length DESC,
    user_id ASC;
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
- [1517. Find Users With Valid E-Mails](../../1501-2000/1664-find-users-with-valid-e-mails/)
- [3793. Find Users with High Token Usage](../../4001-4500/4195-find-users-with-high-token-usage/)
- [3808. Find Emotionally Consistent Users](../../4001-4500/4208-find-emotionally-consistent-users/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-users-with-persistent-behavior-patterns/)
