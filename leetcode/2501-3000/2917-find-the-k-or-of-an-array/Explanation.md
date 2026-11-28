# LeetCode 2917: Find the K-or of an Array

**LeetCode Problem #2917 — Find the K-or of an Array**
Solve LeetCode Find the K-or of an Array using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find the K-or of an Array |
| LeetCode | #2917 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums`, and an integer `k`. Let's introduce **K-or** operation by extending the standard bitwise OR. In K-or, a bit position in the result is set to `1` if at least `k` numbers in `nums` have a `1` in that position.

Return *the K-or of* `nums`.

## Constraints
- `1 <= nums.length <= 50`
- `0 <= nums[i] < 2^31`
- `1 <= k <= nums.length`

## Examples
### Example 1
- **Input:** `nums = [7,12,9,8,9,15], k = 4`
- **Output:** `9`
- **Explanation:** Represent numbers in binary: 

 
 
 
 Number 
 Bit 3 
 Bit 2 
 Bit 1 
 Bit 0 
 
 
 7 
 0 
 1 
 1 
 1 
 
 
 12 
 1 
 1 
 0 
 0 
 
 
 9 
 1 
 0 
 0 
 1 
 
 
 8 
 1 
 0 
 0 
 0 
 
 
 9 
 1 
 0 
 0 
 1 
 
 
 15 
 1 
 1 
 1 
 1 
 
 
 Result = 9 
 1 
 0 
 0 
 1 
 
 
 

 Bit 0 is set in 7, 9, 9, and 15. Bit 3 is set in 12, 9, 8, 9, and 15. 
Only bits 0 and 3 qualify. The result is `(1001)_2 = 9`.

### Example 2
- **Input:** `nums = [2,12,1,11,4,5], k = 6`
- **Output:** `0`

### Example 3
- **Input:** `nums = [10,8,5,9,11,6,8], k = 1`
- **Output:** `15`
- **Explanation:** Since `k == 1`, the 1-or of the array is equal to the bitwise OR of all its elements. Hence, the answer is `10 OR 8 OR 5 OR 9 OR 11 OR 6 OR 8 = 15`.

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Find the K-or of an Array**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [7,12,9,8,9,15], k = 4`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `9`.
4. **Verification:** Represent numbers in binary: 

 
 
 
 Number 
 Bit 3 
 Bit 2 
 Bit 1 
 Bit 0 
 
 
 7 
 0 
 1 
 1 
 1 
 
 
 12 
 1 
 1 
 0 
 0 
 
 
 9 
 1 
 0 
 0 
 1 
 
 
 8 
 1 
 0 
 0 
 0 
 
 
 9 
 1 
 0 
 0 
 1 
 
 
 15 
 1 
 1 
 1 
 1 
 
 
 Result = 9 
 1 
 0 
 0 
 1 
 
 
 

 Bit 0 is set in 7, 9, 9, and 15. Bit 3 is set in 12, 9, 8, 9, and 15. 
Only bits 0 and 3 qualify. The result is `(1001)_2 = 9`.

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
    def findKOr(self, nums, k):
        res = 0
        for b in range(31):
            c = sum((x >> b) & 1 for x in nums)
            if c >= k:
                res |= 1 << b
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
- [1420. Build Array Where You Can Find The Maximum Exactly K Comparisons](../../1001-1500/1420-build-array-where-you-can-find-the-maximum-exactly-k-comparisons/)
- [2386. Find the K-Sum of an Array](../../2001-2500/2386-find-the-k-sum-of-an-array/)
- [34. Find First and Last Position of Element in Sorted Array](../../0001-0500/0034-find-first-and-last-position-of-element-in-sorted-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-the-k-or-of-an-array/)
