# LeetCode 3171: Find Subarray With Bitwise OR Closest to K

**LeetCode Problem #3171 — Find Subarray With Bitwise OR Closest to K**
Solve LeetCode Find Subarray With Bitwise OR Closest to K using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Subarray With Bitwise OR Closest to K |
| LeetCode | #3171 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array `nums` and an integer `k`. You need to find a subarray of `nums` such that the **absolute difference** between `k` and the bitwise `OR` of the subarray elements is as** small** as possible. In other words, select a subarray `nums[l..r]` such that `|k - (nums[l] OR nums[l + 1] ... OR nums[r])|` is minimum.

Return the **minimum** possible value of the absolute difference.

A **subarray** is a contiguous non-empty sequence of elements within an array.

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`
- `1 <= k <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [1,2,4,5], k = 3`
- **Output:** `0`
- **Explanation:** The subarray `nums[0..1]` has `OR` value 3, which gives the minimum absolute difference `|3 - 3| = 0`.

### Example 2
- **Input:** `nums = [1,3,1,3], k = 2`
- **Output:** `1`
- **Explanation:** The subarray `nums[1..1]` has `OR` value 3, which gives the minimum absolute difference `|3 - 2| = 1`.

### Example 3
- **Input:** `nums = [1], k = 10`
- **Output:** `9`
- **Explanation:** There is a single subarray with `OR` value 1, which gives the minimum absolute difference `|10 - 1| = 9`.

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Find Subarray With Bitwise OR Closest to K**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,4,5], k = 3`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `0`.
4. **Verification:** The subarray `nums[0..1]` has `OR` value 3, which gives the minimum absolute difference `|3 - 3| = 0`.

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
    def minimumDifference(self, nums, k):
        best = float('inf')
        cur = set()
        for x in nums:
            cur = {v | x for v in cur}
            cur.add(x)
            for v in cur:
                d = abs(v - k)
                if d < best:
                    best = d
            if best == 0:
                return 0
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
- [658. Find K Closest Elements](../../0501-1000/0658-find-k-closest-elements/)
- [373. Find K Pairs with Smallest Sums](../../0001-0500/0373-find-k-pairs-with-smallest-sums/)
- [560. Subarray Sum Equals K](../../0501-1000/0560-subarray-sum-equals-k/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-subarray-with-bitwise-or-closest-to-k/)
