# LeetCode 262: Trips and Users

**LeetCode Problem #262 — Trips and Users**
Solve LeetCode Trips and Users using SQL and Database / SQL. This solution finds the optimal result using SQL Query / Relational Join & Window Function in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Trips and Users |
| LeetCode | #262 |
| Difficulty | Hard |
| Language | SQL |
| Algorithm | SQL Query / Relational Join & Window Function |
| Data Structure | Relational Table |
| Pattern | Database / SQL |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Table: `Trips`

+-------------+----------+
| Column Name | Type |
+-------------+----------+
| id | int |
| client_id | int |
| driver_id | int |
| city_id | int |
| status | enum |
| request_at | varchar | 
+-------------+----------+
id is the primary key (column with unique values) for this table.
The table holds all taxi trips. Each trip has a unique id, while client_id and driver_id are foreign keys to the users_id at the Users table.
Status is an ENUM (category) type of ('completed', 'cancelled_by_driver', 'cancelled_by_client').

Table: `Users`

+-------------+----------+
| Column Name | Type |
+-------------+----------+
| users_id | int |
| banned | enum |
| role | enum |
+-------------+----------+
users_id is the primary key (column with unique values) for this table.
The table holds all users. Each user has a unique users_id, and role is an ENUM type of ('client', 'driver', 'partner').
banned is an ENUM (category) type of ('Yes', 'No').

The **cancellation rate** is computed by dividing the number of canceled (by client or driver) requests with unbanned users by the total number of requests with unbanned users on that day.

Write a solution to find the **cancellation rate** of requests with unbanned users (**both client and driver must not be banned**) each day between `"2013-10-01"` and `"2013-10-03"` with **at least** one trip. Round `Cancellation Rate` to **two decimal** points.

Return the result table in **any order**.

The result format is in the following example.

## Examples
### Example 1
- **Input:** `Trips table:
+----+-----------+-----------+---------+---------------------+------------+
| id | client_id | driver_id | city_id | status | request_at |
+----+-----------+-----------+---------+---------------------+------------+
| 1 | 1 | 10 | 1 | completed | 2013-10-01 |
| 2 | 2 | 11 | 1 | cancelled_by_driver | 2013-10-01 |
| 3 | 3 | 12 | 6 | completed | 2013-10-01 |
| 4 | 4 | 13 | 6 | cancelled_by_client | 2013-10-01 |
| 5 | 1 | 10 | 1 | completed | 2013-10-02 |
| 6 | 2 | 11 | 6 | completed | 2013-10-02 |
| 7 | 3 | 12 | 6 | completed | 2013-10-02 |
| 8 | 2 | 12 | 12 | completed | 2013-10-03 |
| 9 | 3 | 10 | 12 | completed | 2013-10-03 |
| 10 | 4 | 13 | 12 | cancelled_by_driver | 2013-10-03 |
+----+-----------+-----------+---------+---------------------+------------+
Users table:
+----------+--------+--------+
| users_id | banned | role |
+----------+--------+--------+
| 1 | No | client |
| 2 | Yes | client |
| 3 | No | client |
| 4 | No | client |
| 10 | No | driver |
| 11 | No | driver |
| 12 | No | driver |
| 13 | No | driver |
+----------+--------+--------+`
- **Output:** `+------------+-------------------+
| Day | Cancellation Rate |
+------------+-------------------+
| 2013-10-01 | 0.33 |
| 2013-10-02 | 0.00 |
| 2013-10-03 | 0.50 |
+------------+-------------------+`
- **Explanation:** On 2013-10-01:
 - There were 4 requests in total, 2 of which were canceled.
 - However, the request with Id=2 was made by a banned client (User_Id=2), so it is ignored in the calculation.
 - Hence there are 3 unbanned requests in total, 1 of which was canceled.
 - The Cancellation Rate is (1 / 3) = 0.33
On 2013-10-02:
 - There were 3 requests in total, 0 of which were canceled.
 - The request with Id=6 was made by a banned client, so it is ignored.
 - Hence there are 2 unbanned requests in total, 0 of which were canceled.
 - The Cancellation Rate is (0 / 2) = 0.00
On 2013-10-03:
 - There were 3 requests in total, 1 of which was canceled.
 - The request with Id=8 was made by a banned client, so it is ignored.
 - Hence there are 2 unbanned request in total, 1 of which were canceled.
 - The Cancellation Rate is (1 / 2) = 0.50

## Key Insight
Leverage **Database / SQL** with **Relational Table** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We solve **Trips and Users** by formulating an SQL query that applies relational algebra and SQL aggregation clauses. We join the tables on matching foreign and primary keys. We group records using `GROUP BY` and compute metrics with aggregate functions. Rows are filtered using `WHERE` / `HAVING` to satisfy the problem constraints.

## Algorithm
1. Join relevant tables on matching key columns.
2. Group records and calculate aggregated summary metrics.
3. Filter records according to problem criteria.
4. Project and return the requested output columns.

## Example Walkthrough
1. **Input State:** We begin with `Trips table:
+----+-----------+-----------+---------+---------------------+------------+
| id | client_id | driver_id | city_id | status | request_at |
+----+-----------+-----------+---------+---------------------+------------+
| 1 | 1 | 10 | 1 | completed | 2013-10-01 |
| 2 | 2 | 11 | 1 | cancelled_by_driver | 2013-10-01 |
| 3 | 3 | 12 | 6 | completed | 2013-10-01 |
| 4 | 4 | 13 | 6 | cancelled_by_client | 2013-10-01 |
| 5 | 1 | 10 | 1 | completed | 2013-10-02 |
| 6 | 2 | 11 | 6 | completed | 2013-10-02 |
| 7 | 3 | 12 | 6 | completed | 2013-10-02 |
| 8 | 2 | 12 | 12 | completed | 2013-10-03 |
| 9 | 3 | 10 | 12 | completed | 2013-10-03 |
| 10 | 4 | 13 | 12 | cancelled_by_driver | 2013-10-03 |
+----+-----------+-----------+---------+---------------------+------------+
Users table:
+----------+--------+--------+
| users_id | banned | role |
+----------+--------+--------+
| 1 | No | client |
| 2 | Yes | client |
| 3 | No | client |
| 4 | No | client |
| 10 | No | driver |
| 11 | No | driver |
| 12 | No | driver |
| 13 | No | driver |
+----------+--------+--------+`.
2. **Processing Steps:** We apply **SQL Query / Relational Join & Window Function** using our **Relational Table**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `+------------+-------------------+
| Day | Cancellation Rate |
+------------+-------------------+
| 2013-10-01 | 0.33 |
| 2013-10-02 | 0.00 |
| 2013-10-03 | 0.50 |
+------------+-------------------+`.
4. **Verification:** On 2013-10-01:
 - There were 4 requests in total, 2 of which were canceled.
 - However, the request with Id=2 was made by a banned client (User_Id=2), so it is ignored in the calculation.
 - Hence there are 3 unbanned requests in total, 1 of which was canceled.
 - The Cancellation Rate is (1 / 3) = 0.33
On 2013-10-02:
 - There were 3 requests in total, 0 of which were canceled.
 - The request with Id=6 was made by a banned client, so it is ignored.
 - Hence there are 2 unbanned requests in total, 0 of which were canceled.
 - The Cancellation Rate is (0 / 2) = 0.00
On 2013-10-03:
 - There were 3 requests in total, 1 of which was canceled.
 - The request with Id=8 was made by a banned client, so it is ignored.
 - Hence there are 2 unbanned request in total, 1 of which were canceled.
 - The Cancellation Rate is (1 / 2) = 0.50

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
SELECT t.request_at AS Day,
       ROUND(AVG(t.status != 'completed'), 2) AS `Cancellation Rate`
FROM Trips t
JOIN Users c ON t.client_id = c.users_id AND c.banned = 'No'
JOIN Users d ON t.driver_id = d.users_id AND d.banned = 'No'
WHERE t.request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY t.request_at;
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
- [1633. Percentage of Users Attended a Contest](../../1501-2000/1773-percentage-of-users-attended-a-contest/)
- [3793. Find Users with High Token Usage](../../4001-4500/4195-find-users-with-high-token-usage/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/trips-and-users/)
