# LeetCode 2437: Number of Valid Clock Times

**LeetCode Problem #2437 — Number of Valid Clock Times**
Solve LeetCode Number of Valid Clock Times using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Valid Clock Times |
| LeetCode | #2437 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string of length `5` called `time`, representing the current time on a digital clock in the format `"hh:mm"`. The **earliest** possible time is `"00:00"` and the **latest** possible time is `"23:59"`.

In the string `time`, the digits represented by the `?` symbol are **unknown**, and must be **replaced** with a digit from `0` to `9`.

Return* an integer *`answer`*, the number of valid clock times that can be created by replacing every *`?`* with a digit from *`0`* to *`9`.

## Constraints
- `time` is a valid string of length `5` in the format `"hh:mm"`.
- `"00" <= hh <= "23"`
- `"00" <= mm <= "59"`
- Some of the digits might be replaced with `'?'` and need to be replaced with digits from `0` to `9`.

## Examples
### Example 1
- **Input:** `time = "?5:00"`
- **Output:** `2`
- **Explanation:** We can replace the ? with either a 0 or 1, producing "05:00" or "15:00". Note that we cannot replace it with a 2, since the time "25:00" is invalid. In total, we have two choices.

### Example 2
- **Input:** `time = "0?:0?"`
- **Output:** `100`
- **Explanation:** Each ? can be replaced by any digit from 0 to 9, so we have 100 total choices.

### Example 3
- **Input:** `time = "??:??"`
- **Output:** `1440`
- **Explanation:** There are 24 possible choices for the hours, and 60 possible choices for the minutes. In total, we have 24 * 60 = 1440 choices.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Number of Valid Clock Times**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `time = "?5:00"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** We can replace the ? with either a 0 or 1, producing "05:00" or "15:00". Note that we cannot replace it with a 2, since the time "25:00" is invalid. In total, we have two choices.

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
class Solution(object):
    def countTime(self, time):
        h1, h2, _, m1, m2 = time

        if h1 == '?' and h2 == '?':
            hours = 24
        elif h1 == '?':
            hours = 3 if h2 <= '3' else 2
        elif h2 == '?':
            hours = 4 if h1 == '2' else 10
        else:
            hours = 1

        minutes = (6 if m1 == '?' else 1) * (10 if m2 == '?' else 1)
        return hours * minutes
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
- [1375. Number of Times Binary String Is Prefix-Aligned](../../1001-1500/1375-number-of-times-binary-string-is-prefix-aligned/)
- [65. Valid Number](../../0001-0500/0065-valid-number/)
- [611. Valid Triangle Number](../../0501-1000/0611-valid-triangle-number/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-valid-clock-times/)
