# LeetCode 3451: Find Invalid IP Addresses

**LeetCode Problem #3451 — Find Invalid IP Addresses**
Solve LeetCode Find Invalid IP Addresses using SQL and Database / SQL. This solution finds the optimal result using SQL Query / Relational Join & Window Function in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Invalid IP Addresses |
| LeetCode | #3451 |
| Difficulty | Hard |
| Language | SQL |
| Algorithm | SQL Query / Relational Join & Window Function |
| Data Structure | Relational Table |
| Pattern | Database / SQL |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Table: ` logs`

+-------------+---------+
| Column Name | Type |
+-------------+---------+
| log_id | int |
| ip | varchar |
| status_code | int |
+-------------+---------+
log_id is the unique key for this table.
Each row contains server access log information including IP address and HTTP status code.

Write a solution to find **invalid IP addresses**. Each octet in an IP address contains between `1` and `3` digits. An IPv4 address is invalid if it meets any of these conditions:

Contains a number **greater than** `255` in any octet. 
 Has **leading zeros** in any octet (for example, `01.02.03.04`). 
 Has **fewer or more** than `4` octets.

Return *the result table **ordered by* `invalid_count`, `ip` *in **descending** order respectively*.

The result format is in the following example.

## Examples
Consider the standard input for **Find Invalid IP Addresses**. Applying **SQL Query / Relational Join & Window Function** yields the target result step by step.

## Key Insight
Leverage **Database / SQL** with **Relational Table** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We solve **Find Invalid IP Addresses** by formulating an SQL query that applies relational algebra and SQL aggregation clauses. We group records using `GROUP BY` and compute metrics with aggregate functions. Rows are filtered using `WHERE` / `HAVING` to satisfy the problem constraints. We order the final result set using `ORDER BY`.

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
SELECT
    ip,
    COUNT(*) AS invalid_count
FROM logs
WHERE NOT (
    ip REGEXP '^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$'
)
GROUP BY ip
ORDER BY invalid_count DESC, ip DESC;
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
- [93. Restore IP Addresses](../../0001-0500/0093-restore-ip-addresses/)
- [929. Unique Email Addresses](../../0501-1000/0965-unique-email-addresses/)
- [301. Remove Invalid Parentheses](../../0001-0500/0301-remove-invalid-parentheses/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-invalid-ip-addresses/)
