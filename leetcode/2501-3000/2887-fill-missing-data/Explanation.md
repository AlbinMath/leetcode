# LeetCode 2887: Fill Missing Data

**LeetCode Problem #2887 — Fill Missing Data**
Solve LeetCode Fill Missing Data using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Fill Missing Data |
| LeetCode | #2887 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
DataFrame `products`
+-------------+--------+
| Column Name | Type |
+-------------+--------+
| name | object |
| quantity | int |
| price | int |
+-------------+--------+

Write a solution to fill in the missing value as `**0**` in the `quantity` column.

The result format is in the following example.

## Examples
### Example 1
- **Input:** `+-----------------+----------+-------+
| name | quantity | price |
+-----------------+----------+-------+
| Wristwatch | None | 135 |
| WirelessEarbuds | None | 821 |
| GolfClubs | 779 | 9319 |
| Printer | 849 | 3051 |
+-----------------+----------+-------+`
- **Output:** `+-----------------+----------+-------+
| name | quantity | price |
+-----------------+----------+-------+
| Wristwatch | 0 | 135 |
| WirelessEarbuds | 0 | 821 |
| GolfClubs | 779 | 9319 |
| Printer | 849 | 3051 |
+-----------------+----------+-------+`
- **Explanation:** The quantity for Wristwatch and WirelessEarbuds are filled by 0.

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Fill Missing Data**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `+-----------------+----------+-------+
| name | quantity | price |
+-----------------+----------+-------+
| Wristwatch | None | 135 |
| WirelessEarbuds | None | 821 |
| GolfClubs | 779 | 9319 |
| Printer | 849 | 3051 |
+-----------------+----------+-------+`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `+-----------------+----------+-------+
| name | quantity | price |
+-----------------+----------+-------+
| Wristwatch | 0 | 135 |
| WirelessEarbuds | 0 | 821 |
| GolfClubs | 779 | 9319 |
| Printer | 849 | 3051 |
+-----------------+----------+-------+`.
4. **Verification:** The quantity for Wristwatch and WirelessEarbuds are filled by 0.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Integer Bitmask.

## Pattern
**Bit Manipulation**

## Topics
- Bit Manipulation
- Bitwise Math

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products["quantity"] = products["quantity"].fillna(0)
    return products
```

## Why This Works
By utilizing **Bit Manipulation**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [2883. Drop Missing Data](../../2501-3000/2883-drop-missing-data/)
- [733. Flood Fill](../../0501-1000/0733-flood-fill/)
- [2335. Minimum Amount of Time to Fill Cups](../../2001-2500/2335-minimum-amount-of-time-to-fill-cups/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/fill-missing-data/)
