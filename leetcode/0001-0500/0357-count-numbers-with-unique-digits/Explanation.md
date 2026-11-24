# LeetCode 357: Count Numbers with Unique Digits

**LeetCode Problem #357 — Count Numbers with Unique Digits**
Solve LeetCode Count Numbers with Unique Digits using Python and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Numbers with Unique Digits |
| LeetCode | #357 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an integer `n`, return the count of all numbers with unique digits, `x`, where `0 <= x < 10^n`.

## Constraints
- `0 <= n <= 8`

## Examples
### Example 1
- **Input:** `n = 2`
- **Output:** `91`
- **Explanation:** The answer should be the total numbers in the range of 0 &le; x < 100, excluding 11,22,33,44,55,66,77,88,99

### Example 2
- **Input:** `n = 0`
- **Output:** `1`

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Count Numbers with Unique Digits**, we observe the problem requirements and utilize the **Math & Logic** technique. We iterate through the inputs using **Mathematical Simulation & Modular Arithmetic**, leveraging a **Primitive Types** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Primitive Types**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 2`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `91`.
4. **Verification:** The answer should be the total numbers in the range of 0 &le; x < 100, excluding 11,22,33,44,55,66,77,88,99

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
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        total = 10        # k = 0 and k = 1: the numbers 0..9
        unique = 9        # count of k-digit numbers with unique digits
        avail = 9         # choices for the next digit
        for _ in range(2, n + 1):
            unique *= avail
            total += unique
            avail -= 1
        return total
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
- [828. Count Unique Characters of All Substrings of a Given String](../../0501-1000/0828-count-unique-characters-of-all-substrings-of-a-given-string/)
- [3483. Unique 3-Digit Even Numbers](../../3001-3500/3483-unique-3-digit-even-numbers/)
- [315. Count of Smaller Numbers After Self](../../0001-0500/0315-count-of-smaller-numbers-after-self/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-numbers-with-unique-digits/)
