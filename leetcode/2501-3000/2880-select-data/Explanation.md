# LeetCode 2880: Select Data

**LeetCode Problem #2880 — Select Data**
Solve LeetCode Select Data using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Select Data |
| LeetCode | #2880 |
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

Write a solution to select the name and age of the student with `student_id = 101`.

The result format is in the following example.

## Examples
Consider the standard input for **Select Data**. Applying **Bitwise Masking & Bit Shift** yields the target result step by step.

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Select Data**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
Applying **Bitwise Masking & Bit Shift** step by step to the input yields the expected result.

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

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students[students["student_id"] == 101][["name", "age"]]
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
- [2222. Number of Ways to Select Buildings](../../2001-2500/2222-number-of-ways-to-select-buildings/)
- [3276. Select Cells in Grid With Maximum Score](../../3001-3500/3276-select-cells-in-grid-with-maximum-score/)
- [3458. Select K Disjoint Special Substrings](../../3001-3500/3458-select-k-disjoint-special-substrings/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/select-data/)
