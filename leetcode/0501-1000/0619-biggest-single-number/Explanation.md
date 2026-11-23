# LeetCode 619: Biggest Single Number

**LeetCode Problem #619 — Biggest Single Number**
Solve LeetCode Biggest Single Number using SQL and Database / SQL. This solution finds the optimal result using SQL Query / Relational Join & Window Function in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Biggest Single Number |
| LeetCode | #619 |
| Difficulty | Easy |
| Language | SQL |
| Algorithm | SQL Query / Relational Join & Window Function |
| Data Structure | Relational Table |
| Pattern | Database / SQL |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Table: `MyNumbers`

+-------------+------+
| Column Name | Type |
+-------------+------+
| num | int |
+-------------+------+
This table may contain duplicates (In other words, there is no primary key for this table in SQL).
Each row of this table contains an integer.

A **single number** is a number that appeared only once in the `MyNumbers` table.

Find the largest **single number**. If there is no **single number**, report `null`.

The result format is in the following example.

## Examples
### Example 1
- **Input:** `MyNumbers table:
+-----+
| num |
+-----+
| 8 |
| 8 |
| 3 |
| 3 |
| 1 |
| 4 |
| 5 |
| 6 |
+-----+`
- **Output:** `+-----+
| num |
+-----+
| 6 |
+-----+`
- **Explanation:** The single numbers are 1, 4, 5, and 6.
Since 6 is the largest single number, we return it.

### Example 2
- **Input:** `MyNumbers table:
+-----+
| num |
+-----+
| 8 |
| 8 |
| 7 |
| 7 |
| 3 |
| 3 |
| 3 |
+-----+`
- **Output:** `+------+
| num |
+------+
| null |
+------+`
- **Explanation:** There are no single numbers in the input table so we return null.

## Key Insight
Leverage **Database / SQL** with **Relational Table** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We solve **Biggest Single Number** by formulating an SQL query that applies relational algebra and SQL aggregation clauses. We group records using `GROUP BY` and compute metrics with aggregate functions. Rows are filtered using `WHERE` / `HAVING` to satisfy the problem constraints.

## Algorithm
1. Group records and calculate aggregated summary metrics.
2. Filter records according to problem criteria.
3. Project and return the requested output columns.

## Example Walkthrough
1. **Input State:** We begin with `MyNumbers table:
+-----+
| num |
+-----+
| 8 |
| 8 |
| 3 |
| 3 |
| 1 |
| 4 |
| 5 |
| 6 |
+-----+`.
2. **Processing Steps:** We apply **SQL Query / Relational Join & Window Function** using our **Relational Table**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `+-----+
| num |
+-----+
| 6 |
+-----+`.
4. **Verification:** The single numbers are 1, 4, 5, and 6.
Since 6 is the largest single number, we return it.

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
SELECT MAX(num) AS num
FROM MyNumbers
WHERE num IN (
    SELECT num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(*) = 1
);
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
- [136. Single Number](../../0001-0500/0136-single-number/)
- [137. Single Number II](../../0001-0500/0137-single-number-ii/)
- [260. Single Number III](../../0001-0500/0260-single-number-iii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/biggest-single-number/)
