# LeetCode 2356: Number of Unique Subjects Taught by Each Teacher

**LeetCode Problem #2356 — Number of Unique Subjects Taught by Each Teacher**
Solve LeetCode Number of Unique Subjects Taught by Each Teacher using SQL and Database / SQL. This solution finds the optimal result using SQL Query / Relational Join & Window Function in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Unique Subjects Taught by Each Teacher |
| LeetCode | #2356 |
| Difficulty | Easy |
| Language | SQL |
| Algorithm | SQL Query / Relational Join & Window Function |
| Data Structure | Relational Table |
| Pattern | Database / SQL |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Table: `Teacher`

+-------------+------+
| Column Name | Type |
+-------------+------+
| teacher_id | int |
| subject_id | int |
| dept_id | int |
+-------------+------+
(subject_id, dept_id) is the primary key (combinations of columns with unique values) of this table.
Each row in this table indicates that the teacher with teacher_id teaches the subject subject_id in the department dept_id.

Write a solution to calculate the number of unique subjects each teacher teaches in the university.

Return the result table in **any order**.

The result format is shown in the following example.

## Examples
### Example 1
- **Input:** `Teacher table:
+------------+------------+---------+
| teacher_id | subject_id | dept_id |
+------------+------------+---------+
| 1 | 2 | 3 |
| 1 | 2 | 4 |
| 1 | 3 | 3 |
| 2 | 1 | 1 |
| 2 | 2 | 1 |
| 2 | 3 | 1 |
| 2 | 4 | 1 |
+------------+------------+---------+`
- **Output:** `+------------+-----+
| teacher_id | cnt |
+------------+-----+
| 1 | 2 |
| 2 | 4 |
+------------+-----+`
- **Explanation:** Teacher 1:
 - They teach subject 2 in departments 3 and 4.
 - They teach subject 3 in department 3.
Teacher 2:
 - They teach subject 1 in department 1.
 - They teach subject 2 in department 1.
 - They teach subject 3 in department 1.
 - They teach subject 4 in department 1.

## Key Insight
Leverage **Database / SQL** with **Relational Table** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We solve **Number of Unique Subjects Taught by Each Teacher** by formulating an SQL query that applies relational algebra and SQL aggregation clauses. We group records using `GROUP BY` and compute metrics with aggregate functions.

## Algorithm
1. Group records and calculate aggregated summary metrics.
2. Project and return the requested output columns.

## Example Walkthrough
1. **Input State:** We begin with `Teacher table:
+------------+------------+---------+
| teacher_id | subject_id | dept_id |
+------------+------------+---------+
| 1 | 2 | 3 |
| 1 | 2 | 4 |
| 1 | 3 | 3 |
| 2 | 1 | 1 |
| 2 | 2 | 1 |
| 2 | 3 | 1 |
| 2 | 4 | 1 |
+------------+------------+---------+`.
2. **Processing Steps:** We apply **SQL Query / Relational Join & Window Function** using our **Relational Table**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `+------------+-----+
| teacher_id | cnt |
+------------+-----+
| 1 | 2 |
| 2 | 4 |
+------------+-----+`.
4. **Verification:** Teacher 1:
 - They teach subject 2 in departments 3 and 4.
 - They teach subject 3 in department 3.
Teacher 2:
 - They teach subject 1 in department 1.
 - They teach subject 2 in department 1.
 - They teach subject 3 in department 1.
 - They teach subject 4 in department 1.

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
SELECT teacher_id, COUNT(DISTINCT subject_id) AS cnt
FROM Teacher
GROUP BY teacher_id;
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
- [1178. Number of Valid Words for Each Puzzle](../../1001-1500/1282-number-of-valid-words-for-each-puzzle/)
- [1434. Number of Ways to Wear Different Hats to Each Other](../../1501-2000/1531-number-of-ways-to-wear-different-hats-to-each-other/)
- [1731. The Number of Employees Which Report to Each Employee](../../1501-2000/1882-the-number-of-employees-which-report-to-each-employee/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-unique-subjects-taught-by-each-teacher/)
