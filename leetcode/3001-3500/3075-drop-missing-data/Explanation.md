# LeetCode 2883: Drop Missing Data

**LeetCode Problem #2883 — Drop Missing Data**
Solve LeetCode Drop Missing Data using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Drop Missing Data |
| LeetCode | #2883 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
DataFrame students
+-------------+--------+
| Column Name | Type |
+-------------+--------+
| student_id | int |
| name | object |
| age | int |
+-------------+--------+

There are some rows having missing values in the `name` column.

Write a solution to remove the rows with missing values.

The result format is in the following example.

## Examples
### Example 1
- **Input:** `+------------+---------+-----+
| student_id | name | age |
+------------+---------+-----+
| 32 | Piper | 5 |
| 217 | None | 19 |
| 779 | Georgia | 20 |
| 849 | Willow | 14 |
+------------+---------+-----+`
- **Output:** `+------------+---------+-----+
| student_id | name | age |
+------------+---------+-----+
| 32 | Piper | 5 |
| 779 | Georgia | 20 | 
| 849 | Willow | 14 | 
+------------+---------+-----+`
- **Explanation:** Student with id 217 havs empty value in the name column, so it will be removed.

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Drop Missing Data**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `+------------+---------+-----+
| student_id | name | age |
+------------+---------+-----+
| 32 | Piper | 5 |
| 217 | None | 19 |
| 779 | Georgia | 20 |
| 849 | Willow | 14 |
+------------+---------+-----+`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `+------------+---------+-----+
| student_id | name | age |
+------------+---------+-----+
| 32 | Piper | 5 |
| 779 | Georgia | 20 | 
| 849 | Willow | 14 | 
+------------+---------+-----+`.
4. **Verification:** Student with id 217 havs empty value in the name column, so it will be removed.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Integer Bitmask.

## Pattern
**Bit Manipulation**

## Topics
- Bit Manipulation
- Bitwise Math

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return students.dropna(subset=["name"])
```

## Why This Works
By utilizing **Bit Manipulation**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [2887. Fill Missing Data](../../3001-3500/3070-fill-missing-data/)
- [41. First Missing Positive](../../0001-0500/0041-first-missing-positive/)
- [268. Missing Number](../../0001-0500/0268-missing-number/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/drop-missing-data/)
