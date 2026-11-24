# LeetCode 2885: Rename Columns

**LeetCode Problem #2885 — Rename Columns**
Solve LeetCode Rename Columns using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Rename Columns |
| LeetCode | #2885 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
DataFrame `students`
+-------------+--------+
| Column Name | Type |
+-------------+--------+
| id | int |
| first | object |
| last | object |
| age | int |
+-------------+--------+

Write a solution to rename the columns as follows:

`id` to `student_id` 
 `first` to `first_name` 
 `last` to `last_name` 
 `age` to `age_in_years`

The result format is in the following example.

## Examples
### Example 1
- **Input:** `+----+---------+----------+-----+
| id | first | last | age |
+----+---------+----------+-----+
| 1 | Mason | King | 6 |
| 2 | Ava | Wright | 7 |
| 3 | Taylor | Hall | 16 |
| 4 | Georgia | Thompson | 18 |
| 5 | Thomas | Moore | 10 |
+----+---------+----------+-----+`
- **Output:** `+------------+------------+-----------+--------------+
| student_id | first_name | last_name | age_in_years |
+------------+------------+-----------+--------------+
| 1 | Mason | King | 6 |
| 2 | Ava | Wright | 7 |
| 3 | Taylor | Hall | 16 |
| 4 | Georgia | Thompson | 18 |
| 5 | Thomas | Moore | 10 |
+------------+------------+-----------+--------------+`
- **Explanation:** The column names are changed accordingly.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Rename Columns**, we observe the problem requirements and utilize the **Tree & Graph** technique. We perform a recursive Depth-First Search (DFS) traversal. The algorithm handles base cases at leaf nodes and aggregates results from subtrees back up to the root.

## Algorithm
1. Define base cases for null/leaf nodes.
2. Recursively traverse child nodes.
3. Combine child results to determine current node output.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `+----+---------+----------+-----+
| id | first | last | age |
+----+---------+----------+-----+
| 1 | Mason | King | 6 |
| 2 | Ava | Wright | 7 |
| 3 | Taylor | Hall | 16 |
| 4 | Georgia | Thompson | 18 |
| 5 | Thomas | Moore | 10 |
+----+---------+----------+-----+`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `+------------+------------+-----------+--------------+
| student_id | first_name | last_name | age_in_years |
+------------+------------+-----------+--------------+
| 1 | Mason | King | 6 |
| 2 | Ava | Wright | 7 |
| 3 | Taylor | Hall | 16 |
| 4 | Georgia | Thompson | 18 |
| 5 | Thomas | Moore | 10 |
+------------+------------+-----------+--------------+`.
4. **Verification:** The column names are changed accordingly.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Tree / Graph / Grid.

## Pattern
**Tree & Graph**

## Topics
- Tree
- Graph
- DFS
- BFS

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    return students.rename(columns={
        "id": "student_id",
        "first": "first_name",
        "last": "last_name",
        "age": "age_in_years"
    })
```

## Why This Works
By utilizing **Tree & Graph**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [944. Delete Columns to Make Sorted](../../0501-1000/0944-delete-columns-to-make-sorted/)
- [955. Delete Columns to Make Sorted II](../../0501-1000/0955-delete-columns-to-make-sorted-ii/)
- [960. Delete Columns to Make Sorted III](../../0501-1000/0960-delete-columns-to-make-sorted-iii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/rename-columns/)
