# LeetCode 1507: Reformat Date

**LeetCode Problem #1507 — Reformat Date**
Solve LeetCode Reformat Date using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Reformat Date |
| LeetCode | #1507 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a `date` string in the form `Day Month Year`, where:

`Day` is in the set `{"1st", "2nd", "3rd", "4th", ..., "30th", "31st"}`. 
 `Month` is in the set `{"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"}`. 
 `Year` is in the range `[1900, 2100]`.

Convert the date string to the format `YYYY-MM-DD`, where:

`YYYY` denotes the 4 digit year. 
 `MM` denotes the 2 digit month. 
 `DD` denotes the 2 digit day.

## Constraints
- The given dates are guaranteed to be valid, so no error handling is necessary.

## Examples
### Example 1
- **Input:** `date = "20th Oct 2052"`
- **Output:** `"2052-10-20"`

### Example 2
- **Input:** `date = "6th Jun 1933"`
- **Output:** `"1933-06-06"`

### Example 3
- **Input:** `date = "26th May 1960"`
- **Output:** `"1960-05-26"`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Reformat Date**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `date = "20th Oct 2052"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"2052-10-20"`.

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
class Solution:
    def reformatDate(self, date: str) -> str:
        months = {
            "Jan": "01", "Feb": "02", "Mar": "03",
            "Apr": "04", "May": "05", "Jun": "06",
            "Jul": "07", "Aug": "08", "Sep": "09",
            "Oct": "10", "Nov": "11", "Dec": "12"
        }

        day, month, year = date.split()
        day = day[:-2]

        return f"{year}-{months[month]}-{day.zfill(2)}"
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
- [1164. Product Price at a Given Date](../../1001-1500/1278-product-price-at-a-given-date/)
- [1484. Group Sold Products By The Date](../../1501-2000/1625-group-sold-products-by-the-date/)
- [1179. Reformat Department Table](../../1001-1500/1301-reformat-department-table/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/reformat-date/)
