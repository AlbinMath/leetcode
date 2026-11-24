# LeetCode 3688: Bitwise OR of Even Numbers in an Array

**LeetCode Problem #3688 — Bitwise OR of Even Numbers in an Array**
Solve LeetCode Bitwise OR of Even Numbers in an Array using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Bitwise OR of Even Numbers in an Array |
| LeetCode | #3688 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums`.

Return the bitwise **OR** of all **even** numbers in the array.

If there are no even numbers in `nums`, return 0.

## Constraints
- `1 <= nums.length <= 100`
- `1 <= nums[i] <= 100`

## Examples
### Example 1
- **Input:** `nums = [1,2,3,4,5,6]`
- **Output:** `6`
- **Explanation:** The even numbers are 2, 4, and 6. Their bitwise OR equals 6.

### Example 2
- **Input:** `nums = [7,9,11]`
- **Output:** `0`
- **Explanation:** There are no even numbers, so the result is 0.

### Example 3
- **Input:** `nums = [1,8,16]`
- **Output:** `24`
- **Explanation:** The even numbers are 8 and 16. Their bitwise OR equals 24.

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Bitwise OR of Even Numbers in an Array**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,3,4,5,6]`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `6`.
4. **Verification:** The even numbers are 2, 4, and 6. Their bitwise OR equals 6.

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
    def evenNumberBitwiseORs(self, nums):
        res = 0
        for x in nums:
            if x % 2 == 0:
                res |= x
        return res
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
- [985. Sum of Even Numbers After Queries](../../0501-1000/0985-sum-of-even-numbers-after-queries/)
- [1295. Find Numbers with Even Number of Digits](../../1001-1500/1295-find-numbers-with-even-number-of-digits/)
- [2094. Finding 3-Digit Even Numbers](../../2001-2500/2094-finding-3-digit-even-numbers/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/bitwise-or-of-even-numbers-in-an-array/)
