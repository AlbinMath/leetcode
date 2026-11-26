# LeetCode 2879: Display the First Three Rows

**LeetCode Problem #2879 — Display the First Three Rows**
Solve LeetCode Display the First Three Rows using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Display the First Three Rows |
| LeetCode | #2879 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
DataFrame: `employees`
+-------------+--------+
| Column Name | Type |
+-------------+--------+
| employee_id | int |
| name | object |
| department | object |
| salary | int |
+-------------+--------+

Write a solution to display the **first `3` **rows** **of this DataFrame.

## Examples
### Example 1
- **Input:** `DataFrame employees
+-------------+-----------+-----------------------+--------+
| employee_id | name | department | salary |
+-------------+-----------+-----------------------+--------+
| 3 | Bob | Operations | 48675 |
| 90 | Alice | Sales | 11096 |
| 9 | Tatiana | Engineering | 33805 |
| 60 | Annabelle | InformationTechnology | 37678 |
| 49 | Jonathan | HumanResources | 23793 |
| 43 | Khaled | Administration | 40454 |
+-------------+-----------+-----------------------+--------+`
- **Output:** `+-------------+---------+-------------+--------+
| employee_id | name | department | salary |
+-------------+---------+-------------+--------+
| 3 | Bob | Operations | 48675 |
| 90 | Alice | Sales | 11096 |
| 9 | Tatiana | Engineering | 33805 |
+-------------+---------+-------------+--------+`
- **Explanation:** Only the first 3 rows are displayed.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Display the First Three Rows**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `DataFrame employees
+-------------+-----------+-----------------------+--------+
| employee_id | name | department | salary |
+-------------+-----------+-----------------------+--------+
| 3 | Bob | Operations | 48675 |
| 90 | Alice | Sales | 11096 |
| 9 | Tatiana | Engineering | 33805 |
| 60 | Annabelle | InformationTechnology | 37678 |
| 49 | Jonathan | HumanResources | 23793 |
| 43 | Khaled | Administration | 40454 |
+-------------+-----------+-----------------------+--------+`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `+-------------+---------+-------------+--------+
| employee_id | name | department | salary |
+-------------+---------+-------------+--------+
| 3 | Bob | Operations | 48675 |
| 90 | Alice | Sales | 11096 |
| 9 | Tatiana | Engineering | 33805 |
+-------------+---------+-------------+--------+`.
4. **Verification:** Only the first 3 rows are displayed.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)
```

## Why This Works
By utilizing **Array / General**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1072. Flip Columns For Maximum Number of Equal Rows](../../1001-1500/1072-flip-columns-for-maximum-number-of-equal-rows/)
- [1337. The K Weakest Rows in a Matrix](../../1001-1500/1337-the-k-weakest-rows-in-a-matrix/)
- [1439. Find the Kth Smallest Sum of a Matrix With Sorted Rows](../../1001-1500/1439-find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/display-the-first-three-rows/)
