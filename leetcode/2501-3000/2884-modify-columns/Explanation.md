# LeetCode 2884: Modify Columns

**LeetCode Problem #2884 — Modify Columns**
Solve LeetCode Modify Columns using Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Modify Columns |
| LeetCode | #2884 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
DataFrame `employees`
+-------------+--------+
| Column Name | Type |
+-------------+--------+
| name | object |
| salary | int |
+-------------+--------+

A company intends to give its employees a pay rise.

Write a solution to **modify** the `salary` column by multiplying each salary by 2.

The result format is in the following example.

## Examples
### Example 1
- **Input:** `DataFrame employees
+---------+--------+
| name | salary |
+---------+--------+
| Jack | 19666 |
| Piper | 74754 |
| Mia | 62509 |
| Ulysses | 54866 |
+---------+--------+`
- **Output:** `+---------+--------+
| name | salary |
+---------+--------+
| Jack | 39332 |
| Piper | 149508 |
| Mia | 125018 |
| Ulysses | 109732 |
+---------+--------+`
- **Explanation:** Every salary has been doubled.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Modify Columns**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `DataFrame employees
+---------+--------+
| name | salary |
+---------+--------+
| Jack | 19666 |
| Piper | 74754 |
| Mia | 62509 |
| Ulysses | 54866 |
+---------+--------+`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `+---------+--------+
| name | salary |
+---------+--------+
| Jack | 39332 |
| Piper | 149508 |
| Mia | 125018 |
| Ulysses | 109732 |
+---------+--------+`.
4. **Verification:** Every salary has been doubled.

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

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees["salary"] = employees["salary"] * 2
    return employees
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
- [944. Delete Columns to Make Sorted](../../0501-1000/0944-delete-columns-to-make-sorted/)
- [955. Delete Columns to Make Sorted II](../../0501-1000/0955-delete-columns-to-make-sorted-ii/)
- [960. Delete Columns to Make Sorted III](../../0501-1000/0960-delete-columns-to-make-sorted-iii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/modify-columns/)
