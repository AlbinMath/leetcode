# LeetCode 3601: Find Drivers with Improved Fuel Efficiency

**LeetCode Problem #3601 — Find Drivers with Improved Fuel Efficiency**
Solve LeetCode Find Drivers with Improved Fuel Efficiency using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Drivers with Improved Fuel Efficiency |
| LeetCode | #3601 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Table: `drivers`

+-------------+---------+
| Column Name | Type |
+-------------+---------+
| driver_id | int |
| driver_name | varchar |
+-------------+---------+
driver_id is the unique identifier for this table.
Each row contains information about a driver.

Table: `trips`

+---------------+---------+
| Column Name | Type |
+---------------+---------+
| trip_id | int |
| driver_id | int |
| trip_date | date |
| distance_km | decimal |
| fuel_consumed | decimal |
+---------------+---------+
trip_id is the unique identifier for this table.
Each row represents a trip made by a driver, including the distance traveled and fuel consumed for that trip.

Write a solution to find drivers whose **fuel efficiency has improved** by **comparing** their average fuel efficiency in the** first half** of the year with the **second half** of the year.

Calculate **fuel efficiency** as `distance_km / fuel_consumed` for **each** trip 
 **First half**: January to June, **Second half**: July to December 
 Only include drivers who have trips in **both halves** of the year 
 Calculate the **efficiency improvement** as (`second_half_avg - first_half_avg`) 
 **Round **all** **results** **to** `2` **decimal** **places

Return *the result table ordered by efficiency improvement in **descending** order, then by driver name in **ascending** order*.

The result format is in the following example.

## Examples
Consider the standard input for **Find Drivers with Improved Fuel Efficiency**. Applying **Two Pointer Convergence & Scanning** yields the target result step by step.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Find Drivers with Improved Fuel Efficiency**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

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

def find_improved_efficiency_drivers(
    drivers: pd.DataFrame,
    trips: pd.DataFrame
) -> pd.DataFrame:

    trips = trips.copy()

    # Convert date
    trips["trip_date"] = pd.to_datetime(trips["trip_date"])

    # First half = 1, Second half = 2
    trips["half"] = trips["trip_date"].dt.month.apply(
        lambda x: 1 if x <= 6 else 2
    )

    # Fuel efficiency for each trip
    trips["efficiency"] = (
        trips["distance_km"] / trips["fuel_consumed"]
    )

    # Average efficiency for each driver and half
    avg = (
        trips.groupby(["driver_id", "half"])["efficiency"]
        .mean()
        .reset_index()
    )

    # Convert halves into columns
    avg = avg.pivot(
        index="driver_id",
        columns="half",
        values="efficiency"
    )

    avg = avg.rename(columns={
        1: "first_half_avg",
        2: "second_half_avg"
    })

    # Must have trips in both halves
    avg = avg.dropna()

    # Must actually improve
    avg = avg[
        avg["second_half_avg"] > avg["first_half_avg"]
    ]

    # Improvement
    avg["efficiency_improvement"] = (
        avg["second_half_avg"] - avg["first_half_avg"]
    )

    # Round all numeric results
    avg[
        ["first_half_avg",
         "second_half_avg",
         "efficiency_improvement"]
    ] = avg[
        ["first_half_avg",
         "second_half_avg",
         "efficiency_improvement"]
    ].round(2)

    # Add driver names
    result = avg.reset_index().merge(
        drivers,
        on="driver_id",
        how="inner"
    )

    # Required order
    result = result.sort_values(
        ["efficiency_improvement", "driver_name"],
        ascending=[False, True]
    )

    return result[
        [
            "driver_id",
            "driver_name",
            "first_half_avg",
            "second_half_avg",
            "efficiency_improvement"
        ]
    ].reset_index(drop=True)
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
- [3421. Find Students Who Improved](../../3001-3500/3421-find-students-who-improved/)
- [2477. Minimum Fuel Cost to Report to the Capital](../../2001-2500/2477-minimum-fuel-cost-to-report-to-the-capital/)
- [28. Find the Index of the First Occurrence in a String](../../0001-0500/0028-find-the-index-of-the-first-occurrence-in-a-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-drivers-with-improved-fuel-efficiency/)
