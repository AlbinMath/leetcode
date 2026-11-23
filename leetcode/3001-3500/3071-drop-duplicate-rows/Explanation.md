# LeetCode 2882: Drop Duplicate Rows

**LeetCode Problem #2882 — Drop Duplicate Rows**
Solve LeetCode Drop Duplicate Rows using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Drop Duplicate Rows |
| LeetCode | #2882 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
DataFrame customers
+-------------+--------+
| Column Name | Type |
+-------------+--------+
| customer_id | int |
| name | object |
| email | object |
+-------------+--------+

There are some duplicate rows in the DataFrame based on the `email` column.

Write a solution to remove these duplicate rows and keep only the **first** occurrence.

The result format is in the following example.

## Examples
### Example 1
- **Input:** `+-------------+---------+---------------------+
| customer_id | name | email |
+-------------+---------+---------------------+
| 1 | Ella | emily@example.com |
| 2 | David | michael@example.com |
| 3 | Zachary | sarah@example.com |
| 4 | Alice | john@example.com |
| 5 | Finn | john@example.com |
| 6 | Violet | alice@example.com |
+-------------+---------+---------------------+`
- **Output:** `+-------------+---------+---------------------+
| customer_id | name | email |
+-------------+---------+---------------------+
| 1 | Ella | emily@example.com |
| 2 | David | michael@example.com |
| 3 | Zachary | sarah@example.com |
| 4 | Alice | john@example.com |
| 6 | Violet | alice@example.com |
+-------------+---------+---------------------+`
- **Explanation:** Alic (customer_id = 4) and Finn (customer_id = 5) both use john@example.com, so only the first occurrence of this email is retained.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Drop Duplicate Rows**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `+-------------+---------+---------------------+
| customer_id | name | email |
+-------------+---------+---------------------+
| 1 | Ella | emily@example.com |
| 2 | David | michael@example.com |
| 3 | Zachary | sarah@example.com |
| 4 | Alice | john@example.com |
| 5 | Finn | john@example.com |
| 6 | Violet | alice@example.com |
+-------------+---------+---------------------+`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `+-------------+---------+---------------------+
| customer_id | name | email |
+-------------+---------+---------------------+
| 1 | Ella | emily@example.com |
| 2 | David | michael@example.com |
| 3 | Zachary | sarah@example.com |
| 4 | Alice | john@example.com |
| 6 | Violet | alice@example.com |
+-------------+---------+---------------------+`.
4. **Verification:** Alic (customer_id = 4) and Finn (customer_id = 5) both use john@example.com, so only the first occurrence of this email is retained.

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

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.drop_duplicates(subset=["email"], keep="first")
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
- [2883. Drop Missing Data](../../3001-3500/3075-drop-missing-data/)
- [1072. Flip Columns For Maximum Number of Equal Rows](../../1001-1500/1147-flip-columns-for-maximum-number-of-equal-rows/)
- [1337. The K Weakest Rows in a Matrix](../../1001-1500/1463-the-k-weakest-rows-in-a-matrix/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/drop-duplicate-rows/)
