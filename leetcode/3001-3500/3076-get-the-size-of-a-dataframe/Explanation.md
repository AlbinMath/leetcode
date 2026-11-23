# LeetCode 2878: Get the Size of a DataFrame

**LeetCode Problem #2878 — Get the Size of a DataFrame**
Solve LeetCode Get the Size of a DataFrame using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Get the Size of a DataFrame |
| LeetCode | #2878 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
DataFrame `players:`
+-------------+--------+
| Column Name | Type |
+-------------+--------+
| player_id | int |
| name | object |
| age | int |
| position | object |
| ... | ... |
+-------------+--------+

Write a solution to calculate and display the **number of rows and columns** of `players`.

Return the result as an array:

`[number of rows, number of columns]`

The result format is in the following example.

## Examples
### Example 1
- **Input:** `+-----------+----------+-----+-------------+--------------------+
| player_id | name | age | position | team |
+-----------+----------+-----+-------------+--------------------+
| 846 | Mason | 21 | Forward | RealMadrid |
| 749 | Riley | 30 | Winger | Barcelona |
| 155 | Bob | 28 | Striker | ManchesterUnited |
| 583 | Isabella | 32 | Goalkeeper | Liverpool |
| 388 | Zachary | 24 | Midfielder | BayernMunich |
| 883 | Ava | 23 | Defender | Chelsea |
| 355 | Violet | 18 | Striker | Juventus |
| 247 | Thomas | 27 | Striker | ParisSaint-Germain |
| 761 | Jack | 33 | Midfielder | ManchesterCity |
| 642 | Charlie | 36 | Center-back | Arsenal |
+-----------+----------+-----+-------------+--------------------+`
- **Output:** `[10, 5]`
- **Explanation:** This DataFrame contains 10 rows and 5 columns.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Get the Size of a DataFrame**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `+-----------+----------+-----+-------------+--------------------+
| player_id | name | age | position | team |
+-----------+----------+-----+-------------+--------------------+
| 846 | Mason | 21 | Forward | RealMadrid |
| 749 | Riley | 30 | Winger | Barcelona |
| 155 | Bob | 28 | Striker | ManchesterUnited |
| 583 | Isabella | 32 | Goalkeeper | Liverpool |
| 388 | Zachary | 24 | Midfielder | BayernMunich |
| 883 | Ava | 23 | Defender | Chelsea |
| 355 | Violet | 18 | Striker | Juventus |
| 247 | Thomas | 27 | Striker | ParisSaint-Germain |
| 761 | Jack | 33 | Midfielder | ManchesterCity |
| 642 | Charlie | 36 | Center-back | Arsenal |
+-----------+----------+-----+-------------+--------------------+`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[10, 5]`.
4. **Verification:** This DataFrame contains 10 rows and 5 columns.

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

def getDataframeSize(players: pd.DataFrame):
    return list(players.shape)
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
- [2877. Create a DataFrame from List](../../3001-3500/3062-create-a-dataframe-from-list/)
- [864. Shortest Path to Get All Keys](../../0501-1000/0895-shortest-path-to-get-all-keys/)
- [1208. Get Equal Substrings Within Budget](../../1001-1500/1321-get-equal-substrings-within-budget/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/get-the-size-of-a-dataframe/)
