# LeetCode 180: Consecutive Numbers

**LeetCode Problem #180 — Consecutive Numbers**
Solve LeetCode Consecutive Numbers using SQL and Database / SQL. This solution finds the optimal result using SQL Query / Relational Join & Window Function in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Consecutive Numbers |
| LeetCode | #180 |
| Difficulty | Medium |
| Language | SQL |
| Algorithm | SQL Query / Relational Join & Window Function |
| Data Structure | Relational Table |
| Pattern | Database / SQL |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Table: `Logs`

+-------------+---------+
| Column Name | Type |
+-------------+---------+
| id | int |
| num | varchar |
+-------------+---------+
In SQL, id is the primary key for this table.
id is an autoincrement column starting from 1.

Find all numbers that appear at least three times consecutively.

Return the result table in **any order**.

The result format is in the following example.

## Examples
### Example 1
- **Input:** `Logs table:
+----+-----+
| id | num |
+----+-----+
| 1 | 1 |
| 2 | 1 |
| 3 | 1 |
| 4 | 2 |
| 5 | 1 |
| 6 | 2 |
| 7 | 2 |
+----+-----+`
- **Output:** `+-----------------+
| ConsecutiveNums |
+-----------------+
| 1 |
+-----------------+`
- **Explanation:** 1 is the only number that appears consecutively for at least three times.

## Key Insight
Leverage **Database / SQL** with **Relational Table** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We solve **Consecutive Numbers** by formulating an SQL query that applies relational algebra and SQL aggregation clauses. We join the tables on matching foreign and primary keys.

## Algorithm
1. Join relevant tables on matching key columns.
2. Project and return the requested output columns.

## Example Walkthrough
1. **Input State:** We begin with `Logs table:
+----+-----+
| id | num |
+----+-----+
| 1 | 1 |
| 2 | 1 |
| 3 | 1 |
| 4 | 2 |
| 5 | 1 |
| 6 | 2 |
| 7 | 2 |
+----+-----+`.
2. **Processing Steps:** We apply **SQL Query / Relational Join & Window Function** using our **Relational Table**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `+-----------------+
| ConsecutiveNums |
+-----------------+
| 1 |
+-----------------+`.
4. **Verification:** 1 is the only number that appears consecutively for at least three times.

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
SELECT DISTINCT l1.num AS ConsecutiveNums
FROM Logs l1
JOIN Logs l2 ON l1.id = l2.id - 1 AND l1.num = l2.num
JOIN Logs l3 ON l2.id = l3.id - 1 AND l2.num = l3.num;
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
- [829. Consecutive Numbers Sum](../../0501-1000/0829-consecutive-numbers-sum/)
- [967. Numbers With Same Consecutive Differences](../../0501-1000/0967-numbers-with-same-consecutive-differences/)
- [1296. Divide Array in Sets of K Consecutive Numbers](../../1001-1500/1296-divide-array-in-sets-of-k-consecutive-numbers/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/consecutive-numbers/)
