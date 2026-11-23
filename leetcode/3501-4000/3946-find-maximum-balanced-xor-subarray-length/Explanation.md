# LeetCode 3755: Find Maximum Balanced XOR Subarray Length

**LeetCode Problem #3755 — Find Maximum Balanced XOR Subarray Length**
Solve LeetCode Find Maximum Balanced XOR Subarray Length using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Maximum Balanced XOR Subarray Length |
| LeetCode | #3755 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an integer array `nums`, return the **length** of the **longest subarray ** that has a bitwise XOR of zero and contains an **equal** number of **even** and **odd** numbers. If no such subarray exists, return 0.

## Constraints
- `1 <= nums.length <= 10^5`
- `0 <= nums[i] <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [3,1,3,2,0]`
- **Output:** `4`
- **Explanation:** The subarray `[1, 3, 2, 0]` has bitwise XOR `1 XOR 3 XOR 2 XOR 0 = 0` and contains 2 even and 2 odd numbers.

### Example 2
- **Input:** `nums = [3,2,8,5,4,14,9,15]`
- **Output:** `8`
- **Explanation:** The whole array has bitwise XOR `0` and contains 4 even and 4 odd numbers.

### Example 3
- **Input:** `nums = [0]`
- **Output:** `0`
- **Explanation:** No non-empty subarray satisfies both conditions.

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Find Maximum Balanced XOR Subarray Length**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [3,1,3,2,0]`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** The subarray `[1, 3, 2, 0]` has bitwise XOR `1 XOR 3 XOR 2 XOR 0 = 0` and contains 2 even and 2 odd numbers.

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
    def maxBalancedSubarray(self, nums):
        first = {(0, 0): 0}
        x = 0
        bal = 0
        best = 0
        for i, v in enumerate(nums, 1):
            x ^= v
            bal += 1 if v & 1 else -1
            key = (x, bal)
            if key in first:
                length = i - first[key]
                if length > best:
                    best = length
            else:
                first[key] = i
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
- [718. Maximum Length of Repeated Subarray](../../0501-1000/0718-maximum-length-of-repeated-subarray/)
- [3845. Maximum Subarray XOR with Bounded Range](../../4001-4500/4204-maximum-subarray-xor-with-bounded-range/)
- [2945. Find Maximum Non-decreasing Array Length](../../3001-3500/3211-find-maximum-non-decreasing-array-length/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-maximum-balanced-xor-subarray-length/)
