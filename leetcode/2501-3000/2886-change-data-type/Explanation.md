# LeetCode 2886: Change Data Type

**LeetCode Problem #2886 — Change Data Type**
Solve LeetCode Change Data Type using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Change Data Type |
| LeetCode | #2886 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
DataFrame `students`
+-------------+--------+
| Column Name | Type |
+-------------+--------+
| student_id | int |
| name | object |
| age | int |
| grade | float |
+-------------+--------+

Write a solution to correct the errors:

The `grade` column is stored as floats, convert it to integers.

The result format is in the following example.

## Examples
### Example 1
- **Input:** `DataFrame students:
+------------+------+-----+-------+
| student_id | name | age | grade |
+------------+------+-----+-------+
| 1 | Ava | 6 | 73.0 |
| 2 | Kate | 15 | 87.0 |
+------------+------+-----+-------+`
- **Output:** `+------------+------+-----+-------+
| student_id | name | age | grade |
+------------+------+-----+-------+
| 1 | Ava | 6 | 73 |
| 2 | Kate | 15 | 87 |
+------------+------+-----+-------+`
- **Explanation:** The data types of the column grade is converted to int.

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Change Data Type**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `DataFrame students:
+------------+------+-----+-------+
| student_id | name | age | grade |
+------------+------+-----+-------+
| 1 | Ava | 6 | 73.0 |
| 2 | Kate | 15 | 87.0 |
+------------+------+-----+-------+`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `+------------+------+-----+-------+
| student_id | name | age | grade |
+------------+------+-----+-------+
| 1 | Ava | 6 | 73 |
| 2 | Kate | 15 | 87 |
+------------+------+-----+-------+`.
4. **Verification:** The data types of the column grade is converted to int.

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

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students["grade"] = students["grade"].astype(int)
    return students
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
- [1320. Minimum Distance to Type a Word Using Two Fingers](../../1001-1500/1320-minimum-distance-to-type-a-word-using-two-fingers/)
- [1935. Maximum Number of Words You Can Type](../../1501-2000/1935-maximum-number-of-words-you-can-type/)
- [1974. Minimum Time to Type Word Using Special Typewriter](../../1501-2000/1974-minimum-time-to-type-word-using-special-typewriter/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/change-data-type/)
