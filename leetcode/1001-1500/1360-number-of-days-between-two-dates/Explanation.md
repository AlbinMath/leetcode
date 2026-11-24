# LeetCode 1360: Number of Days Between Two Dates

**LeetCode Problem #1360 — Number of Days Between Two Dates**
Solve LeetCode Number of Days Between Two Dates using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Days Between Two Dates |
| LeetCode | #1360 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Write a program to count the number of days between two dates.

The two dates are given as strings, their format is `YYYY-MM-DD` as shown in the examples.

## Constraints
- The given dates are valid dates between the years `1971` and `2100`.

## Examples
### Example 1
- **Input:** `date1 = "2019-06-29", date2 = "2019-06-30"`
- **Output:** `1`

### Example 2
- **Input:** `date1 = "2020-01-15", date2 = "2019-12-31"`
- **Output:** `15`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Number of Days Between Two Dates**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `date1 = "2019-06-29", date2 = "2019-06-30"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.

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
from datetime import datetime

class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        d1 = datetime.strptime(date1, "%Y-%m-%d").date()
        d2 = datetime.strptime(date2, "%Y-%m-%d").date()

        return abs((d1 - d2).days)
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
- [1347. Minimum Number of Steps to Make Two Strings Anagram](../../1001-1500/1347-minimum-number-of-steps-to-make-two-strings-anagram/)
- [1385. Find the Distance Value Between Two Arrays](../../1001-1500/1385-find-the-distance-value-between-two-arrays/)
- [1467. Probability of a Two Boxes Having The Same Number of Distinct Balls](../../1001-1500/1467-probability-of-a-two-boxes-having-the-same-number-of-distinct-balls/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-days-between-two-dates/)
