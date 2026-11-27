# LeetCode 738: Monotone Increasing Digits

**LeetCode Problem #738 — Monotone Increasing Digits**
Solve LeetCode Monotone Increasing Digits using Python and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Monotone Increasing Digits |
| LeetCode | #738 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
An integer has **monotone increasing digits** if and only if each pair of adjacent digits `x` and `y` satisfy `x <= y`.

Given an integer `n`, return *the largest number that is less than or equal to *`n`* with **monotone increasing digits***.

## Constraints
- `0 <= n <= 10^9`

## Examples
### Example 1
- **Input:** `n = 10`
- **Output:** `9`

### Example 2
- **Input:** `n = 1234`
- **Output:** `1234`

### Example 3
- **Input:** `n = 332`
- **Output:** `299`

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Monotone Increasing Digits**, we observe the problem requirements and utilize the **Math & Logic** technique. We iterate through the inputs using **Mathematical Simulation & Modular Arithmetic**, leveraging a **Primitive Types** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Primitive Types**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 10`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `9`.

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
class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        d = list(str(n))
        mark = len(d)  # first index to be filled with '9'
        for i in range(len(d) - 1, 0, -1):
            if d[i - 1] > d[i]:
                d[i - 1] = str(int(d[i - 1]) - 1)
                mark = i
        for i in range(mark, len(d)):
            d[i] = '9'
        return int(''.join(d))
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
- [926. Flip String to Monotone Increasing](../../0501-1000/0926-flip-string-to-monotone-increasing/)
- [300. Longest Increasing Subsequence](../../0001-0500/0300-longest-increasing-subsequence/)
- [329. Longest Increasing Path in a Matrix](../../0001-0500/0329-longest-increasing-path-in-a-matrix/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/monotone-increasing-digits/)
