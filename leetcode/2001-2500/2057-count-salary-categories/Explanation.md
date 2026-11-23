# LeetCode 1907: Count Salary Categories

**LeetCode Problem #1907 — Count Salary Categories**
Solve LeetCode Count Salary Categories using SQL and Database / SQL. This solution finds the optimal result using SQL Query / Relational Join & Window Function in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Salary Categories |
| LeetCode | #1907 |
| Difficulty | Medium |
| Language | SQL |
| Algorithm | SQL Query / Relational Join & Window Function |
| Data Structure | Relational Table |
| Pattern | Database / SQL |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Table: `Accounts`

+-------------+------+
| Column Name | Type |
+-------------+------+
| account_id | int |
| income | int |
+-------------+------+
account_id is the primary key (column with unique values) for this table.
Each row contains information about the monthly income for one bank account.

Write a solution to calculate the number of bank accounts for each salary category. The salary categories are:

`"Low Salary"`: All the salaries **strictly less** than `$20000`. 
 `"Average Salary"`: All the salaries in the **inclusive** range `[$20000, $50000]`. 
 `"High Salary"`: All the salaries **strictly greater** than `$50000`.

The result table **must** contain all three categories. If there are no accounts in a category, return `0`.

Return the result table in **any order**.

The result format is in the following example.

## Examples
### Example 1
- **Input:** `Accounts table:
+------------+--------+
| account_id | income |
+------------+--------+
| 3 | 108939 |
| 2 | 12747 |
| 8 | 87709 |
| 6 | 91796 |
+------------+--------+`
- **Output:** `+----------------+----------------+
| category | accounts_count |
+----------------+----------------+
| Low Salary | 1 |
| Average Salary | 0 |
| High Salary | 3 |
+----------------+----------------+`
- **Explanation:** Low Salary: Account 2.
Average Salary: No accounts.
High Salary: Accounts 3, 6, and 8.

## Key Insight
Leverage **Database / SQL** with **Relational Table** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We solve **Count Salary Categories** by formulating an SQL query that applies relational algebra and SQL aggregation clauses. We join the tables on matching foreign and primary keys. We group records using `GROUP BY` and compute metrics with aggregate functions.

## Algorithm
1. Join relevant tables on matching key columns.
2. Group records and calculate aggregated summary metrics.
3. Project and return the requested output columns.

## Example Walkthrough
1. **Input State:** We begin with `Accounts table:
+------------+--------+
| account_id | income |
+------------+--------+
| 3 | 108939 |
| 2 | 12747 |
| 8 | 87709 |
| 6 | 91796 |
+------------+--------+`.
2. **Processing Steps:** We apply **SQL Query / Relational Join & Window Function** using our **Relational Table**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `+----------------+----------------+
| category | accounts_count |
+----------------+----------------+
| Low Salary | 1 |
| Average Salary | 0 |
| High Salary | 3 |
+----------------+----------------+`.
4. **Verification:** Low Salary: Account 2.
Average Salary: No accounts.
High Salary: Accounts 3, 6, and 8.

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
    category,
    COUNT(a.account_id) AS accounts_count
FROM (
    SELECT 'Low Salary' AS category
    UNION ALL
    SELECT 'Average Salary'
    UNION ALL
    SELECT 'High Salary'
) c
LEFT JOIN Accounts a
    ON (c.category = 'Low Salary' AND a.income < 20000)
    OR (c.category = 'Average Salary' AND a.income BETWEEN 20000 AND 50000)
    OR (c.category = 'High Salary' AND a.income > 50000)
GROUP BY category;
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
- [38. Count and Say](../../0001-0500/0038-count-and-say/)
- [204. Count Primes](../../0001-0500/0204-count-primes/)
- [222. Count Complete Tree Nodes](../../0001-0500/0222-count-complete-tree-nodes/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-salary-categories/)
