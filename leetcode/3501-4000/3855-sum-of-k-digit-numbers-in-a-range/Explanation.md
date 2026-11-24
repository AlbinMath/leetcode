# LeetCode 3855: Sum of K-Digit Numbers in a Range

**LeetCode Problem #3855 — Sum of K-Digit Numbers in a Range**
Solve LeetCode Sum of K-Digit Numbers in a Range using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Sum of K-Digit Numbers in a Range |
| LeetCode | #3855 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given three integers `l`, `r`, and `k`.

Consider all possible integers consisting of **exactly** `k` digits, where each digit is chosen independently from the integer range `[l, r]` (inclusive). If 0 is included in the range, leading zeros are allowed.

Return an integer representing the sum of all such numbers. ​​​​​​​ Since the answer may be very large, return it **modulo** `10^9 + 7`.

## Constraints
- `0 <= l <= r <= 9`
- `1 <= k <= 10^9`

## Examples
### Example 1
- **Input:** `l = 1, r = 2, k = 2`
- **Output:** `66`
- **Explanation:** All numbers formed using `k = 2` digits in the range `[1, 2]` are `11, 12, 21, 22`. 
 The total sum is `11 + 12 + 21 + 22 = 66`.

### Example 2
- **Input:** `l = 0, r = 1, k = 3`
- **Output:** `444`
- **Explanation:** All numbers formed using `k = 3` digits in the range `[0, 1]` are `000, 001, 010, 011, 100, 101, 110, 111`​​​​​​​. 
 These numbers without leading zeros are `0, 1, 10, 11, 100, 101, 110, 111`. 
 The total sum is 444.

### Example 3
- **Input:** `l = 5, r = 5, k = 10`
- **Output:** `555555520`
- **Explanation:** ​​​​​​​ 

 
 5555555555 is the only valid number consisting of `k = 10` digits in the range `[5, 5]`. 
 The total sum is `5555555555 % (10^9 + 7) = 555555520`.

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Sum of K-Digit Numbers in a Range**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `l = 1, r = 2, k = 2`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `66`.
4. **Verification:** All numbers formed using `k = 2` digits in the range `[1, 2]` are `11, 12, 21, 22`. 
 The total sum is `11 + 12 + 21 + 22 = 66`.

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
class Solution:
    def sumOfNumbers(self, l, r, k):
        MOD = 10**9 + 7
        c = r - l + 1
        S = (l + r) * c // 2
        rep = (pow(10, k, MOD) - 1) * pow(9, MOD - 2, MOD) % MOD
        return S % MOD * pow(c, k - 1, MOD) % MOD * rep % MOD
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
- [2310. Sum of Numbers With Units Digit K](../../2001-2500/2310-sum-of-numbers-with-units-digit-k/)
- [3954. Sum of Compatible Numbers in Range I](../../3501-4000/3954-sum-of-compatible-numbers-in-range-i/)
- [2081. Sum of k-Mirror Numbers](../../2001-2500/2081-sum-of-k-mirror-numbers/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/sum-of-k-digit-numbers-in-a-range/)
