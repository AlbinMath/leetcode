# LeetCode 176: Second Highest Salary

**LeetCode Problem #176 — Second Highest Salary**
Solve LeetCode Second Highest Salary using SQL and Database / SQL. This solution finds the optimal result using SQL Query / Relational Join & Window Function in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Second Highest Salary |
| LeetCode | #176 |
| Difficulty | Medium |
| Language | SQL |
| Algorithm | SQL Query / Relational Join & Window Function |
| Data Structure | Relational Table |
| Pattern | Database / SQL |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Table: `Employee`

+-------------+------+
| Column Name | Type |
+-------------+------+
| id | int |
| salary | int |
+-------------+------+
id is the primary key (column with unique values) for this table.
Each row of this table contains information about the salary of an employee.

Write a solution to find the second highest **distinct** salary from the `Employee` table. If there is no second highest salary, return `null (return None in Pandas)`.

The result format is in the following example.

## Examples
### Example 1
- **Input:** `Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1 | 100 |
| 2 | 200 |
| 3 | 300 |
+----+--------+`
- **Output:** `+---------------------+
| SecondHighestSalary |
+---------------------+
| 200 |
+---------------------+`

### Example 2
- **Input:** `Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1 | 100 |
+----+--------+`
- **Output:** `+---------------------+
| SecondHighestSalary |
+---------------------+
| null |
+---------------------+`

## Key Insight
Leverage **Database / SQL** with **Relational Table** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We solve **Second Highest Salary** by formulating an SQL query that applies relational algebra and SQL aggregation clauses. We order the final result set using `ORDER BY`.

## Algorithm
1. Sort the projected result.
2. Project and return the requested output columns.

## Example Walkthrough
1. **Input State:** We begin with `Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1 | 100 |
| 2 | 200 |
| 3 | 300 |
+----+--------+`.
2. **Processing Steps:** We apply **SQL Query / Relational Join & Window Function** using our **Relational Table**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `+---------------------+
| SecondHighestSalary |
+---------------------+
| 200 |
+---------------------+`.

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
SELECT (
    SELECT DISTINCT salary
    FROM Employee
    ORDER BY salary DESC
    LIMIT 1 OFFSET 1
) AS SecondHighestSalary;
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
- [177. Nth Highest Salary](../../0001-0500/0177-nth-highest-salary/)
- [184. Department Highest Salary](../../0001-0500/0184-department-highest-salary/)
- [1732. Find the Highest Altitude](../../1501-2000/1833-find-the-highest-altitude/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/second-highest-salary/)
