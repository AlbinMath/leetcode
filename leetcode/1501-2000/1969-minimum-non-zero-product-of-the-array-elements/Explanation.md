# LeetCode 1969: Minimum Non-Zero Product of the Array Elements

**LeetCode Problem #1969 — Minimum Non-Zero Product of the Array Elements**
Solve LeetCode Minimum Non-Zero Product of the Array Elements using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Non-Zero Product of the Array Elements |
| LeetCode | #1969 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a positive integer `p`. Consider an array `nums` (**1-indexed**) that consists of the integers in the **inclusive** range `[1, 2^p - 1]` in their binary representations. You are allowed to do the following operation **any** number of times:

Choose two elements `x` and `y` from `nums`. 
 Choose a bit in `x` and swap it with its corresponding bit in `y`. Corresponding bit refers to the bit that is in the **same position** in the other integer.

For example, if `x = 11 0 1` and `y = 00 1 1`, after swapping the `2^nd` bit from the right, we have `x = 11 1 1` and `y = 00 0 1`.

Find the **minimum non-zero** product of `nums` after performing the above operation **any** number of times. Return *this product** **modulo** *`10^9 + 7`.

**Note:** The answer should be the minimum product **before** the modulo operation is done.

## Constraints
- `1 <= p <= 60`

## Examples
### Example 1
- **Input:** `p = 1`
- **Output:** `1`
- **Explanation:** nums = [1].
There is only one element, so the product equals that element.

### Example 2
- **Input:** `p = 2`
- **Output:** `6`
- **Explanation:** nums = [01, 10, 11].
Any swap would either make the product 0 or stay the same.
Thus, the array product of 1 * 2 * 3 = 6 is already minimized.

### Example 3
- **Input:** `p = 3`
- **Output:** `1512`
- **Explanation:** nums = [001, 010, 011, 100, 101, 110, 111]
- In the first operation we can swap the leftmost bit of the second and fifth elements.
 - The resulting array is [001, 1 10, 011, 100, 0 01, 110, 111].
- In the second operation we can swap the middle bit of the third and fourth elements.
 - The resulting array is [001, 110, 0 0 1, 1 1 0, 001, 110, 111].
The array product is 1 * 6 * 1 * 6 * 1 * 6 * 7 = 1512, which is the minimum possible product.

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Non-Zero Product of the Array Elements**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `p = 1`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** nums = [1].
There is only one element, so the product equals that element.

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
    def minNonZeroProduct(self, p: int) -> int:
        MOD = 10**9 + 7
        top = (1 << p) - 1
        return top % MOD * pow(top - 1, (1 << (p - 1)) - 1, MOD) % MOD
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
- [3495. Minimum Operations to Make Array Elements Zero](../../3001-3500/3495-minimum-operations-to-make-array-elements-zero/)
- [3354. Make Array Elements Equal to Zero](../../3001-3500/3354-make-array-elements-equal-to-zero/)
- [3542. Minimum Operations to Convert All Elements to Zero](../../3501-4000/3542-minimum-operations-to-convert-all-elements-to-zero/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-non-zero-product-of-the-array-elements/)
