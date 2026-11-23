# LeetCode 1341: Movie Rating

**LeetCode Problem #1341 — Movie Rating**
Solve LeetCode Movie Rating using SQL and Database / SQL. This solution finds the optimal result using SQL Query / Relational Join & Window Function in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Movie Rating |
| LeetCode | #1341 |
| Difficulty | Medium |
| Language | SQL |
| Algorithm | SQL Query / Relational Join & Window Function |
| Data Structure | Relational Table |
| Pattern | Database / SQL |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Table: `Movies`

+---------------+---------+
| Column Name | Type |
+---------------+---------+
| movie_id | int |
| title | varchar |
+---------------+---------+
movie_id is the primary key (column with unique values) for this table.
title is the name of the movie.
Each movie has a unique title.

Table: `Users`

+---------------+---------+
| Column Name | Type |
+---------------+---------+
| user_id | int |
| name | varchar |
+---------------+---------+
user_id is the primary key (column with unique values) for this table.
The column 'name' has unique values.

Table: `MovieRating`

+---------------+---------+
| Column Name | Type |
+---------------+---------+
| movie_id | int |
| user_id | int |
| rating | int |
| created_at | date |
+---------------+---------+
(movie_id, user_id) is the primary key (column with unique values) for this table.
This table contains the rating of a movie by a user in their review.
created_at is the user's review date.

Write a solution to:

Find the name of the user who has rated the greatest number of movies. In case of a tie, return the lexicographically smaller user name. 
 Find the movie name with the **highest average** rating in `February 2020`. In case of a tie, return the lexicographically smaller movie name.

The result format is in the following example.

## Examples
### Example 1
- **Input:** `Movies table:
+-------------+--------------+
| movie_id | title |
+-------------+--------------+
| 1 | Avengers |
| 2 | Frozen 2 |
| 3 | Joker |
+-------------+--------------+
Users table:
+-------------+--------------+
| user_id | name |
+-------------+--------------+
| 1 | Daniel |
| 2 | Monica |
| 3 | Maria |
| 4 | James |
+-------------+--------------+
MovieRating table:
+-------------+--------------+--------------+-------------+
| movie_id | user_id | rating | created_at |
+-------------+--------------+--------------+-------------+
| 1 | 1 | 3 | 2020-01-12 |
| 1 | 2 | 4 | 2020-02-11 |
| 1 | 3 | 2 | 2020-02-12 |
| 1 | 4 | 1 | 2020-01-01 |
| 2 | 1 | 5 | 2020-02-17 | 
| 2 | 2 | 2 | 2020-02-01 | 
| 2 | 3 | 2 | 2020-03-01 |
| 3 | 1 | 3 | 2020-02-22 | 
| 3 | 2 | 4 | 2020-02-25 | 
+-------------+--------------+--------------+-------------+`
- **Output:** `+--------------+
| results |
+--------------+
| Daniel |
| Frozen 2 |
+--------------+`
- **Explanation:** Daniel and Monica have rated 3 movies ("Avengers", "Frozen 2" and "Joker") but Daniel is smaller lexicographically.
Frozen 2 and Joker have a rating average of 3.5 in February but Frozen 2 is smaller lexicographically.

## Key Insight
Leverage **Database / SQL** with **Relational Table** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We solve **Movie Rating** by formulating an SQL query that applies relational algebra and SQL aggregation clauses. We join the tables on matching foreign and primary keys. We group records using `GROUP BY` and compute metrics with aggregate functions. Rows are filtered using `WHERE` / `HAVING` to satisfy the problem constraints. We order the final result set using `ORDER BY`.

## Algorithm
1. Join relevant tables on matching key columns.
2. Group records and calculate aggregated summary metrics.
3. Filter records according to problem criteria.
4. Sort the projected result.
5. Project and return the requested output columns.

## Example Walkthrough
1. **Input State:** We begin with `Movies table:
+-------------+--------------+
| movie_id | title |
+-------------+--------------+
| 1 | Avengers |
| 2 | Frozen 2 |
| 3 | Joker |
+-------------+--------------+
Users table:
+-------------+--------------+
| user_id | name |
+-------------+--------------+
| 1 | Daniel |
| 2 | Monica |
| 3 | Maria |
| 4 | James |
+-------------+--------------+
MovieRating table:
+-------------+--------------+--------------+-------------+
| movie_id | user_id | rating | created_at |
+-------------+--------------+--------------+-------------+
| 1 | 1 | 3 | 2020-01-12 |
| 1 | 2 | 4 | 2020-02-11 |
| 1 | 3 | 2 | 2020-02-12 |
| 1 | 4 | 1 | 2020-01-01 |
| 2 | 1 | 5 | 2020-02-17 | 
| 2 | 2 | 2 | 2020-02-01 | 
| 2 | 3 | 2 | 2020-03-01 |
| 3 | 1 | 3 | 2020-02-22 | 
| 3 | 2 | 4 | 2020-02-25 | 
+-------------+--------------+--------------+-------------+`.
2. **Processing Steps:** We apply **SQL Query / Relational Join & Window Function** using our **Relational Table**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `+--------------+
| results |
+--------------+
| Daniel |
| Frozen 2 |
+--------------+`.
4. **Verification:** Daniel and Monica have rated 3 movies ("Avengers", "Frozen 2" and "Joker") but Daniel is smaller lexicographically.
Frozen 2 and Joker have a rating average of 3.5 in February but Frozen 2 is smaller lexicographically.

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
(SELECT u.name AS results
 FROM Users u
 JOIN MovieRating r ON u.user_id = r.user_id
 GROUP BY u.user_id, u.name
 ORDER BY COUNT(*) DESC, u.name
 LIMIT 1)

UNION ALL

(SELECT m.title AS results
 FROM Movies m
 JOIN MovieRating r ON m.movie_id = r.movie_id
 WHERE r.created_at >= '2020-02-01'
   AND r.created_at < '2020-03-01'
 GROUP BY m.movie_id, m.title
 ORDER BY AVG(r.rating) DESC, m.title
 LIMIT 1);
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
- [2353. Design a Food Rating System](../../2001-2500/2429-design-a-food-rating-system/)
- [1912. Design Movie Rental System](../../2001-2500/2023-design-movie-rental-system/)
- [175. Combine Two Tables](../../0001-0500/0175-combine-two-tables/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/movie-rating/)
