# LeetCode 949: Largest Time for Given Digits

**LeetCode Problem #949 — Largest Time for Given Digits**
Solve LeetCode Largest Time for Given Digits using Python and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Largest Time for Given Digits |
| LeetCode | #949 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an array `arr` of 4 digits, find the latest 24-hour time that can be made using each digit **exactly once**.

24-hour times are formatted as `"HH:MM"`, where `HH` is between `00` and `23`, and `MM` is between `00` and `59`. The earliest 24-hour time is `00:00`, and the latest is `23:59`.

Return *the latest 24-hour time in `"HH:MM"` format*. If no valid time can be made, return an empty string.

## Constraints
- `arr.length == 4`
- `0 <= arr[i] <= 9`

## Examples
### Example 1
- **Input:** `arr = [1,2,3,4]`
- **Output:** `"23:41"`
- **Explanation:** The valid 24-hour times are "12:34", "12:43", "13:24", "13:42", "14:23", "14:32", "21:34", "21:43", "23:14", and "23:41". Of these times, "23:41" is the latest.

### Example 2
- **Input:** `arr = [5,5,5,5]`
- **Output:** `""`
- **Explanation:** There are no valid 24-hour times as "55:55" is not valid.

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Largest Time for Given Digits**, we observe the problem requirements and utilize the **Math & Logic** technique. We iterate through the inputs using **Mathematical Simulation & Modular Arithmetic**, leveraging a **Primitive Types** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Primitive Types**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `arr = [1,2,3,4]`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"23:41"`.
4. **Verification:** The valid 24-hour times are "12:34", "12:43", "13:24", "13:42", "14:23", "14:32", "21:34", "21:43", "23:14", and "23:41". Of these times, "23:41" is the latest.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Primitive Types.

## Pattern
**Math & Logic**

## Topics
- Math
- Simulation

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List
from itertools import permutations

class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        best = -1
        for a, b, c, d in permutations(arr):
            h = a * 10 + b
            m = c * 10 + d
            if h < 24 and m < 60:
                best = max(best, h * 60 + m)
        if best < 0:
            return ""
        return f"{best // 60:02d}:{best % 60:02d}"
```

## Why This Works
By utilizing **Math & Logic**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1736. Latest Time by Replacing Hidden Digits](../../1501-2000/1858-latest-time-by-replacing-hidden-digits/)
- [1450. Number of Students Doing Homework at a Given Time](../../1501-2000/1560-number-of-students-doing-homework-at-a-given-time/)
- [84. Largest Rectangle in Histogram](../../0001-0500/0084-largest-rectangle-in-histogram/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/largest-time-for-given-digits/)
