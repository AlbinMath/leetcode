# LeetCode 3793: Find Users with High Token Usage

**LeetCode Problem #3793 — Find Users with High Token Usage**
Solve LeetCode Find Users with High Token Usage using SQL and Database / SQL. This solution finds the optimal result using SQL Query / Relational Join & Window Function in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Users with High Token Usage |
| LeetCode | #3793 |
| Difficulty | Easy |
| Language | SQL |
| Algorithm | SQL Query / Relational Join & Window Function |
| Data Structure | Relational Table |
| Pattern | Database / SQL |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Table: `prompts`

+-------------+---------+
| Column Name | Type |
+-------------+---------+
| user_id | int |
| prompt | varchar |
| tokens | int |
+-------------+---------+
(user_id, prompt) is the primary key (unique value) for this table.
Each row represents a prompt submitted by a user to an AI system along with the number of tokens consumed.

Write a solution to analyze **AI prompt usage patterns** based on the following requirements:

For each user, calculate the **total number of prompts** they have submitted. 
 For each user, calculate the **average tokens used per prompt **(Rounded to `2` decimal places). 
 Only include users who have submitted **at least **`3`** prompts**. 
 Only include users who have submitted **at least one prompt** with `tokens` **greater than** their own average token usage.

Return *the result table ordered by **average tokens** in **descending** order, and then by `user_id` in **ascending** order.*

The result format is in the following example.

## Examples
Consider the standard input for **Find Users with High Token Usage**. Applying **SQL Query / Relational Join & Window Function** yields the target result step by step.

## Key Insight
Leverage **Database / SQL** with **Relational Table** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We solve **Find Users with High Token Usage** by formulating an SQL query that applies relational algebra and SQL aggregation clauses. We group records using `GROUP BY` and compute metrics with aggregate functions. Rows are filtered using `WHERE` / `HAVING` to satisfy the problem constraints. We order the final result set using `ORDER BY`.

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
    user_id,
    COUNT(*) AS prompt_count,
    ROUND(AVG(tokens), 2) AS avg_tokens
FROM prompts
GROUP BY user_id
HAVING COUNT(*) >= 3
   AND MAX(tokens) > AVG(tokens)
ORDER BY
    avg_tokens DESC,
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
- [1517. Find Users With Valid E-Mails](../../1501-2000/1517-find-users-with-valid-e-mails/)
- [3808. Find Emotionally Consistent Users](../../3501-4000/3808-find-emotionally-consistent-users/)
- [3832. Find Users with Persistent Behavior Patterns](../../3501-4000/3832-find-users-with-persistent-behavior-patterns/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-users-with-high-token-usage/)
