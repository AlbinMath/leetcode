# LeetCode 577: Employee Bonus

**LeetCode Problem #577 — Employee Bonus**
Solve LeetCode Employee Bonus using SQL and Database / SQL. This solution finds the optimal result using SQL Query / Relational Join & Window Function in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Employee Bonus |
| LeetCode | #577 |
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
| empId | int |
| name | varchar |
| supervisor | int |
| salary | int |
+-------------+---------+
empId is the column with unique values for this table.
Each row of this table indicates the name and the ID of an employee in addition to their salary and the id of their manager.

Table: `Bonus`

+-------------+------+
| Column Name | Type |
+-------------+------+
| empId | int |
| bonus | int |
+-------------+------+
empId is the column of unique values for this table.
empId is a foreign key (reference column) to empId from the Employee table.
Each row of this table contains the id of an employee and their respective bonus.

Write a solution to report the name and bonus amount of each employee who satisfies either of the following:

The employee has a bonus **less than** `1000`. 
 The employee did not get any bonus.

Return the result table in **any order**.

The result format is in the following example.

## Examples
### Example 1
- **Input:** `Employee table:
+-------+--------+------------+--------+
| empId | name | supervisor | salary |
+-------+--------+------------+--------+
| 3 | Brad | null | 4000 |
| 1 | John | 3 | 1000 |
| 2 | Dan | 3 | 2000 |
| 4 | Thomas | 3 | 4000 |
+-------+--------+------------+--------+
Bonus table:
+-------+-------+
| empId | bonus |
+-------+-------+
| 2 | 500 |
| 4 | 2000 |
+-------+-------+`
- **Output:** `+------+-------+
| name | bonus |
+------+-------+
| Brad | null |
| John | null |
| Dan | 500 |
+------+-------+`

## Key Insight
Leverage **Database / SQL** with **Relational Table** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We solve **Employee Bonus** by formulating an SQL query that applies relational algebra and SQL aggregation clauses. We join the tables on matching foreign and primary keys. Rows are filtered using `WHERE` / `HAVING` to satisfy the problem constraints.

## Algorithm
1. Join relevant tables on matching key columns.
2. Filter records according to problem criteria.
3. Project and return the requested output columns.

## Example Walkthrough
1. **Input State:** We begin with `Employee table:
+-------+--------+------------+--------+
| empId | name | supervisor | salary |
+-------+--------+------------+--------+
| 3 | Brad | null | 4000 |
| 1 | John | 3 | 1000 |
| 2 | Dan | 3 | 2000 |
| 4 | Thomas | 3 | 4000 |
+-------+--------+------------+--------+
Bonus table:
+-------+-------+
| empId | bonus |
+-------+-------+
| 2 | 500 |
| 4 | 2000 |
+-------+-------+`.
2. **Processing Steps:** We apply **SQL Query / Relational Join & Window Function** using our **Relational Table**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `+------+-------+
| name | bonus |
+------+-------+
| Brad | null |
| John | null |
| Dan | 500 |
+------+-------+`.

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
    e.name,
    b.bonus
FROM Employee e
LEFT JOIN Bonus b
    ON e.empId = b.empId
WHERE b.bonus < 1000
   OR b.bonus IS NULL;
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
- [690. Employee Importance](../../0501-1000/0690-employee-importance/)
- [1378. Replace Employee ID With The Unique Identifier](../../1501-2000/1509-replace-employee-id-with-the-unique-identifier/)
- [1731. The Number of Employees Which Report to Each Employee](../../1501-2000/1882-the-number-of-employees-which-report-to-each-employee/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/employee-bonus/)
