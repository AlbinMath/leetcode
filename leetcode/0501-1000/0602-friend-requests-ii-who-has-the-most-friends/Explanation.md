# LeetCode 602: Friend Requests II: Who Has the Most Friends

**LeetCode Problem #602 — Friend Requests II: Who Has the Most Friends**
Solve LeetCode Friend Requests II: Who Has the Most Friends using SQL and Database / SQL. This solution finds the optimal result using SQL Query / Relational Join & Window Function in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Friend Requests II: Who Has the Most Friends |
| LeetCode | #602 |
| Difficulty | Medium |
| Language | SQL |
| Algorithm | SQL Query / Relational Join & Window Function |
| Data Structure | Relational Table |
| Pattern | Database / SQL |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Table: `RequestAccepted`

+----------------+---------+
| Column Name | Type |
+----------------+---------+
| requester_id | int |
| accepter_id | int |
| accept_date | date |
+----------------+---------+
(requester_id, accepter_id) is the primary key (combination of columns with unique values) for this table.
This table contains the ID of the user who sent the request, the ID of the user who received the request, and the date when the request was accepted.

Write a solution to find the people who have the most friends and the most friends number.

The test cases are generated so that only one person has the most friends.

The result format is in the following example.

## Examples
### Example 1
- **Input:** `RequestAccepted table:
+--------------+-------------+-------------+
| requester_id | accepter_id | accept_date |
+--------------+-------------+-------------+
| 1 | 2 | 2016/06/03 |
| 1 | 3 | 2016/06/08 |
| 2 | 3 | 2016/06/08 |
| 3 | 4 | 2016/06/09 |
+--------------+-------------+-------------+`
- **Output:** `+----+-----+
| id | num |
+----+-----+
| 3 | 3 |
+----+-----+`
- **Explanation:** The person with id 3 is a friend of people 1, 2, and 4, so he has three friends in total, which is the most number than any others.

## Key Insight
Leverage **Database / SQL** with **Relational Table** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We solve **Friend Requests II: Who Has the Most Friends** by formulating an SQL query that applies relational algebra and SQL aggregation clauses. We group records using `GROUP BY` and compute metrics with aggregate functions. We order the final result set using `ORDER BY`.

## Algorithm
1. Group records and calculate aggregated summary metrics.
2. Sort the projected result.
3. Project and return the requested output columns.

## Example Walkthrough
1. **Input State:** We begin with `RequestAccepted table:
+--------------+-------------+-------------+
| requester_id | accepter_id | accept_date |
+--------------+-------------+-------------+
| 1 | 2 | 2016/06/03 |
| 1 | 3 | 2016/06/08 |
| 2 | 3 | 2016/06/08 |
| 3 | 4 | 2016/06/09 |
+--------------+-------------+-------------+`.
2. **Processing Steps:** We apply **SQL Query / Relational Join & Window Function** using our **Relational Table**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `+----+-----+
| id | num |
+----+-----+
| 3 | 3 |
+----+-----+`.
4. **Verification:** The person with id 3 is a friend of people 1, 2, and 4, so he has three friends in total, which is the most number than any others.

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
WITH Friends AS (
    SELECT requester_id AS id
    FROM RequestAccepted

    UNION ALL

    SELECT accepter_id AS id
    FROM RequestAccepted
),
FriendCount AS (
    SELECT 
        id,
        COUNT(*) AS num
    FROM Friends
    GROUP BY id
)
SELECT TOP 1
    id,
    num
FROM FriendCount
ORDER BY num DESC;
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
- [1784. Check if Binary String Has at Most One Segment of Ones](../../1501-2000/1784-check-if-binary-string-has-at-most-one-segment-of-ones/)
- [3178. Find the Child Who Has the Ball After K Seconds](../../3001-3500/3178-find-the-child-who-has-the-ball-after-k-seconds/)
- [1606. Find Servers That Handled Most Number of Requests](../../1501-2000/1606-find-servers-that-handled-most-number-of-requests/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends/)
