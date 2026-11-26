# LeetCode 1873: Calculate Special Bonus

**LeetCode Problem #1873 — Calculate Special Bonus**
Solve LeetCode Calculate Special Bonus using SQL and Database / SQL. This solution finds the optimal result using SQL Query / Relational Join & Window Function in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Calculate Special Bonus |
| LeetCode | #1873 |
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
| salary | int |
+-------------+---------+
employee_id is the primary key (column with unique values) for this table.
Each row of this table indicates the employee ID, employee name, and salary.

Write a solution to calculate the bonus of each employee. The bonus of an employee is `100%` of their salary if the ID of the employee is **an odd number** and **the employee's name does not start with the character **`'M'`. The bonus of an employee is `0` otherwise.

Return the result table ordered by `employee_id`.

The result format is in the following example.

## Examples
### Example 1
- **Input:** `Employees table:
+-------------+---------+--------+
| employee_id | name | salary |
+-------------+---------+--------+
| 2 | Meir | 3000 |
| 3 | Michael | 3800 |
| 7 | Addilyn | 7400 |
| 8 | Juan | 6100 |
| 9 | Kannon | 7700 |
+-------------+---------+--------+`
- **Output:** `+-------------+-------+
| employee_id | bonus |
+-------------+-------+
| 2 | 0 |
| 3 | 0 |
| 7 | 7400 |
| 8 | 0 |
| 9 | 7700 |
+-------------+-------+`
- **Explanation:** The employees with IDs 2 and 8 get 0 bonus because they have an even employee_id.
The employee with ID 3 gets 0 bonus because their name starts with 'M'.
The rest of the employees get a 100% bonus.

## Key Insight
Leverage **Database / SQL** with **Relational Table** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We solve **Calculate Special Bonus** by formulating an SQL query that applies relational algebra and SQL aggregation clauses. We order the final result set using `ORDER BY`.

## Algorithm
1. Sort the projected result.
2. Project and return the requested output columns.

## Example Walkthrough
1. **Input State:** We begin with `Employees table:
+-------------+---------+--------+
| employee_id | name | salary |
+-------------+---------+--------+
| 2 | Meir | 3000 |
| 3 | Michael | 3800 |
| 7 | Addilyn | 7400 |
| 8 | Juan | 6100 |
| 9 | Kannon | 7700 |
+-------------+---------+--------+`.
2. **Processing Steps:** We apply **SQL Query / Relational Join & Window Function** using our **Relational Table**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `+-------------+-------+
| employee_id | bonus |
+-------------+-------+
| 2 | 0 |
| 3 | 0 |
| 7 | 7400 |
| 8 | 0 |
| 9 | 7700 |
+-------------+-------+`.
4. **Verification:** The employees with IDs 2 and 8 get 0 bonus because they have an even employee_id.
The employee with ID 3 gets 0 bonus because their name starts with 'M'.
The rest of the employees get a 100% bonus.

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
    employee_id,
    CASE
        WHEN employee_id % 2 = 1
             AND name NOT LIKE 'M%'
        THEN salary
        ELSE 0
    END AS bonus
FROM Employees
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
- [1716. Calculate Money in Leetcode Bank](../../1501-2000/1716-calculate-money-in-leetcode-bank/)
- [2243. Calculate Digit Sum of a String](../../2001-2500/2243-calculate-digit-sum-of-a-string/)
- [2303. Calculate Amount Paid in Taxes](../../2001-2500/2303-calculate-amount-paid-in-taxes/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/calculate-special-bonus/)
