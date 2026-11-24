# LeetCode 3764: Most Common Course Pairs

**LeetCode Problem #3764 — Most Common Course Pairs**
Solve LeetCode Most Common Course Pairs using SQL and Database / SQL. This solution finds the optimal result using SQL Query / Relational Join & Window Function in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Most Common Course Pairs |
| LeetCode | #3764 |
| Difficulty | Hard |
| Language | SQL |
| Algorithm | SQL Query / Relational Join & Window Function |
| Data Structure | Relational Table |
| Pattern | Database / SQL |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Table: `course_completions`

+-------------------+---------+
| Column Name | Type | 
+-------------------+---------+
| user_id | int |
| course_id | int |
| course_name | varchar |
| completion_date | date |
| course_rating | int |
+-------------------+---------+
(user_id, course_id) is the combination of columns with unique values for this table.
Each row represents a completed course by a user with their rating (1-5 scale).

Write a solution to identify **skill mastery pathways** by analyzing course completion sequences among top-performing students:

Consider only **top-performing students** (those who completed **at least **`5`** courses** with an **average rating of **`4`** or higher**). 
 For each top performer, identify the **sequence of courses** they completed in chronological order. 
 Find all **consecutive course pairs** (`Course A &rarr; Course B`) taken by these students. 
 Return the **pair frequency**, identifying which course transitions are most common among high achievers.

Return *the result table ordered by* *pair frequency in **descending** order* *and then by first course name and second course name in **ascending** order*.

The result format is in the following example.

## Examples
Consider the standard input for **Most Common Course Pairs**. Applying **SQL Query / Relational Join & Window Function** yields the target result step by step.

## Key Insight
Leverage **Database / SQL** with **Relational Table** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We solve **Most Common Course Pairs** by formulating an SQL query that applies relational algebra and SQL aggregation clauses. We join the tables on matching foreign and primary keys. We group records using `GROUP BY` and compute metrics with aggregate functions. Rows are filtered using `WHERE` / `HAVING` to satisfy the problem constraints. We order the final result set using `ORDER BY`.

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
WITH TopLearners AS (
    SELECT
        user_id
    FROM course_completions
    GROUP BY user_id
    HAVING COUNT(*) >= 5
       AND AVG(course_rating) >= 4
),

OrderedCourses AS (
    SELECT
        c.user_id,
        c.course_name,
        LEAD(c.course_name) OVER (
            PARTITION BY c.user_id
            ORDER BY c.completion_date, c.course_id
        ) AS second_course
    FROM course_completions c
    JOIN TopLearners t
        ON c.user_id = t.user_id
),

CoursePairs AS (
    SELECT
        course_name AS first_course,
        second_course
    FROM OrderedCourses
    WHERE second_course IS NOT NULL
)

SELECT
    first_course,
    second_course,
    COUNT(*) AS transition_count
FROM CoursePairs
GROUP BY
    first_course,
    second_course
ORDER BY
    transition_count DESC,
    first_course ASC,
    second_course ASC;
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
- [819. Most Common Word](../../0501-1000/0819-most-common-word/)
- [3527. Find the Most Common Response](../../3501-4000/3527-find-the-most-common-response/)
- [4066. Maximum Equal Adjacent Pairs After at Most One Replacement](../../4001-4500/4066-maximum-equal-adjacent-pairs-after-at-most-one-replacement/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/most-common-course-pairs/)
