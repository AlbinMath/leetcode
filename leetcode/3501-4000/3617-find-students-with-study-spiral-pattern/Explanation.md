# LeetCode 3617: Find Students with Study Spiral Pattern

**LeetCode Problem #3617 — Find Students with Study Spiral Pattern**
Solve LeetCode Find Students with Study Spiral Pattern using SQL and Database / SQL. This solution finds the optimal result using SQL Query / Relational Join & Window Function in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Students with Study Spiral Pattern |
| LeetCode | #3617 |
| Difficulty | Hard |
| Language | SQL |
| Algorithm | SQL Query / Relational Join & Window Function |
| Data Structure | Relational Table |
| Pattern | Database / SQL |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Table: `students`

+--------------+---------+
| Column Name | Type |
+--------------+---------+
| student_id | int |
| student_name | varchar |
| major | varchar |
+--------------+---------+
student_id is the unique identifier for this table.
Each row contains information about a student and their academic major.

Table: `study_sessions`

+---------------+---------+
| Column Name | Type |
+---------------+---------+
| session_id | int |
| student_id | int |
| subject | varchar |
| session_date | date |
| hours_studied | decimal |
+---------------+---------+
session_id is the unique identifier for this table.
Each row represents a study session by a student for a specific subject.

Write a solution to find students who follow the **Study Spiral Pattern** - students who consistently study multiple subjects in a rotating cycle.

A Study Spiral Pattern means a student studies at least `3`** different subjects** in a repeating sequence 
 The pattern must repeat for **at least **`2`** complete cycles** (minimum `6` study sessions) 
 Sessions must be **consecutive dates** with no gaps longer than `2` days between sessions 
 Calculate the **cycle length** (number of different subjects in the pattern) 
 Calculate the **total study hours** across all sessions in the pattern 
 Only include students with cycle length of **at least **`3`** subjects**

Return *the result table ordered by cycle length in **descending** order, then by total study hours in **descending** order*.

The result format is in the following example.

## Examples
Consider the standard input for **Find Students with Study Spiral Pattern**. Applying **SQL Query / Relational Join & Window Function** yields the target result step by step.

## Key Insight
Leverage **Database / SQL** with **Relational Table** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We solve **Find Students with Study Spiral Pattern** by formulating an SQL query that applies relational algebra and SQL aggregation clauses. We join the tables on matching foreign and primary keys. We group records using `GROUP BY` and compute metrics with aggregate functions. Rows are filtered using `WHERE` / `HAVING` to satisfy the problem constraints. We order the final result set using `ORDER BY`.

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
WITH ordered AS (
    SELECT
        ss.*,
        ROW_NUMBER() OVER (
            PARTITION BY student_id
            ORDER BY session_date, session_id
        ) AS rn,
        LAG(session_date) OVER (
            PARTITION BY student_id
            ORDER BY session_date, session_id
        ) AS prev_date
    FROM study_sessions ss
),

grouped AS (
    SELECT
        *,
        SUM(
            CASE
                WHEN prev_date IS NULL
                     OR DATEDIFF(day, prev_date, session_date) > 2
                THEN 1
                ELSE 0
            END
        ) OVER (
            PARTITION BY student_id
            ORDER BY rn
            ROWS UNBOUNDED PRECEDING
        ) AS grp
    FROM ordered
),

sequence_info AS (
    SELECT
        student_id,
        grp,
        COUNT(*) AS session_count,
        COUNT(DISTINCT subject) AS subject_count,
        SUM(hours_studied) AS total_hours
    FROM grouped
    GROUP BY student_id, grp
    HAVING COUNT(*) >= 6
       AND COUNT(DISTINCT subject) >= 3
),

numbers AS (
    SELECT 3 AS n
    UNION ALL SELECT 4
    UNION ALL SELECT 5
    UNION ALL SELECT 6
    UNION ALL SELECT 7
    UNION ALL SELECT 8
    UNION ALL SELECT 9
    UNION ALL SELECT 10
    UNION ALL SELECT 11
    UNION ALL SELECT 12
    UNION ALL SELECT 13
    UNION ALL SELECT 14
    UNION ALL SELECT 15
    UNION ALL SELECT 16
    UNION ALL SELECT 17
    UNION ALL SELECT 18
    UNION ALL SELECT 19
    UNION ALL SELECT 20
),

candidates AS (
    SELECT
        si.student_id,
        si.grp,
        si.session_count,
        si.total_hours,
        n.n AS cycle_length
    FROM sequence_info si
    JOIN numbers n
        ON n.n >= 3
       AND n.n <= si.session_count / 2
       AND si.session_count % n.n = 0
),

pattern_validation AS (
    SELECT
        c.student_id,
        c.grp,
        c.cycle_length,
        c.total_hours,

        COUNT(DISTINCT
            CASE
                WHEN g.rn <= c.cycle_length
                THEN g.subject
            END
        ) AS first_cycle_subjects,

        COUNT(*) AS total_sessions,

        COUNT(DISTINCT
            CONCAT(
                (g.rn - 1) % c.cycle_length,
                '|',
                g.subject
            )
        ) AS unique_positions

    FROM candidates c
    JOIN grouped g
        ON g.student_id = c.student_id
       AND g.grp = c.grp

    GROUP BY
        c.student_id,
        c.grp,
        c.cycle_length,
        c.total_hours
),

valid_patterns AS (
    SELECT
        student_id,
        grp,
        cycle_length,
        total_hours
    FROM pattern_validation
    WHERE first_cycle_subjects = cycle_length
      AND unique_positions = cycle_length
)

SELECT
    s.student_id,
    s.student_name,
    s.major,
    vp.cycle_length,
    vp.total_hours AS total_study_hours
FROM valid_patterns vp
JOIN students s
    ON s.student_id = vp.student_id
ORDER BY
    vp.cycle_length DESC,
    vp.total_hours DESC;
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
- [890. Find and Replace Pattern](../../0501-1000/0890-find-and-replace-pattern/)
- [3421. Find Students Who Improved](../../3001-3500/3421-find-students-who-improved/)
- [54. Spiral Matrix](../../0001-0500/0054-spiral-matrix/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-students-with-study-spiral-pattern/)
