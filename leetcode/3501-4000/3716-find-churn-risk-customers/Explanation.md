# LeetCode 3716: Find Churn Risk Customers

**LeetCode Problem #3716 — Find Churn Risk Customers**
Solve LeetCode Find Churn Risk Customers using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Churn Risk Customers |
| LeetCode | #3716 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Table: `subscription_events`

+------------------+---------+
| Column Name | Type | 
+------------------+---------+
| event_id | int |
| user_id | int |
| event_date | date |
| event_type | varchar |
| plan_name | varchar |
| monthly_amount | decimal |
+------------------+---------+
event_id is the unique identifier for this table.
event_type can be start, upgrade, downgrade, or cancel.
plan_name can be basic, standard, premium, or NULL (when event_type is cancel).
monthly_amount represents the monthly subscription cost after this event.
For cancel events, monthly_amount is 0.

Write a solution to **Find Churn Risk Customers** - users who show warning signs before churning. A user is considered churn risk customer if they meet ALL the following criteria:

Currently have an **active subscription** (their last event is not cancel). 
 Have performed **at least one** downgrade in their subscription history. 
 Their **current plan revenue** is less than `50%` of their historical maximum plan revenue. 
 Have been a subscriber for **at least** `60` days.

Return *the result table ordered by* `days_as_subscriber` *in **descending** order, then by* `user_id` *in **ascending** order*.

The result format is in the following example.

## Examples
Consider the standard input for **Find Churn Risk Customers**. Applying **Two Pointer Convergence & Scanning** yields the target result step by step.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Find Churn Risk Customers**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

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

def find_churn_risk_customers(
    subscription_events: pd.DataFrame
) -> pd.DataFrame:

    df = subscription_events.copy()

    # Make sure event_date is datetime
    df['event_date'] = pd.to_datetime(df['event_date'])

    # Sort events chronologically for each user
    df = df.sort_values(
        ['user_id', 'event_date', 'event_id']
    )

    # Aggregate user-level information
    stats = df.groupby('user_id').agg(
        first_date=('event_date', 'min'),
        last_date=('event_date', 'max'),
        max_historical_amount=('monthly_amount', 'max'),
        downgrade_count=(
            'event_type',
            lambda x: (x == 'downgrade').sum()
        ),
        last_event=('event_type', 'last'),
        current_plan=('plan_name', 'last'),
        current_monthly_amount=('monthly_amount', 'last')
    ).reset_index()

    # Days as subscriber
    stats['days_as_subscriber'] = (
        stats['last_date'] - stats['first_date']
    ).dt.days

    # Currently active
    active = stats['last_event'] != 'cancel'

    # Has at least one downgrade
    has_downgrade = stats['downgrade_count'] >= 1

    # Current revenue < 50% of historical maximum
    revenue_drop = (
        stats['current_monthly_amount']
        < 0.5 * stats['max_historical_amount']
    )

    # Subscriber for at least 60 days
    long_enough = stats['days_as_subscriber'] >= 60

    # Apply all conditions
    result = stats[
        active &
        has_downgrade &
        revenue_drop &
        long_enough
    ].copy()

    # Required columns
    result = result[
        [
            'user_id',
            'current_plan',
            'current_monthly_amount',
            'max_historical_amount',
            'days_as_subscriber'
        ]
    ]

    # Required ordering
    result = result.sort_values(
        ['days_as_subscriber', 'user_id'],
        ascending=[False, True]
    ).reset_index(drop=True)

    return result
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
- [3657. Find Loyal Customers](../../3501-4000/3657-find-loyal-customers/)
- [3705. Find Golden Hour Customers](../../3501-4000/3705-find-golden-hour-customers/)
- [28. Find the Index of the First Occurrence in a String](../../0001-0500/0028-find-the-index-of-the-first-occurrence-in-a-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-churn-risk-customers/)
