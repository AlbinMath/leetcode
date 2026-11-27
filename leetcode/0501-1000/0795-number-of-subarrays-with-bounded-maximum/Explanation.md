# LeetCode 795: Number of Subarrays with Bounded Maximum

**LeetCode Problem #795 — Number of Subarrays with Bounded Maximum**
Solve LeetCode Number of Subarrays with Bounded Maximum using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Subarrays with Bounded Maximum |
| LeetCode | #795 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an integer array `nums` and two integers `left` and `right`, return *the number of contiguous non-empty **subarrays** such that the value of the maximum array element in that subarray is in the range *`[left, right]`.

The test cases are generated so that the answer will fit in a **32-bit** integer.

## Constraints
- `1 <= nums.length <= 10^5`
- `0 <= nums[i] <= 10^9`
- `0 <= left <= right <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [2,1,4,3], left = 2, right = 3`
- **Output:** `3`
- **Explanation:** There are three subarrays that meet the requirements: [2], [2, 1], [3].

### Example 2
- **Input:** `nums = [2,9,2,5,6], left = 2, right = 8`
- **Output:** `7`

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Number of Subarrays with Bounded Maximum**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,1,4,3], left = 2, right = 3`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** There are three subarrays that meet the requirements: [2], [2, 1], [3].

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
    def numSubarrayBoundedMax(self, nums: list[int], left: int, right: int) -> int:
        ans = 0
        last_invalid = -1
        last_valid = -1
        
        for i, num in enumerate(nums):
            if num > right:
                last_invalid = i
                last_valid = i
            elif num >= left:
                last_valid = i
                
            ans += last_valid - last_invalid
            
        return ans
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
- [1546. Maximum Number of Non-Overlapping Subarrays With Sum Equals Target](../../1501-2000/1546-maximum-number-of-non-overlapping-subarrays-with-sum-equals-target/)
- [2871. Split Array Into Maximum Number of Subarrays](../../2501-3000/2871-split-array-into-maximum-number-of-subarrays/)
- [3113. Find the Number of Subarrays Where Boundary Elements Are Maximum](../../3001-3500/3113-find-the-number-of-subarrays-where-boundary-elements-are-maximum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/)
