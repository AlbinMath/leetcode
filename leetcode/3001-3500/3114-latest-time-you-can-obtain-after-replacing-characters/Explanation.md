# LeetCode 3114: Latest Time You Can Obtain After Replacing Characters

**LeetCode Problem #3114 — Latest Time You Can Obtain After Replacing Characters**
Solve LeetCode Latest Time You Can Obtain After Replacing Characters using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Latest Time You Can Obtain After Replacing Characters |
| LeetCode | #3114 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string `s` representing a 12-hour format time where some of the digits (possibly none) are replaced with a `"?"`.

12-hour times are formatted as `"HH:MM"`, where `HH` is between `00` and `11`, and `MM` is between `00` and `59`. The earliest 12-hour time is `00:00`, and the latest is `11:59`.

You have to replace **all** the `"?"` characters in `s` with digits such that the time we obtain by the resulting string is a **valid** 12-hour format time and is the **latest** possible.

Return *the resulting string*.

## Constraints
- `s.length == 5`
- `s[2]` is equal to the character `":"`.
- All characters except `s[2]` are digits or `"?"` characters.
- The input is generated such that there is **at least** one time between `"00:00"` and `"11:59"` that you can obtain after replacing the `"?"` characters.

## Examples
### Example 1
- **Input:** `s = "1?:?4"`
- **Output:** `"11:54"`
- **Explanation:** The latest 12-hour format time we can achieve by replacing `"?"` characters is `"11:54"`.

### Example 2
- **Input:** `s = "0?:5?"`
- **Output:** `"09:59"`
- **Explanation:** The latest 12-hour format time we can achieve by replacing `"?"` characters is `"09:59"`.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Latest Time You Can Obtain After Replacing Characters**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "1?:?4"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"11:54"`.
4. **Verification:** The latest 12-hour format time we can achieve by replacing `"?"` characters is `"11:54"`.

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
    def findLatestTime(self, s: str) -> str:
        for h in range(11, -1, -1):
            for m in range(59, -1, -1):
                t = f"{h:02d}:{m:02d}"
                if all(p == '?' or p == c for p, c in zip(s, t)):
                    return t
        return ""
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
- [1736. Latest Time by Replacing Hidden Digits](../../1501-2000/1736-latest-time-by-replacing-hidden-digits/)
- [1423. Maximum Points You Can Obtain from Cards](../../1001-1500/1423-maximum-points-you-can-obtain-from-cards/)
- [2332. The Latest Time to Catch a Bus](../../2001-2500/2332-the-latest-time-to-catch-a-bus/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/latest-time-you-can-obtain-after-replacing-characters/)
