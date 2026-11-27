# LeetCode 2889: Reshape Data: Pivot

**LeetCode Problem #2889 — Reshape Data: Pivot**
Solve LeetCode Reshape Data: Pivot using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Reshape Data: Pivot |
| LeetCode | #2889 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
DataFrame `weather`
+-------------+--------+
| Column Name | Type |
+-------------+--------+
| city | object |
| month | object |
| temperature | int |
+-------------+--------+

Write a solution to **pivot** the data so that each row represents temperatures for a specific month, and each city is a separate column.

The result format is in the following example.

## Examples
### Example 1
- **Input:** `+--------------+----------+-------------+
| city | month | temperature |
+--------------+----------+-------------+
| Jacksonville | January | 13 |
| Jacksonville | February | 23 |
| Jacksonville | March | 38 |
| Jacksonville | April | 5 |
| Jacksonville | May | 34 |
| ElPaso | January | 20 |
| ElPaso | February | 6 |
| ElPaso | March | 26 |
| ElPaso | April | 2 |
| ElPaso | May | 43 |
+--------------+----------+-------------+`
- **Output:** `+----------+--------+--------------+
| month | ElPaso | Jacksonville |
+----------+--------+--------------+
| April | 2 | 5 |
| February | 6 | 23 |
| January | 20 | 13 |
| March | 26 | 38 |
| May | 43 | 34 |
+----------+--------+--------------+`
- **Explanation:** The table is pivoted, each column represents a city, and each row represents a specific month.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Reshape Data: Pivot**, we observe the problem requirements and utilize the **Tree & Graph** technique. We decompose the problem into overlapping subproblems using a **Tree / Graph / Grid**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `+--------------+----------+-------------+
| city | month | temperature |
+--------------+----------+-------------+
| Jacksonville | January | 13 |
| Jacksonville | February | 23 |
| Jacksonville | March | 38 |
| Jacksonville | April | 5 |
| Jacksonville | May | 34 |
| ElPaso | January | 20 |
| ElPaso | February | 6 |
| ElPaso | March | 26 |
| ElPaso | April | 2 |
| ElPaso | May | 43 |
+--------------+----------+-------------+`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `+----------+--------+--------------+
| month | ElPaso | Jacksonville |
+----------+--------+--------------+
| April | 2 | 5 |
| February | 6 | 23 |
| January | 20 | 13 |
| March | 26 | 38 |
| May | 43 | 34 |
+----------+--------+--------------+`.
4. **Verification:** The table is pivoted, each column represents a city, and each row represents a specific month.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for DP Table / Array.

## Pattern
**Dynamic Programming**

## Topics
- Dynamic Programming
- Memoization
- State Transition

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    return weather.pivot(
        index="month",
        columns="city",
        values="temperature"
    )
```

## Why This Works
By utilizing **Dynamic Programming**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Incorrect base case initialization.
2. Flawed state transition equation.
3. Storing unnecessary state leading to Memory Limit Exceeded (MLE).

## Interview Notes
- **Tests:** Subproblem decomposition, state transition logic, and space optimization.
- **Follow-up:** Can space complexity be reduced from $O(n^2)$ to $O(n)$ or $O(1)$?

## Related Problems
- [2888. Reshape Data: Concatenate](../../2501-3000/2888-reshape-data-concatenate/)
- [2890. Reshape Data: Melt](../../2501-3000/2890-reshape-data-melt/)
- [724. Find Pivot Index](../../0501-1000/0724-find-pivot-index/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/reshape-data-pivot/)
