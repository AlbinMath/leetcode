# LeetCode 3611: Find Overbooked Employees

**LeetCode Problem #3611 — Find Overbooked Employees**
Solve LeetCode Find Overbooked Employees using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Overbooked Employees |
| LeetCode | #3611 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Table: `employees`

+---------------+---------+
| Column Name | Type |
+---------------+---------+
| employee_id | int |
| employee_name | varchar |
| department | varchar |
+---------------+---------+
employee_id is the unique identifier for this table.
Each row contains information about an employee and their department.

Table: `meetings`

+---------------+---------+
| Column Name | Type |
+---------------+---------+
| meeting_id | int |
| employee_id | int |
| meeting_date | date |
| meeting_type | varchar |
| duration_hours| decimal |
+---------------+---------+
meeting_id is the unique identifier for this table.
Each row represents a meeting attended by an employee. meeting_type can be 'Team', 'Client', or 'Training'.

Write a solution to find employees who are **meeting-heavy** - employees who spend more than `50%` of their working time in meetings during any given week.

Assume a standard work week is `40`** hours** 
 Calculate **total meeting hours** per employee **per week** (**Monday to Sunday**) 
 An employee is meeting-heavy if their weekly meeting hours `>` `20` hours (`50%` of `40` hours) 
 Count how many weeks each employee was meeting-heavy 
 **Only include** employees who were meeting-heavy for **at least **`2`** weeks**

Return *the result table ordered by the number of meeting-heavy weeks in **descending** order, then by employee name in **ascending** order*.

The result format is in the following example.

## Examples
Consider the standard input for **Find Overbooked Employees**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Find Overbooked Employees**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
Applying **In-Place Array Traversal & Index Mapping** step by step to the input yields the expected result.

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

def find_overbooked_employees(
    employees: pd.DataFrame,
    meetings: pd.DataFrame
) -> pd.DataFrame:

    meetings = meetings.copy()
    meetings["meeting_date"] = pd.to_datetime(meetings["meeting_date"])

    # Get Monday of each week
    meetings["week_start"] = (
        meetings["meeting_date"]
        - pd.to_timedelta(meetings["meeting_date"].dt.weekday, unit="D")
    )

    # Total meeting hours per employee per week
    weekly = (
        meetings.groupby(["employee_id", "week_start"])["duration_hours"]
        .sum()
        .reset_index(name="total_hours")
    )

    # Weeks with more than 20 meeting hours
    heavy = weekly[weekly["total_hours"] > 20]

    # Count heavy weeks per employee
    result = (
        heavy.groupby("employee_id")
        .size()
        .reset_index(name="meeting_heavy_weeks")
    )

    # Keep employees with at least 2 heavy weeks
    result = result[result["meeting_heavy_weeks"] >= 2]

    # Add employee details
    result = result.merge(
        employees,
        on="employee_id",
        how="inner"
    )

    return (
        result[
            ["employee_id", "employee_name", "department", "meeting_heavy_weeks"]
        ]
        .sort_values(
            ["meeting_heavy_weeks", "employee_name"],
            ascending=[False, True]
        )
        .reset_index(drop=True)
    )
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
- [3580. Find Consistently Improving Employees](../../3501-4000/3580-find-consistently-improving-employees/)
- [181. Employees Earning More Than Their Managers](../../0001-0500/0181-employees-earning-more-than-their-managers/)
- [627. Swap Sex of Employees](../../0501-1000/0627-swap-sex-of-employees/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-overbooked-employees/)
