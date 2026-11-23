# LeetCode 3808: Find Emotionally Consistent Users

**LeetCode Problem #3808 — Find Emotionally Consistent Users**
Solve LeetCode Find Emotionally Consistent Users using SQL and Database / SQL. This solution finds the optimal result using SQL Query / Relational Join & Window Function in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Emotionally Consistent Users |
| LeetCode | #3808 |
| Difficulty | Medium |
| Language | SQL |
| Algorithm | SQL Query / Relational Join & Window Function |
| Data Structure | Relational Table |
| Pattern | Database / SQL |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Table: `reactions`

+--------------+---------+
| Column Name | Type |
+--------------+---------+
| user_id | int |
| content_id | int |
| reaction | varchar |
+--------------+---------+
(user_id, content_id) is the primary key (unique value) for this table.
Each row represents a reaction given by a user to a piece of content.

Write a solution to identify **emotionally consistent users** based on the following requirements:

For each user, count the total number of reactions they have given. 
 Only include users who have reacted to **at least **`5`** different content items**. 
 A user is considered **emotionally consistent** if **at least **`60%` of their reactions are of the **same type**.

Return *the result table ordered by* `reaction_ratio` *in **descending** order and then by* `user_id` *in **ascending** order*.

**Note:**

`reaction_ratio` should be rounded to `2` decimal places

The result format is in the following example.

## Examples
Consider the standard input for **Find Emotionally Consistent Users**. Applying **SQL Query / Relational Join & Window Function** yields the target result step by step.

## Key Insight
Leverage **Database / SQL** with **Relational Table** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We solve **Find Emotionally Consistent Users** by formulating an SQL query that applies relational algebra and SQL aggregation clauses. We join the tables on matching foreign and primary keys. We group records using `GROUP BY` and compute metrics with aggregate functions. Rows are filtered using `WHERE` / `HAVING` to satisfy the problem constraints. We order the final result set using `ORDER BY`.

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
WITH ReactionCounts AS (
    SELECT
        user_id,
        reaction,
        COUNT(*) AS reaction_count
    FROM reactions
    GROUP BY user_id, reaction
),
UserStats AS (
    SELECT
        user_id,
        SUM(reaction_count) AS total_reactions,
        MAX(reaction_count) AS max_reaction_count
    FROM ReactionCounts
    GROUP BY user_id
),
DominantReaction AS (
    SELECT
        rc.user_id,
        rc.reaction,
        rc.reaction_count,
        ROW_NUMBER() OVER (
            PARTITION BY rc.user_id
            ORDER BY rc.reaction_count DESC, rc.reaction ASC
        ) AS rn
    FROM ReactionCounts rc
)
SELECT
    d.user_id,
    d.reaction AS dominant_reaction,
    ROUND(
        d.reaction_count / u.total_reactions,
        2
    ) AS reaction_ratio
FROM DominantReaction d
JOIN UserStats u
    ON d.user_id = u.user_id
WHERE d.rn = 1
  AND u.total_reactions >= 5
  AND d.reaction_count / u.total_reactions >= 0.60
ORDER BY
    reaction_ratio DESC,
    d.user_id ASC;
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
- [3832. Find Users with Persistent Behavior Patterns](../../4001-4500/4227-find-users-with-persistent-behavior-patterns/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-emotionally-consistent-users/)
