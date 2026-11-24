# LeetCode 3642: Find Books with Polarized Opinions

**LeetCode Problem #3642 — Find Books with Polarized Opinions**
Solve LeetCode Find Books with Polarized Opinions using SQL and Database / SQL. This solution finds the optimal result using SQL Query / Relational Join & Window Function in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Books with Polarized Opinions |
| LeetCode | #3642 |
| Difficulty | Medium |
| Language | SQL |
| Algorithm | SQL Query / Relational Join & Window Function |
| Data Structure | Relational Table |
| Pattern | Database / SQL |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Table: `books`

+-------------+---------+
| Column Name | Type |
+-------------+---------+
| book_id | int |
| title | varchar |
| author | varchar |
| genre | varchar |
| pages | int |
+-------------+---------+
book_id is the unique ID for this table.
Each row contains information about a book including its genre and page count.

Table: `reading_sessions`

+----------------+---------+
| Column Name | Type |
+----------------+---------+
| session_id | int |
| book_id | int |
| reader_name | varchar |
| pages_read | int |
| session_rating | int |
+----------------+---------+
session_id is the unique ID for this table.
Each row represents a reading session where someone read a portion of a book. session_rating is on a scale of 1-5.

Write a solution to find books that have **polarized opinions** - books that receive both very high ratings and very low ratings from different readers.

A book has polarized opinions if it has `at least one rating &ge; 4` and `at least one rating &le; 2` 
 Only consider books that have **at least **`5`** reading sessions** 
 Calculate the **rating spread** as (`highest_rating - lowest_rating`) 
 Calculate the **polarization score** as the number of extreme ratings (`ratings &le; 2 or &ge; 4`) divided by total sessions 
 **Only include** books where `polarization score &ge; 0.6` (at least `60%` extreme ratings)

Return *the result table ordered by polarization score in **descending** order, then by title in **descending** order*. 
The *polarization score* should be rounded to 2 decimal places.

The result format is in the following example.

## Examples
Consider the standard input for **Find Books with Polarized Opinions**. Applying **SQL Query / Relational Join & Window Function** yields the target result step by step.

## Key Insight
Leverage **Database / SQL** with **Relational Table** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We solve **Find Books with Polarized Opinions** by formulating an SQL query that applies relational algebra and SQL aggregation clauses. We join the tables on matching foreign and primary keys. We group records using `GROUP BY` and compute metrics with aggregate functions. Rows are filtered using `WHERE` / `HAVING` to satisfy the problem constraints. We order the final result set using `ORDER BY`.

## Algorithm
1. Join relevant tables on matching key columns.
2. Group records and calculate aggregated summary metrics.
3. Filter records according to problem criteria.
4. Sort the projected result.
5. Project and return the requested output columns.

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
WITH book_stats AS (
    SELECT
        rs.book_id,
        COUNT(*) AS total_sessions,
        MAX(rs.session_rating) AS highest_rating,
        MIN(rs.session_rating) AS lowest_rating,

        SUM(
            CASE
                WHEN rs.session_rating >= 4
                  OR rs.session_rating <= 2
                THEN 1
                ELSE 0
            END
        ) AS extreme_ratings,

        SUM(
            CASE
                WHEN rs.session_rating >= 4
                THEN 1
                ELSE 0
            END
        ) AS high_ratings,

        SUM(
            CASE
                WHEN rs.session_rating <= 2
                THEN 1
                ELSE 0
            END
        ) AS low_ratings

    FROM reading_sessions rs
    GROUP BY rs.book_id
)

SELECT
    b.book_id,
    b.title,
    b.author,
    b.genre,
    b.pages,

    bs.highest_rating - bs.lowest_rating AS rating_spread,

    ROUND(
        CAST(bs.extreme_ratings AS DECIMAL(10, 2))
        / bs.total_sessions,
        2
    ) AS polarization_score

FROM books b
JOIN book_stats bs
    ON b.book_id = bs.book_id

WHERE bs.total_sessions >= 5
  AND bs.high_ratings >= 1
  AND bs.low_ratings >= 1
  AND (
        CAST(bs.extreme_ratings AS DECIMAL(10, 2))
        / bs.total_sessions
      ) >= 0.6

ORDER BY
    polarization_score DESC,
    b.title DESC;
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
- [3570. Find Books with No Available Copies](../../3501-4000/3570-find-books-with-no-available-copies/)
- [28. Find the Index of the First Occurrence in a String](../../0001-0500/0028-find-the-index-of-the-first-occurrence-in-a-string/)
- [34. Find First and Last Position of Element in Sorted Array](../../0001-0500/0034-find-first-and-last-position-of-element-in-sorted-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-books-with-polarized-opinions/)
