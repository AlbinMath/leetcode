# LeetCode 1683: Invalid Tweets

**LeetCode Problem #1683 — Invalid Tweets**
Solve LeetCode Invalid Tweets using SQL and Database / SQL. This solution finds the optimal result using SQL Query / Relational Join & Window Function in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Invalid Tweets |
| LeetCode | #1683 |
| Difficulty | Easy |
| Language | SQL |
| Algorithm | SQL Query / Relational Join & Window Function |
| Data Structure | Relational Table |
| Pattern | Database / SQL |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Table: `Tweets`

+----------------+---------+
| Column Name | Type |
+----------------+---------+
| tweet_id | int |
| content | varchar |
+----------------+---------+
tweet_id is the primary key (column with unique values) for this table.
content consists of alphanumeric characters, '!', or ' ' and no other special characters.
This table contains all the tweets in a social media app.

Write a solution to find the IDs of the invalid tweets. The tweet is invalid if the number of characters used in the content of the tweet is **strictly greater** than `15`.

Return the result table in **any order**.

The result format is in the following example.

## Examples
### Example 1
- **Input:** `Tweets table:
+----------+-----------------------------------+
| tweet_id | content |
+----------+-----------------------------------+
| 1 | Let us Code |
| 2 | More than fifteen chars are here! |
+----------+-----------------------------------+`
- **Output:** `+----------+
| tweet_id |
+----------+
| 2 |
+----------+`
- **Explanation:** Tweet 1 has length = 11. It is a valid tweet.
Tweet 2 has length = 33. It is an invalid tweet.

## Key Insight
Leverage **Database / SQL** with **Relational Table** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We solve **Invalid Tweets** by formulating an SQL query that applies relational algebra and SQL aggregation clauses. Rows are filtered using `WHERE` / `HAVING` to satisfy the problem constraints.

## Algorithm
1. Filter records according to problem criteria.
2. Project and return the requested output columns.

## Example Walkthrough
1. **Input State:** We begin with `Tweets table:
+----------+-----------------------------------+
| tweet_id | content |
+----------+-----------------------------------+
| 1 | Let us Code |
| 2 | More than fifteen chars are here! |
+----------+-----------------------------------+`.
2. **Processing Steps:** We apply **SQL Query / Relational Join & Window Function** using our **Relational Table**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `+----------+
| tweet_id |
+----------+
| 2 |
+----------+`.
4. **Verification:** Tweet 1 has length = 11. It is a valid tweet.
Tweet 2 has length = 33. It is an invalid tweet.

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
SELECT tweet_id
FROM Tweets
WHERE LEN(content) > 15;
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
- [301. Remove Invalid Parentheses](../../0001-0500/0301-remove-invalid-parentheses/)
- [1169. Invalid Transactions](../../1001-1500/1272-invalid-transactions/)
- [3451. Find Invalid IP Addresses](../../3501-4000/3792-find-invalid-ip-addresses/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/invalid-tweets/)
