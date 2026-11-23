# LeetCode 3097: Shortest Subarray With OR at Least K II

**LeetCode Problem #3097 — Shortest Subarray With OR at Least K II**
Solve LeetCode Shortest Subarray With OR at Least K II using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Shortest Subarray With OR at Least K II |
| LeetCode | #3097 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array `nums` of **non-negative** integers and an integer `k`.

An array is called **special** if the bitwise `OR` of all of its elements is **at least** `k`.

Return *the length of the **shortest** **special** **non-empty** subarray of* `nums`, *or return* `-1` *if no special subarray exists*.

## Constraints
- `1 <= nums.length <= 2 * 10^5`
- `0 <= nums[i] <= 10^9`
- `0 <= k <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [1,2,3], k = 2`
- **Output:** `1`
- **Explanation:** The subarray `[3]` has `OR` value of `3`. Hence, we return `1`.

### Example 2
- **Input:** `nums = [2,1,8], k = 10`
- **Output:** `3`
- **Explanation:** The subarray `[2,1,8]` has `OR` value of `11`. Hence, we return `3`.

### Example 3
- **Input:** `nums = [1,2], k = 0`
- **Output:** `1`
- **Explanation:** The subarray `[1]` has `OR` value of `1`. Hence, we return `1`.

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Shortest Subarray With OR at Least K II**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,3], k = 2`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** The subarray `[3]` has `OR` value of `3`. Hence, we return `1`.

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
    def minimumSubarrayLength(self, nums, k):
        cnt = [0] * 31
        cur = 0
        l = 0
        best = float('inf')
        for r, x in enumerate(nums):
            for b in range(31):
                if (x >> b) & 1:
                    cnt[b] += 1
                    cur |= 1 << b
            while l <= r and cur >= k:
                if r - l + 1 < best:
                    best = r - l + 1
                y = nums[l]
                for b in range(31):
                    if (y >> b) & 1:
                        cnt[b] -= 1
                        if cnt[b] == 0:
                            cur &= ~(1 << b)
                l += 1
        return -1 if best == float('inf') else best
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
- [862. Shortest Subarray with Sum at Least K](../../0501-1000/0892-shortest-subarray-with-sum-at-least-k/)
- [3095. Shortest Subarray With OR at Least K I](../../3001-3500/3381-shortest-subarray-with-or-at-least-k-i/)
- [3795. Minimum Subarray Length With Distinct Sum At Least K](../../4001-4500/4152-minimum-subarray-length-with-distinct-sum-at-least-k/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-ii/)
