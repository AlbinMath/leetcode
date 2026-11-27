# LeetCode 3673: Find Zombie Sessions

**LeetCode Problem #3673 — Find Zombie Sessions**
Solve LeetCode Find Zombie Sessions using SQL and Database / SQL. This solution finds the optimal result using SQL Query / Relational Join & Window Function in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Zombie Sessions |
| LeetCode | #3673 |
| Difficulty | Hard |
| Language | SQL |
| Algorithm | SQL Query / Relational Join & Window Function |
| Data Structure | Relational Table |
| Pattern | Database / SQL |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Table: `app_events`

+------------------+----------+
| Column Name | Type | 
+------------------+----------+
| event_id | int |
| user_id | int |
| event_timestamp | datetime |
| event_type | varchar |
| session_id | varchar |
| event_value | int |
+------------------+----------+
event_id is the unique identifier for this table.
event_type can be app_open, click, scroll, purchase, or app_close.
session_id groups events within the same user session.
event_value represents: for purchase - amount in dollars, for scroll - pixels scrolled, for others - NULL.

Write a solution to identify **zombie sessions, **sessions where users appear active but show abnormal behavior patterns. A session is considered a **zombie session** if it meets ALL the following criteria:

The session duration is **more than** `30` minutes. 
 Has **at least** `5` scroll events. 
 The **click-to-scroll ratio** is less than `0.20` . 
 **No purchases** were made during the session.

Return *the result table ordered by* `scroll_count` *in **descending** order, then by* `session_id` *in **ascending** order*.

The result format is in the following example.

## Examples
Consider the standard input for **Find Zombie Sessions**. Applying **SQL Query / Relational Join & Window Function** yields the target result step by step.

## Key Insight
Leverage **Database / SQL** with **Relational Table** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We solve **Find Zombie Sessions** by formulating an SQL query that applies relational algebra and SQL aggregation clauses. We group records using `GROUP BY` and compute metrics with aggregate functions. Rows are filtered using `WHERE` / `HAVING` to satisfy the problem constraints. We order the final result set using `ORDER BY`.

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
SELECT
    session_id,
    MAX(user_id) AS user_id,
    DATEDIFF(
        MINUTE,
        MIN(event_timestamp),
        MAX(event_timestamp)
    ) AS session_duration_minutes,
    SUM(CASE WHEN event_type = 'scroll' THEN 1 ELSE 0 END) AS scroll_count
FROM app_events
GROUP BY session_id
HAVING
    -- Duration more than 30 minutes
    DATEDIFF(
        MINUTE,
        MIN(event_timestamp),
        MAX(event_timestamp)
    ) > 30

    -- At least 5 scroll events
    AND SUM(
        CASE WHEN event_type = 'scroll' THEN 1 ELSE 0 END
    ) >= 5

    -- Click-to-scroll ratio < 0.20
    AND CAST(
        SUM(CASE WHEN event_type = 'click' THEN 1 ELSE 0 END)
        AS DECIMAL(10, 4)
    )
    /
    SUM(CASE WHEN event_type = 'scroll' THEN 1 ELSE 0 END)
    < 0.20

    -- No purchases
    AND SUM(
        CASE WHEN event_type = 'purchase' THEN 1 ELSE 0 END
    ) = 0

ORDER BY
    scroll_count DESC,
    session_id ASC;
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
- [28. Find the Index of the First Occurrence in a String](../../0001-0500/0028-find-the-index-of-the-first-occurrence-in-a-string/)
- [34. Find First and Last Position of Element in Sorted Array](../../0001-0500/0034-find-first-and-last-position-of-element-in-sorted-array/)
- [153. Find Minimum in Rotated Sorted Array](../../0001-0500/0153-find-minimum-in-rotated-sorted-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-zombie-sessions/)
