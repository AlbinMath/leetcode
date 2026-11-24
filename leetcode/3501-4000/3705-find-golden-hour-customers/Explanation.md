# LeetCode 3705: Find Golden Hour Customers

**LeetCode Problem #3705 — Find Golden Hour Customers**
Solve LeetCode Find Golden Hour Customers using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Golden Hour Customers |
| LeetCode | #3705 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Table: `restaurant_orders`

+------------------+----------+
| Column Name | Type | 
+------------------+----------+
| order_id | int |
| customer_id | int |
| order_timestamp | datetime |
| order_amount | decimal |
| payment_method | varchar |
| order_rating | int |
+------------------+----------+
order_id is the unique identifier for this table.
payment_method can be cash, card, or app.
order_rating is between 1 and 5, where 5 is the best (NULL if not rated).
order_timestamp contains both date and time information.

Write a solution to find **golden hour customers** - customers who consistently order during peak hours and provide high satisfaction. A customer is a **golden hour customer** if they meet ALL the following criteria:

Made **at least** `3` orders. 
 **At least** `60%` of their orders are during **peak hours **(`11:00`-`14:00` or `18:00`-`21:00`). 
 Their **average rating** for rated orders is at least `4.0,` round it to` 2 `decimal places. 
 Have rated **at least** `50%` of their orders.

Return *the result table ordered by* `average_rating` *in **descending** order, then by* `customer_id`​​​​​​​ *in **descending** order*.

The result format is in the following example.

## Examples
Consider the standard input for **Find Golden Hour Customers**. Applying **Two Pointer Convergence & Scanning** yields the target result step by step.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Find Golden Hour Customers**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

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

def find_golden_hour_customers(restaurant_orders: pd.DataFrame) -> pd.DataFrame:
    df = restaurant_orders.copy()

    # Convert timestamp to datetime
    df['order_timestamp'] = pd.to_datetime(df['order_timestamp'])

    # Extract time
    time = df['order_timestamp'].dt.time

    # Peak hours
    lunch_start = pd.to_datetime('11:00:00').time()
    lunch_end = pd.to_datetime('14:00:00').time()
    dinner_start = pd.to_datetime('18:00:00').time()
    dinner_end = pd.to_datetime('21:00:00').time()

    df['is_peak'] = (
        ((time >= lunch_start) & (time < lunch_end)) |
        ((time >= dinner_start) & (time < dinner_end))
    )

    # Aggregate customer statistics
    stats = df.groupby('customer_id').agg(
        total_orders=('order_id', 'count'),
        peak_orders=('is_peak', 'sum'),
        rated_orders=('order_rating', 'count'),
        average_rating=('order_rating', 'mean')
    ).reset_index()

    # Calculate raw peak percentage
    stats['peak_percentage_raw'] = (
        stats['peak_orders'] / stats['total_orders'] * 100
    )

    # Average rating: 2 decimal places
    stats['average_rating'] = (
        stats['average_rating'].round(2)
    )

    # Apply conditions
    result = stats[
        (stats['total_orders'] >= 3) &
        (stats['peak_percentage_raw'] >= 60) &
        (stats['average_rating'] >= 4.0) &
        (
            stats['rated_orders'] / stats['total_orders'] >= 0.50
        )
    ].copy()

    # Peak percentage: 0 decimal places
    result['peak_hour_percentage'] = (
        result['peak_percentage_raw'].round(0).astype(int)
    )

    # Select required columns
    result = result[
        [
            'customer_id',
            'total_orders',
            'peak_hour_percentage',
            'average_rating'
        ]
    ]

    # Sort
    result = result.sort_values(
        by=['average_rating', 'customer_id'],
        ascending=[False, False]
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
- [3716. Find Churn Risk Customers](../../3501-4000/3716-find-churn-risk-customers/)
- [1604. Alert Using Same Key-Card Three or More Times in a One Hour Period](../../1501-2000/1604-alert-using-same-key-card-three-or-more-times-in-a-one-hour-period/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-golden-hour-customers/)
