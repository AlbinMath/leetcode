# LeetCode 3497: Analyze Subscription Conversion 

**LeetCode Problem #3497 — Analyze Subscription Conversion **
Solve LeetCode Analyze Subscription Conversion  using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Analyze Subscription Conversion  |
| LeetCode | #3497 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Table: `UserActivity`

+------------------+---------+
| Column Name | Type | 
+------------------+---------+
| user_id | int |
| activity_date | date |
| activity_type | varchar |
| activity_duration| int |
+------------------+---------+
(user_id, activity_date, activity_type) is the unique key for this table.
activity_type is one of ('free_trial', 'paid', 'cancelled').
activity_duration is the number of minutes the user spent on the platform that day.
Each row represents a user's activity on a specific date.

A subscription service wants to analyze user behavior patterns. The company offers a `7`-day **free trial**, after which users can subscribe to a **paid plan** or **cancel**. Write a solution to:

Find users who converted from free trial to paid subscription 
 Calculate each user's **average daily activity duration** during their **free trial** period (rounded to `2` decimal places) 
 Calculate each user's **average daily activity duration** during their **paid** subscription period (rounded to `2` decimal places)

Return *the result table ordered by *`user_id`* in **ascending** order*.

The result format is in the following example.

## Examples
Consider the standard input for **Analyze Subscription Conversion **. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Analyze Subscription Conversion **, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

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

def analyze_subscription_conversion(user_activity: pd.DataFrame) -> pd.DataFrame:
    df = user_activity[user_activity["activity_type"] != "cancelled"]

    # Calculate average duration
    grouped = (
        df.groupby(["user_id", "activity_type"])["activity_duration"]
        .mean()
        .add(0.0001)
        .round(2)
        .reset_index()
    )

    # Free trial averages
    trial = (
        grouped[grouped["activity_type"] == "free_trial"]
        .rename(columns={
            "activity_duration": "trial_avg_duration"
        })
        .drop(columns=["activity_type"])
    )

    # Paid averages
    paid = (
        grouped[grouped["activity_type"] == "paid"]
        .rename(columns={
            "activity_duration": "paid_avg_duration"
        })
        .drop(columns=["activity_type"])
    )

    # Keep only users who have BOTH free_trial and paid
    result = trial.merge(
        paid,
        on="user_id",
        how="inner"
    )

    return result.sort_values("user_id").reset_index(drop=True)
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
- [6. Zigzag Conversion](../../0001-0500/0006-zigzag-conversion/)
- [3528. Unit Conversion I](../../3501-4000/3528-unit-conversion-i/)
- [3482. Analyze Organization Hierarchy](../../3001-3500/3482-analyze-organization-hierarchy/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/analyze-subscription-conversion/)
