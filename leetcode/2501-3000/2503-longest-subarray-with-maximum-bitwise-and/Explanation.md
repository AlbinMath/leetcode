# LeetCode 2419: Longest Subarray With Maximum Bitwise AND

**LeetCode Problem #2419 — Longest Subarray With Maximum Bitwise AND**
Solve LeetCode Longest Subarray With Maximum Bitwise AND using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest Subarray With Maximum Bitwise AND |
| LeetCode | #2419 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums` of size `n`.

Consider a **non-empty** subarray from `nums` that has the **maximum** possible **bitwise AND**.

In other words, let `k` be the maximum value of the bitwise AND of **any** subarray of `nums`. Then, only subarrays with a bitwise AND equal to `k` should be considered.

Return *the length of the **longest** such subarray*.

The bitwise AND of an array is the bitwise AND of all the numbers in it.

A **subarray** is a contiguous sequence of elements within an array.

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^6`

## Examples
### Example 1
- **Input:** `nums = [1,2,3,3,2,2]`
- **Output:** `2`
- **Explanation:** The maximum possible bitwise AND of a subarray is 3.
The longest subarray with that value is [3,3], so we return 2.

### Example 2
- **Input:** `nums = [1,2,3,4]`
- **Output:** `1`
- **Explanation:** The maximum possible bitwise AND of a subarray is 4.
The longest subarray with that value is [4], so we return 1.

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Longest Subarray With Maximum Bitwise AND**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,3,3,2,2]`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** The maximum possible bitwise AND of a subarray is 3.
The longest subarray with that value is [3,3], so we return 2.

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
from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        m = max(nums)
        best = cur = 0
        for v in nums:
            if v == m:
                cur += 1
                best = max(best, cur)
            else:
                cur = 0
        return best
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
- [2044. Count Number of Maximum Bitwise-OR Subsets](../../2001-2500/2170-count-number-of-maximum-bitwise-or-subsets/)
- [2411. Smallest Subarrays With Maximum Bitwise OR](../../2001-2500/2498-smallest-subarrays-with-maximum-bitwise-or/)
- [3171. Find Subarray With Bitwise OR Closest to K](../../3001-3500/3436-find-subarray-with-bitwise-or-closest-to-k/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/)
