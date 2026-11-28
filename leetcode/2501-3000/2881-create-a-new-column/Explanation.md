# LeetCode 2881: Create a New Column

**LeetCode Problem #2881 — Create a New Column**
Solve LeetCode Create a New Column using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Create a New Column |
| LeetCode | #2881 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
DataFrame `employees`
+-------------+--------+
| Column Name | Type. |
+-------------+--------+
| name | object |
| salary | int. |
+-------------+--------+

A company plans to provide its employees with a bonus.

Write a solution to create a new column name `bonus` that contains the **doubled values** of the `salary` column.

The result format is in the following example.

## Examples
### Example 1
- **Input:** `DataFrame employees
+---------+--------+
| name | salary |
+---------+--------+
| Piper | 4548 |
| Grace | 28150 |
| Georgia | 1103 |
| Willow | 6593 |
| Finn | 74576 |
| Thomas | 24433 |
+---------+--------+`
- **Output:** `+---------+--------+--------+
| name | salary | bonus |
+---------+--------+--------+
| Piper | 4548 | 9096 |
| Grace | 28150 | 56300 |
| Georgia | 1103 | 2206 |
| Willow | 6593 | 13186 |
| Finn | 74576 | 149152 |
| Thomas | 24433 | 48866 |
+---------+--------+--------+`
- **Explanation:** A new column bonus is created by doubling the value in the column salary.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Create a New Column**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `DataFrame employees
+---------+--------+
| name | salary |
+---------+--------+
| Piper | 4548 |
| Grace | 28150 |
| Georgia | 1103 |
| Willow | 6593 |
| Finn | 74576 |
| Thomas | 24433 |
+---------+--------+`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `+---------+--------+--------+
| name | salary | bonus |
+---------+--------+--------+
| Piper | 4548 | 9096 |
| Grace | 28150 | 56300 |
| Georgia | 1103 | 2206 |
| Willow | 6593 | 13186 |
| Finn | 74576 | 149152 |
| Thomas | 24433 | 48866 |
+---------+--------+--------+`.
4. **Verification:** A new column bonus is created by doubling the value in the column salary.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees["bonus"] = employees["salary"] * 2
    return employees
```

## Why This Works
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [168. Excel Sheet Column Title](../../0001-0500/0168-excel-sheet-column-title/)
- [171. Excel Sheet Column Number](../../0001-0500/0171-excel-sheet-column-number/)
- [947. Most Stones Removed with Same Row or Column](../../0501-1000/0947-most-stones-removed-with-same-row-or-column/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/create-a-new-column/)
