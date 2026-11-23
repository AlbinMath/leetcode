# LeetCode 3421: Find Students Who Improved

**LeetCode Problem #3421 — Find Students Who Improved**
Solve LeetCode Find Students Who Improved using SQL and Database / SQL. This solution finds the optimal result using SQL Query / Relational Join & Window Function in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Students Who Improved |
| LeetCode | #3421 |
| Difficulty | Medium |
| Language | SQL |
| Algorithm | SQL Query / Relational Join & Window Function |
| Data Structure | Relational Table |
| Pattern | Database / SQL |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Table: `Scores`

+-------------+---------+
| Column Name | Type |
+-------------+---------+
| student_id | int |
| subject | varchar |
| score | int |
| exam_date | varchar |
+-------------+---------+
(student_id, subject, exam_date) is the primary key for this table.
Each row contains information about a student's score in a specific subject on a particular exam date. score is between 0 and 100 (inclusive).

Write a solution to find the **students who have shown improvement**. A student is considered to have shown improvement if they meet **both** of these conditions:

Have taken exams in the **same subject** on at least two different dates 
 Their **latest score** in that subject is **higher** than their **first score**

Return *the result table* *ordered by* `student_id,` `subject` *in **ascending** order*.

The result format is in the following example.

## Examples
Consider the standard input for **Find Students Who Improved**. Applying **SQL Query / Relational Join & Window Function** yields the target result step by step.

## Key Insight
Leverage **Database / SQL** with **Relational Table** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We solve **Find Students Who Improved** by formulating an SQL query that applies relational algebra and SQL aggregation clauses. We group records using `GROUP BY` and compute metrics with aggregate functions. Rows are filtered using `WHERE` / `HAVING` to satisfy the problem constraints. We order the final result set using `ORDER BY`.

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
WITH ranked AS (
    SELECT
        student_id,
        subject,
        score,
        exam_date,
        ROW_NUMBER() OVER (
            PARTITION BY student_id, subject
            ORDER BY exam_date ASC
        ) AS first_exam,
        ROW_NUMBER() OVER (
            PARTITION BY student_id, subject
            ORDER BY exam_date DESC
        ) AS latest_exam
    FROM Scores
)

SELECT
    student_id,
    subject,
    MAX(CASE WHEN first_exam = 1 THEN score END) AS first_score,
    MAX(CASE WHEN latest_exam = 1 THEN score END) AS latest_score
FROM ranked
GROUP BY student_id, subject
HAVING COUNT(*) >= 2
   AND MAX(CASE WHEN latest_exam = 1 THEN score END)
       > MAX(CASE WHEN first_exam = 1 THEN score END)
ORDER BY student_id, subject;
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
- [3617. Find Students with Study Spiral Pattern](../../3501-4000/3961-find-students-with-study-spiral-pattern/)
- [3601. Find Drivers with Improved Fuel Efficiency](../../3501-4000/3942-find-drivers-with-improved-fuel-efficiency/)
- [3178. Find the Child Who Has the Ball After K Seconds](../../3001-3500/3450-find-the-child-who-has-the-ball-after-k-seconds/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-students-who-improved/)
