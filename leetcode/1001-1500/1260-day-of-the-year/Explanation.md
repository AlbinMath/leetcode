# LeetCode 1154: Day of the Year

**LeetCode Problem #1154 — Day of the Year**
Solve LeetCode Day of the Year using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Day of the Year |
| LeetCode | #1154 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a string `date` representing a Gregorian calendar date formatted as `YYYY-MM-DD`, return *the day number of the year*.

## Constraints
- `date.length == 10`
- `date[4] == date[7] == '-'`, and all other `date[i]`'s are digits
- `date` represents a calendar date between Jan 1^st, 1900 and Dec 31^st, 2019.

## Examples
### Example 1
- **Input:** `date = "2019-01-09"`
- **Output:** `9`
- **Explanation:** Given date is the 9th day of the year in 2019.

### Example 2
- **Input:** `date = "2019-02-10"`
- **Output:** `41`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Day of the Year**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `date = "2019-01-09"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `9`.
4. **Verification:** Given date is the 9th day of the year in 2019.

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
    def dayOfYear(self, date: str) -> int:
        current_date = datetime.strptime(date, "%Y-%m-%d")
        start_date = datetime(current_date.year, 1, 1)

        return (current_date - start_date).days + 1
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
- [1185. Day of the Week](../../1001-1500/1289-day-of-the-week/)
- [1970. Last Day Where You Can Still Cross](../../2001-2500/2101-last-day-where-you-can-still-cross/)
- [1854. Maximum Population Year](../../1501-2000/1983-maximum-population-year/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/day-of-the-year/)
