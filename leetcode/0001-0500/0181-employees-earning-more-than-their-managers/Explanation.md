# LeetCode 181: Employees Earning More Than Their Managers

**LeetCode Problem #181 — Employees Earning More Than Their Managers**
Solve LeetCode Employees Earning More Than Their Managers using SQL and Database / SQL. This solution finds the optimal result using SQL Query / Relational Join & Window Function in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Employees Earning More Than Their Managers |
| LeetCode | #181 |
| Difficulty | Easy |
| Language | SQL |
| Algorithm | SQL Query / Relational Join & Window Function |
| Data Structure | Relational Table |
| Pattern | Database / SQL |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Table: `Employee`

+-------------+---------+
| Column Name | Type |
+-------------+---------+
| id | int |
| name | varchar |
| salary | int |
| managerId | int |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table indicates the ID of an employee, their name, salary, and the ID of their manager.

Write a solution to find the employees who earn more than their managers.

Return the result table in **any order**.

The result format is in the following example.

## Examples
### Example 1
- **Input:** `Employee table:
+----+-------+--------+-----------+
| id | name | salary | managerId |
+----+-------+--------+-----------+
| 1 | Joe | 70000 | 3 |
| 2 | Henry | 80000 | 4 |
| 3 | Sam | 60000 | Null |
| 4 | Max | 90000 | Null |
+----+-------+--------+-----------+`
- **Output:** `+----------+
| Employee |
+----------+
| Joe |
+----------+`
- **Explanation:** Joe is the only employee who earns more than his manager.

## Key Insight
Leverage **Database / SQL** with **Relational Table** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We solve **Employees Earning More Than Their Managers** by formulating an SQL query that applies relational algebra and SQL aggregation clauses. We join the tables on matching foreign and primary keys. Rows are filtered using `WHERE` / `HAVING` to satisfy the problem constraints.

## Algorithm
1. Join relevant tables on matching key columns.
2. Filter records according to problem criteria.
3. Project and return the requested output columns.

## Example Walkthrough
1. **Input State:** We begin with `Employee table:
+----+-------+--------+-----------+
| id | name | salary | managerId |
+----+-------+--------+-----------+
| 1 | Joe | 70000 | 3 |
| 2 | Henry | 80000 | 4 |
| 3 | Sam | 60000 | Null |
| 4 | Max | 90000 | Null |
+----+-------+--------+-----------+`.
2. **Processing Steps:** We apply **SQL Query / Relational Join & Window Function** using our **Relational Table**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `+----------+
| Employee |
+----------+
| Joe |
+----------+`.
4. **Verification:** Joe is the only employee who earns more than his manager.

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
SELECT e.name AS Employee
FROM Employee e
JOIN Employee m ON e.managerId = m.id
WHERE e.salary > m.salary;
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
- [1287. Element Appearing More Than 25% In Sorted Array](../../1001-1500/1287-element-appearing-more-than-25-in-sorted-array/)
- [1566. Detect Pattern of Length M Repeated K or More Times](../../1501-2000/1566-detect-pattern-of-length-m-repeated-k-or-more-times/)
- [1604. Alert Using Same Key-Card Three or More Times in a One Hour Period](../../1501-2000/1604-alert-using-same-key-card-three-or-more-times-in-a-one-hour-period/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/employees-earning-more-than-their-managers/)
