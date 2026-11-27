# LeetCode 1731: The Number of Employees Which Report to Each Employee

**LeetCode Problem #1731 — The Number of Employees Which Report to Each Employee**
Solve LeetCode The Number of Employees Which Report to Each Employee using SQL and Database / SQL. This solution finds the optimal result using SQL Query / Relational Join & Window Function in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | The Number of Employees Which Report to Each Employee |
| LeetCode | #1731 |
| Difficulty | Easy |
| Language | SQL |
| Algorithm | SQL Query / Relational Join & Window Function |
| Data Structure | Relational Table |
| Pattern | Database / SQL |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Table: `Employees`

+-------------+----------+
| Column Name | Type |
+-------------+----------+
| employee_id | int |
| name | varchar |
| reports_to | int |
| age | int |
+-------------+----------+
employee_id is the column with unique values for this table.
This table contains information about the employees and the id of the manager they report to. Some employees do not report to anyone (reports_to is null).

For this problem, we will consider a **manager** an employee who has at least 1 other employee reporting to them.

Write a solution to report the ids and the names of all **managers**, the number of employees who report **directly** to them, and the average age of the reports rounded to the nearest integer.

Return the result table ordered by `employee_id`.

The result format is in the following example.

## Examples
### Example 1
- **Input:** `Employees table:
+-------------+---------+------------+-----+
| employee_id | name | reports_to | age |
+-------------+---------+------------+-----+
| 9 | Hercy | null | 43 |
| 6 | Alice | 9 | 41 |
| 4 | Bob | 9 | 36 |
| 2 | Winston | null | 37 |
+-------------+---------+------------+-----+`
- **Output:** `+-------------+-------+---------------+-------------+
| employee_id | name | reports_count | average_age |
+-------------+-------+---------------+-------------+
| 9 | Hercy | 2 | 39 |
+-------------+-------+---------------+-------------+`
- **Explanation:** Hercy has 2 people report directly to him, Alice and Bob. Their average age is (41+36)/2 = 38.5, which is 39 after rounding it to the nearest integer.

### Example 2
- **Input:** `Employees table:
+-------------+---------+------------+-----+ 
| employee_id | name | reports_to | age |
|-------------|---------|------------|-----|
| 1 | Michael | null | 45 |
| 2 | Alice | 1 | 38 |
| 3 | Bob | 1 | 42 |
| 4 | Charlie | 2 | 34 |
| 5 | David | 2 | 40 |
| 6 | Eve | 3 | 37 |
| 7 | Frank | null | 50 |
| 8 | Grace | null | 48 |
+-------------+---------+------------+-----+`
- **Output:** `+-------------+---------+---------------+-------------+
| employee_id | name | reports_count | average_age |
| ----------- | ------- | ------------- | ----------- |
| 1 | Michael | 2 | 40 |
| 2 | Alice | 2 | 37 |
| 3 | Bob | 1 | 37 |
+-------------+---------+---------------+-------------+`

## Key Insight
Leverage **Database / SQL** with **Relational Table** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We solve **The Number of Employees Which Report to Each Employee** by formulating an SQL query that applies relational algebra and SQL aggregation clauses. We join the tables on matching foreign and primary keys. We group records using `GROUP BY` and compute metrics with aggregate functions. We order the final result set using `ORDER BY`.

## Algorithm
1. Join relevant tables on matching key columns.
2. Group records and calculate aggregated summary metrics.
3. Sort the projected result.
4. Project and return the requested output columns.

## Example Walkthrough
1. **Input State:** We begin with `Employees table:
+-------------+---------+------------+-----+
| employee_id | name | reports_to | age |
+-------------+---------+------------+-----+
| 9 | Hercy | null | 43 |
| 6 | Alice | 9 | 41 |
| 4 | Bob | 9 | 36 |
| 2 | Winston | null | 37 |
+-------------+---------+------------+-----+`.
2. **Processing Steps:** We apply **SQL Query / Relational Join & Window Function** using our **Relational Table**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `+-------------+-------+---------------+-------------+
| employee_id | name | reports_count | average_age |
+-------------+-------+---------------+-------------+
| 9 | Hercy | 2 | 39 |
+-------------+-------+---------------+-------------+`.
4. **Verification:** Hercy has 2 people report directly to him, Alice and Bob. Their average age is (41+36)/2 = 38.5, which is 39 after rounding it to the nearest integer.

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
    m.employee_id,
    m.name,
    COUNT(e.employee_id) AS reports_count,
    ROUND(AVG(CAST(e.age AS FLOAT)), 0) AS average_age
FROM Employees m
JOIN Employees e
    ON m.employee_id = e.reports_to
GROUP BY
    m.employee_id,
    m.name
ORDER BY
    m.employee_id;
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
- [2930. Number of Strings Which Can Be Rearranged to Contain Substring](../../2501-3000/2930-number-of-strings-which-can-be-rearranged-to-contain-substring/)
- [1741. Find Total Time Spent by Each Employee](../../1501-2000/1741-find-total-time-spent-by-each-employee/)
- [1789. Primary Department for Each Employee](../../1501-2000/1789-primary-department-for-each-employee/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/the-number-of-employees-which-report-to-each-employee/)
