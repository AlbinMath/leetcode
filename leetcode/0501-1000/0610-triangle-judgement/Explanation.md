# LeetCode 610: Triangle Judgement

**LeetCode Problem #610 — Triangle Judgement**
Solve LeetCode Triangle Judgement using SQL and Database / SQL. This solution finds the optimal result using SQL Query / Relational Join & Window Function in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Triangle Judgement |
| LeetCode | #610 |
| Difficulty | Easy |
| Language | SQL |
| Algorithm | SQL Query / Relational Join & Window Function |
| Data Structure | Relational Table |
| Pattern | Database / SQL |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Table: `Triangle`

+-------------+------+
| Column Name | Type |
+-------------+------+
| x | int |
| y | int |
| z | int |
+-------------+------+
In SQL, (x, y, z) is the primary key column for this table.
Each row of this table contains the lengths of three line segments.

Report for every three line segments whether they can form a triangle.

Return the result table in **any order**.

The result format is in the following example.

## Examples
### Example 1
- **Input:** `Triangle table:
+----+----+----+
| x | y | z |
+----+----+----+
| 13 | 15 | 30 |
| 10 | 20 | 15 |
+----+----+----+`
- **Output:** `+----+----+----+----------+
| x | y | z | triangle |
+----+----+----+----------+
| 13 | 15 | 30 | No |
| 10 | 20 | 15 | Yes |
+----+----+----+----------+`

## Key Insight
Leverage **Database / SQL** with **Relational Table** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We solve **Triangle Judgement** by formulating an SQL query that applies relational algebra and SQL aggregation clauses.

## Algorithm
1. Execute target query with relational operators.
2. Format and return final projection.
3. Project and return the requested output columns.

## Example Walkthrough
1. **Input State:** We begin with `Triangle table:
+----+----+----+
| x | y | z |
+----+----+----+
| 13 | 15 | 30 |
| 10 | 20 | 15 |
+----+----+----+`.
2. **Processing Steps:** We apply **SQL Query / Relational Join & Window Function** using our **Relational Table**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `+----+----+----+----------+
| x | y | z | triangle |
+----+----+----+----------+
| 13 | 15 | 30 | No |
| 10 | 20 | 15 | Yes |
+----+----+----+----------+`.

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
    x,
    y,
    z,
    CASE
        WHEN x + y > z
         AND x + z > y
         AND y + z > x
        THEN 'Yes'
        ELSE 'No'
    END AS triangle
FROM Triangle;
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
- [118. Pascal's Triangle](../../0001-0500/0118-pascals-triangle/)
- [119. Pascal's Triangle II](../../0001-0500/0119-pascals-triangle-ii/)
- [120. Triangle](../../0001-0500/0120-triangle/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/triangle-judgement/)
