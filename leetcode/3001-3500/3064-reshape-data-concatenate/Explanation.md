# LeetCode 2888: Reshape Data: Concatenate

**LeetCode Problem #2888 — Reshape Data: Concatenate**
Solve LeetCode Reshape Data: Concatenate using Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Reshape Data: Concatenate |
| LeetCode | #2888 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
DataFrame `df1`
+-------------+--------+
| Column Name | Type |
+-------------+--------+
| student_id | int |
| name | object |
| age | int |
+-------------+--------+

DataFrame `df2`
+-------------+--------+
| Column Name | Type |
+-------------+--------+
| student_id | int |
| name | object |
| age | int |
+-------------+--------+

Write a solution to concatenate these two DataFrames **vertically** into one DataFrame.

The result format is in the following example.

## Examples
Consider the standard input for **Reshape Data: Concatenate**. Applying **Stack Push / Pop Parsing** yields the target result step by step.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Reshape Data: Concatenate**, we observe the problem requirements and utilize the **Stack & Queue** technique. We decompose the problem into overlapping subproblems using a **Stack**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
Applying **Stack Push / Pop Parsing** step by step to the input yields the expected result.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    return pd.concat([df1, df2], axis=0, ignore_index=True)
```

## Why This Works
By utilizing **Stack & Queue**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [2889. Reshape Data: Pivot](../../3001-3500/3072-reshape-data-pivot/)
- [2890. Reshape Data: Melt](../../3001-3500/3073-reshape-data-melt/)
- [566. Reshape the Matrix](../../0501-1000/0566-reshape-the-matrix/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/reshape-data-concatenate/)
