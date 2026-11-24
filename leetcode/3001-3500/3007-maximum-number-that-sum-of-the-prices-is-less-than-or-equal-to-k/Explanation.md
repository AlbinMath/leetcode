# LeetCode 3007: Maximum Number That Sum of the Prices Is Less Than or Equal to K

**LeetCode Problem #3007 — Maximum Number That Sum of the Prices Is Less Than or Equal to K**
Solve LeetCode Maximum Number That Sum of the Prices Is Less Than or Equal to K using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Number That Sum of the Prices Is Less Than or Equal to K |
| LeetCode | #3007 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer `k` and an integer `x`. The price of a number `num` is calculated by the count of set bits at positions `x`, `2x`, `3x`, etc., in its binary representation, starting from the least significant bit. The following table contains examples of how price is calculated.

x 
 num 
 Binary Representation 
 Price 
 
 
 1 
 13 
 0 0 0 0 0 ** 1 **** 1 ** 0 ** 1 ** 
 3 
 
 
 2 
 13 
 0 0 0 0 0** 1 **1 0 1 
 1 
 
 
 2 
 233 
 0** 1 **1** 1 **0** 1 **0 0 1 
 3 
 
 
 3 
 13 
 0 00 0 01** 1 **01 
 1 
 
 
 3 
 362 
 ** 1 **01** 1 **01 0 10 
 2

The **accumulated price** of `num` is the total price of numbers from `1` to `num`. `num` is considered **cheap** if its accumulated price is less than or equal to `k`.

Return the greatest cheap number.

## Constraints
- `1 <= k <= 10^15`
- `1 <= x <= 8`

## Examples
### Example 1
- **Input:** `k = 9, x = 1`
- **Output:** `6`
- **Explanation:** As shown in the table below, `6` is the greatest cheap number. 

 
 
 
 x 
 num 
 Binary Representation 
 Price 
 Accumulated Price 
 
 
 1 
 1 
 0 0

### Example 2
- **Input:** `k = 7, x = 2`
- **Output:** `9`
- **Explanation:** As shown in the table below, `9` is the greatest cheap number. 

 
 
 
 x 
 num 
 Binary Representation 
 Price 
 Accumulated Price 
 
 
 2 
 1 
 0 0 0 1 
 0 
 0 
 
 
 2 
 2 
 0 0

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Number That Sum of the Prices Is Less Than or Equal to K**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `k = 9, x = 1`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `6`.
4. **Verification:** As shown in the table below, `6` is the greatest cheap number. 

 
 
 
 x 
 num 
 Binary Representation 
 Price 
 Accumulated Price 
 
 
 1 
 1 
 0 0

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
class Solution(object):
    def findMaximumNumber(self, k, x):
        def price(num):
            n = num + 1
            total = 0
            p = x
            while p <= 61:
                b = p - 1
                full = (n >> (b + 1)) << b
                rem = n & ((1 << (b + 1)) - 1)
                total += full + max(0, rem - (1 << b))
                p += x
            return total

        lo, hi = 0, 1 << 60
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if price(mid) <= k:
                lo = mid
            else:
                hi = mid - 1
        return lo
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
- [1292. Maximum Side Length of a Square with Sum Less than or Equal to Threshold](../../1001-1500/1292-maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/)
- [1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold](../../1001-1500/1343-number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/)
- [2311. Longest Binary Subsequence Less Than or Equal to K](../../2001-2500/2311-longest-binary-subsequence-less-than-or-equal-to-k/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-number-that-sum-of-the-prices-is-less-than-or-equal-to-k/)
