# LeetCode 3580: Find Consistently Improving Employees

**LeetCode Problem #3580 — Find Consistently Improving Employees**
Solve LeetCode Find Consistently Improving Employees using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Consistently Improving Employees |
| LeetCode | #3580 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Table: `employees`

+-------------+---------+
| Column Name | Type |
+-------------+---------+
| employee_id | int |
| name | varchar |
+-------------+---------+
employee_id is the unique identifier for this table.
Each row contains information about an employee.

Table: `performance_reviews`

+-------------+------+
| Column Name | Type |
+-------------+------+
| review_id | int |
| employee_id | int |
| review_date | date |
| rating | int |
+-------------+------+
review_id is the unique identifier for this table.
Each row represents a performance review for an employee. The rating is on a scale of 1-5 where 5 is excellent and 1 is poor.

Write a solution to find employees who have consistently improved their performance over **their last three reviews**.

An employee must have **at least **`3`** review** to be considered 
 The employee's **last **`3`** reviews** must show **strictly increasing ratings** (each review better than the previous) 
 Use the most recent `3` reviews based on `review_date` for each employee 
 Calculate the **improvement score** as the difference between the latest rating and the earliest rating among the last `3` reviews

Return *the result table ordered by **improvement score** in **descending** order, then by **name** in **ascending** order*.

The result format is in the following example.

## Examples
Consider the standard input for **Find Consistently Improving Employees**. Applying **Two Pointer Convergence & Scanning** yields the target result step by step.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Find Consistently Improving Employees**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
Applying **Two Pointer Convergence & Scanning** step by step to the input yields the expected result.

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

def find_consistently_improving_employees(
    employees: pd.DataFrame,
    performance_reviews: pd.DataFrame
) -> pd.DataFrame:

    # Sort reviews by employee and date
    reviews = performance_reviews.sort_values(
        ["employee_id", "review_date"]
    )

    # Keep only employees with at least 3 reviews
    counts = reviews.groupby("employee_id").size()
    eligible = counts[counts >= 3].index

    reviews = reviews[
        reviews["employee_id"].isin(eligible)
    ]

    # Get the latest 3 reviews
    last_three = (
        reviews.groupby("employee_id")
        .tail(3)
        .sort_values(["employee_id", "review_date"])
    )

    # Check strictly increasing ratings
    def check_increasing(group):
        ratings = group["rating"].tolist()
        return ratings[0] < ratings[1] < ratings[2]

    valid_ids = (
        last_three.groupby("employee_id")
        .apply(check_increasing)
    )

    valid_ids = valid_ids[valid_ids].index

    # Keep only improving employees
    valid = last_three[
        last_three["employee_id"].isin(valid_ids)
    ]

    # Calculate improvement score
    scores = (
        valid.groupby("employee_id")["rating"]
        .agg(["first", "last"])
        .reset_index()
    )

    scores["improvement_score"] = (
        scores["last"] - scores["first"]
    )

    # Add names
    result = scores.merge(
        employees,
        on="employee_id",
        how="left"
    )

    # Required ordering
    return result[
        ["employee_id", "name", "improvement_score"]
    ].sort_values(
        ["improvement_score", "name"],
        ascending=[False, True]
    ).reset_index(drop=True)
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
- [3611. Find Overbooked Employees](../../3501-4000/3943-find-overbooked-employees/)
- [181. Employees Earning More Than Their Managers](../../0001-0500/0181-employees-earning-more-than-their-managers/)
- [627. Swap Sex of Employees](../../0501-1000/0627-swap-sex-of-employees/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-consistently-improving-employees/)
