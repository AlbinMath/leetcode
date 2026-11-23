# LeetCode 1965: Employees With Missing Information

**LeetCode Problem #1965 — Employees With Missing Information**
Solve LeetCode Employees With Missing Information using SQL and Database / SQL. This solution finds the optimal result using SQL Query / Relational Join & Window Function in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Employees With Missing Information |
| LeetCode | #1965 |
| Difficulty | Easy |
| Language | SQL |
| Algorithm | SQL Query / Relational Join & Window Function |
| Data Structure | Relational Table |
| Pattern | Database / SQL |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Table: `Employees`

+-------------+---------+
| Column Name | Type |
+-------------+---------+
| employee_id | int |
| name | varchar |
+-------------+---------+
employee_id is the column with unique values for this table.
Each row of this table indicates the name of the employee whose ID is employee_id.

Table: `Salaries`

+-------------+---------+
| Column Name | Type |
+-------------+---------+
| employee_id | int |
| salary | int |
+-------------+---------+
employee_id is the column with unique values for this table.
Each row of this table indicates the salary of the employee whose ID is employee_id.

Write a solution to report the IDs of all the employees with **missing information**. The information of an employee is missing if:

The employee's **name** is missing, or 
 The employee's **salary** is missing.

Return the result table ordered by `employee_id` **in ascending order**.

The result format is in the following example.

## Examples
### Example 1
- **Input:** `Employees table:
+-------------+----------+
| employee_id | name |
+-------------+----------+
| 2 | Crew |
| 4 | Haven |
| 5 | Kristian |
+-------------+----------+
Salaries table:
+-------------+--------+
| employee_id | salary |
+-------------+--------+
| 5 | 76071 |
| 1 | 22517 |
| 4 | 63539 |
+-------------+--------+`
- **Output:** `+-------------+
| employee_id |
+-------------+
| 1 |
| 2 |
+-------------+`
- **Explanation:** Employees 1, 2, 4, and 5 are working at this company.
The name of employee 1 is missing.
The salary of employee 2 is missing.

## Key Insight
Leverage **Database / SQL** with **Relational Table** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We solve **Employees With Missing Information** by formulating an SQL query that applies relational algebra and SQL aggregation clauses. We join the tables on matching foreign and primary keys. Rows are filtered using `WHERE` / `HAVING` to satisfy the problem constraints. We order the final result set using `ORDER BY`.

## Algorithm
1. Join relevant tables on matching key columns.
2. Filter records according to problem criteria.
3. Sort the projected result.
4. Project and return the requested output columns.

## Example Walkthrough
1. **Input State:** We begin with `Employees table:
+-------------+----------+
| employee_id | name |
+-------------+----------+
| 2 | Crew |
| 4 | Haven |
| 5 | Kristian |
+-------------+----------+
Salaries table:
+-------------+--------+
| employee_id | salary |
+-------------+--------+
| 5 | 76071 |
| 1 | 22517 |
| 4 | 63539 |
+-------------+--------+`.
2. **Processing Steps:** We apply **SQL Query / Relational Join & Window Function** using our **Relational Table**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `+-------------+
| employee_id |
+-------------+
| 1 |
| 2 |
+-------------+`.
4. **Verification:** Employees 1, 2, 4, and 5 are working at this company.
The name of employee 1 is missing.
The salary of employee 2 is missing.

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
SELECT e.employee_id
FROM Employees e
LEFT JOIN Salaries s
    ON e.employee_id = s.employee_id
WHERE s.employee_id IS NULL

UNION

SELECT s.employee_id
FROM Salaries s
LEFT JOIN Employees e
    ON s.employee_id = e.employee_id
WHERE e.employee_id IS NULL

ORDER BY employee_id;
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
- [181. Employees Earning More Than Their Managers](../../0001-0500/0181-employees-earning-more-than-their-managers/)
- [627. Swap Sex of Employees](../../0501-1000/0627-swap-sex-of-employees/)
- [1075. Project Employees I](../../1001-1500/1161-project-employees-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/employees-with-missing-information/)
