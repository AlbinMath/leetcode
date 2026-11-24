# LeetCode 2871: Split Array Into Maximum Number of Subarrays

**LeetCode Problem #2871 — Split Array Into Maximum Number of Subarrays**
Solve LeetCode Split Array Into Maximum Number of Subarrays using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Split Array Into Maximum Number of Subarrays |
| LeetCode | #2871 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array `nums` consisting of **non-negative** integers.

We define the score of subarray `nums[l..r]` such that `l <= r` as `nums[l] AND nums[l + 1] AND ... AND nums[r]` where **AND** is the bitwise `AND` operation.

Consider splitting the array into one or more subarrays such that the following conditions are satisfied:

**E****ach** element of the array belongs to **exactly** one subarray. 
 The sum of scores of the subarrays is the **minimum** possible.

Return *the **maximum** number of subarrays in a split that satisfies the conditions above.*

A **subarray** is a contiguous part of an array.

## Constraints
- `1 <= nums.length <= 10^5`
- `0 <= nums[i] <= 10^6`

## Examples
### Example 1
- **Input:** `nums = [1,0,2,0,1,2]`
- **Output:** `3`
- **Explanation:** We can split the array into the following subarrays:
- [1,0]. The score of this subarray is 1 AND 0 = 0.
- [2,0]. The score of this subarray is 2 AND 0 = 0.
- [1,2]. The score of this subarray is 1 AND 2 = 0.
The sum of scores is 0 + 0 + 0 = 0, which is the minimum possible score that we can obtain.
It can be shown that we cannot split the array into more than 3 subarrays with a total score of 0. So we return 3.

### Example 2
- **Input:** `nums = [5,7,1,3]`
- **Output:** `1`
- **Explanation:** We can split the array into one subarray: [5,7,1,3] with a score of 1, which is the minimum possible score that we can obtain.
It can be shown that we cannot split the array into more than 1 subarray with a total score of 1. So we return 1.

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Split Array Into Maximum Number of Subarrays**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,0,2,0,1,2]`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** We can split the array into the following subarrays:
- [1,0]. The score of this subarray is 1 AND 0 = 0.
- [2,0]. The score of this subarray is 2 AND 0 = 0.
- [1,2]. The score of this subarray is 1 AND 2 = 0.
The sum of scores is 0 + 0 + 0 = 0, which is the minimum possible score that we can obtain.
It can be shown that we cannot split the array into more than 3 subarrays with a total score of 0. So we return 3.

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
    def maxSubarrays(self, nums):
        total = nums[0]
        for x in nums:
            total &= x
        if total != 0:
            return 1

        count = 0
        cur = -1  # all bits set
        for x in nums:
            cur &= x
            if cur == 0:
                count += 1
                cur = -1
        return count
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
- [1712. Ways to Split Array Into Three Subarrays](../../1501-2000/1712-ways-to-split-array-into-three-subarrays/)
- [842. Split Array into Fibonacci Sequence](../../0501-1000/0842-split-array-into-fibonacci-sequence/)
- [1593. Split a String Into the Max Number of Unique Substrings](../../1501-2000/1593-split-a-string-into-the-max-number-of-unique-substrings/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/split-array-into-maximum-number-of-subarrays/)
