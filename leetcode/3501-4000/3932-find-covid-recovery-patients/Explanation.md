# LeetCode 3586: Find COVID Recovery Patients

**LeetCode Problem #3586 — Find COVID Recovery Patients**
Solve LeetCode Find COVID Recovery Patients using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find COVID Recovery Patients |
| LeetCode | #3586 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Table: `patients`

+-------------+---------+
| Column Name | Type |
+-------------+---------+
| patient_id | int |
| patient_name| varchar |
| age | int |
+-------------+---------+
patient_id is the unique identifier for this table.
Each row contains information about a patient.

Table: `covid_tests`

+-------------+---------+
| Column Name | Type |
+-------------+---------+
| test_id | int |
| patient_id | int |
| test_date | date |
| result | varchar |
+-------------+---------+
test_id is the unique identifier for this table.
Each row represents a COVID test result. The result can be Positive, Negative, or Inconclusive.

Write a solution to find patients who have **recovered from COVID** - patients who tested positive but later tested negative.

A patient is considered recovered if they have **at least one** **Positive** test followed by at least one **Negative** test on a **later date** 
 Calculate the **recovery time** in days as the **difference** between the **first positive test** and the **first negative test** after that **positive test** 
 **Only include** patients who have both positive and negative test results

Return *the result table ordered by *`recovery_time`* in **ascending** order, then by *`patient_name`* in **ascending** order*.

The result format is in the following example.

## Examples
Consider the standard input for **Find COVID Recovery Patients**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Find COVID Recovery Patients**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

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

def find_covid_recovery_patients(
    patients: pd.DataFrame,
    covid_tests: pd.DataFrame
) -> pd.DataFrame:

    # Convert test_date to datetime
    tests = covid_tests.copy()
    tests["test_date"] = pd.to_datetime(tests["test_date"])

    # First positive test for each patient
    positive = (
        tests[tests["result"] == "Positive"]
        .groupby("patient_id")["test_date"]
        .min()
        .reset_index(name="positive_date")
    )

    # Merge positive date back with all tests
    tests = tests.merge(
        positive,
        on="patient_id",
        how="inner"
    )

    # Negative tests after the first positive
    negative = tests[
        (tests["result"] == "Negative") &
        (tests["test_date"] > tests["positive_date"])
    ]

    # First negative after positive
    negative = (
        negative.groupby("patient_id")["test_date"]
        .min()
        .reset_index(name="negative_date")
    )

    # Combine positive and negative dates
    result = positive.merge(
        negative,
        on="patient_id",
        how="inner"
    )

    # Calculate recovery time
    result["recovery_time"] = (
        result["negative_date"] - result["positive_date"]
    ).dt.days

    # Add patient information
    result = result.merge(
        patients,
        on="patient_id",
        how="left"
    )

    # Required output and sorting
    return result[
        [
            "patient_id",
            "patient_name",
            "age",
            "recovery_time"
        ]
    ].sort_values(
        ["recovery_time", "patient_name"],
        ascending=[True, True]
    ).reset_index(drop=True)
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
- [1527. Patients With a Condition](../../1501-2000/1670-patients-with-a-condition/)
- [3620. Network Recovery Pathways](../../3501-4000/3919-network-recovery-pathways/)
- [28. Find the Index of the First Occurrence in a String](../../0001-0500/0028-find-the-index-of-the-first-occurrence-in-a-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-covid-recovery-patients/)
