# LeetCode 2890: Reshape Data: Melt

**LeetCode Problem #2890 — Reshape Data: Melt**
Solve LeetCode Reshape Data: Melt using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Reshape Data: Melt |
| LeetCode | #2890 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
DataFrame `report`
+-------------+--------+
| Column Name | Type |
+-------------+--------+
| product | object |
| quarter_1 | int |
| quarter_2 | int |
| quarter_3 | int |
| quarter_4 | int |
+-------------+--------+

Write a solution to **reshape** the data so that each row represents sales data for a product in a specific quarter.

The result format is in the following example.

## Examples
### Example 1
- **Input:** `+-------------+-----------+-----------+-----------+-----------+
| product | quarter_1 | quarter_2 | quarter_3 | quarter_4 |
+-------------+-----------+-----------+-----------+-----------+
| Umbrella | 417 | 224 | 379 | 611 |
| SleepingBag | 800 | 936 | 93 | 875 |
+-------------+-----------+-----------+-----------+-----------+`
- **Output:** `+-------------+-----------+-------+
| product | quarter | sales |
+-------------+-----------+-------+
| Umbrella | quarter_1 | 417 |
| SleepingBag | quarter_1 | 800 |
| Umbrella | quarter_2 | 224 |
| SleepingBag | quarter_2 | 936 |
| Umbrella | quarter_3 | 379 |
| SleepingBag | quarter_3 | 93 |
| Umbrella | quarter_4 | 611 |
| SleepingBag | quarter_4 | 875 |
+-------------+-----------+-------+`
- **Explanation:** The DataFrame is reshaped from wide to long format. Each row represents the sales of a product in a quarter.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Reshape Data: Melt**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We decompose the problem into overlapping subproblems using a **Integer Bitmask**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `+-------------+-----------+-----------+-----------+-----------+
| product | quarter_1 | quarter_2 | quarter_3 | quarter_4 |
+-------------+-----------+-----------+-----------+-----------+
| Umbrella | 417 | 224 | 379 | 611 |
| SleepingBag | 800 | 936 | 93 | 875 |
+-------------+-----------+-----------+-----------+-----------+`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `+-------------+-----------+-------+
| product | quarter | sales |
+-------------+-----------+-------+
| Umbrella | quarter_1 | 417 |
| SleepingBag | quarter_1 | 800 |
| Umbrella | quarter_2 | 224 |
| SleepingBag | quarter_2 | 936 |
| Umbrella | quarter_3 | 379 |
| SleepingBag | quarter_3 | 93 |
| Umbrella | quarter_4 | 611 |
| SleepingBag | quarter_4 | 875 |
+-------------+-----------+-------+`.
4. **Verification:** The DataFrame is reshaped from wide to long format. Each row represents the sales of a product in a quarter.

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

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    return report.melt(
        id_vars=["product"],
        var_name="quarter",
        value_name="sales"
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
- [2889. Reshape Data: Pivot](../../2501-3000/2889-reshape-data-pivot/)
- [566. Reshape the Matrix](../../0501-1000/0566-reshape-the-matrix/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/reshape-data-melt/)
