# LeetCode 626: Exchange Seats

**LeetCode Problem #626 — Exchange Seats**
Solve LeetCode Exchange Seats using SQL and Database / SQL. This solution finds the optimal result using SQL Query / Relational Join & Window Function in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Exchange Seats |
| LeetCode | #626 |
| Difficulty | Medium |
| Language | SQL |
| Algorithm | SQL Query / Relational Join & Window Function |
| Data Structure | Relational Table |
| Pattern | Database / SQL |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Table: `Seat`

+-------------+---------+
| Column Name | Type |
+-------------+---------+
| id | int |
| student | varchar |
+-------------+---------+
id is the primary key (unique value) column for this table.
Each row of this table indicates the name and the ID of a student.
The ID sequence always starts from 1 and increments continuously.

Write a solution to swap the seat id of every two consecutive students. If the number of students is odd, the id of the last student is not swapped.

Return the result table ordered by `id` **in ascending order**.

The result format is in the following example.

## Examples
### Example 1
- **Input:** `Seat table:
+----+---------+
| id | student |
+----+---------+
| 1 | Abbot |
| 2 | Doris |
| 3 | Emerson |
| 4 | Green |
| 5 | Jeames |
+----+---------+`
- **Output:** `+----+---------+
| id | student |
+----+---------+
| 1 | Doris |
| 2 | Abbot |
| 3 | Green |
| 4 | Emerson |
| 5 | Jeames |
+----+---------+`
- **Explanation:** Note that if the number of students is odd, there is no need to change the last one's seat.

## Key Insight
Leverage **Database / SQL** with **Relational Table** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We solve **Exchange Seats** by formulating an SQL query that applies relational algebra and SQL aggregation clauses. We order the final result set using `ORDER BY`.

## Algorithm
1. Sort the projected result.
2. Project and return the requested output columns.

## Example Walkthrough
1. **Input State:** We begin with `Seat table:
+----+---------+
| id | student |
+----+---------+
| 1 | Abbot |
| 2 | Doris |
| 3 | Emerson |
| 4 | Green |
| 5 | Jeames |
+----+---------+`.
2. **Processing Steps:** We apply **SQL Query / Relational Join & Window Function** using our **Relational Table**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `+----+---------+
| id | student |
+----+---------+
| 1 | Doris |
| 2 | Abbot |
| 3 | Green |
| 4 | Emerson |
| 5 | Jeames |
+----+---------+`.
4. **Verification:** Note that if the number of students is odd, there is no need to change the last one's seat.

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
    CASE
        WHEN id % 2 = 1 AND id < (SELECT MAX(id) FROM Seat)
            THEN id + 1
        WHEN id % 2 = 0
            THEN id - 1
        ELSE id
    END AS id,
    student
FROM Seat
ORDER BY id;
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
- [175. Combine Two Tables](../../0001-0500/0175-combine-two-tables/)
- [176. Second Highest Salary](../../0001-0500/0176-second-highest-salary/)
- [177. Nth Highest Salary](../../0001-0500/0177-nth-highest-salary/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/exchange-seats/)
