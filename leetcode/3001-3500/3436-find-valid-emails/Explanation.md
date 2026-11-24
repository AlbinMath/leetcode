# LeetCode 3436: Find Valid Emails

**LeetCode Problem #3436 — Find Valid Emails**
Solve LeetCode Find Valid Emails using SQL and Database / SQL. This solution finds the optimal result using SQL Query / Relational Join & Window Function in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Valid Emails |
| LeetCode | #3436 |
| Difficulty | Easy |
| Language | SQL |
| Algorithm | SQL Query / Relational Join & Window Function |
| Data Structure | Relational Table |
| Pattern | Database / SQL |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Table: `Users`

+-----------------+---------+
| Column Name | Type |
+-----------------+---------+
| user_id | int |
| email | varchar |
+-----------------+---------+
(user_id) is the unique key for this table.
Each row contains a user's unique ID and email address.

Write a solution to find all the **valid email addresses**. A valid email address meets the following criteria:

It contains exactly one `@` symbol. 
 It ends with `.com`. 
 The part before the `@` symbol contains only **alphanumeric** characters and **underscores**. 
 The part after the `@` symbol and before `.com` contains a domain name **that contains only letters**.

Return* the result table ordered by* `user_id` *in* **ascending ***order*.

## Examples
Consider the standard input for **Find Valid Emails**. Applying **SQL Query / Relational Join & Window Function** yields the target result step by step.

## Key Insight
Leverage **Database / SQL** with **Relational Table** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We solve **Find Valid Emails** by formulating an SQL query that applies relational algebra and SQL aggregation clauses. Rows are filtered using `WHERE` / `HAVING` to satisfy the problem constraints. We order the final result set using `ORDER BY`.

## Algorithm
1. Filter records according to problem criteria.
2. Sort the projected result.
3. Project and return the requested output columns.

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
    email
FROM Users
WHERE email REGEXP '^[A-Za-z0-9_]+@[A-Za-z]+[.]com$'
ORDER BY user_id ASC;
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
- [1964. Find the Longest Valid Obstacle Course at Each Position](../../1501-2000/1964-find-the-longest-valid-obstacle-course-at-each-position/)
- [3302. Find the Lexicographically Smallest Valid Sequence](../../3001-3500/3302-find-the-lexicographically-smallest-valid-sequence/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-valid-emails/)
