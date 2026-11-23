# LeetCode 2765: Longest Alternating Subarray

**LeetCode Problem #2765 — Longest Alternating Subarray**
Solve LeetCode Longest Alternating Subarray using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest Alternating Subarray |
| LeetCode | #2765 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** integer array `nums`. A subarray `s` of length `m` is called **alternating** if:

`m` is greater than `1`. 
 `s_1 = s_0 + 1`. 
 The **0-indexed** subarray `s` looks like `[s_0, s_1, s_0, s_1,...,s_(m-1) % 2]`. In other words, `s_1 - s_0 = 1`, `s_2 - s_1 = -1`, `s_3 - s_2 = 1`, `s_4 - s_3 = -1`, and so on up to `s[m - 1] - s[m - 2] = (-1)^m`.

Return *the maximum length of all **alternating** subarrays present in *`nums` *or *`-1`* if no such subarray exists**.*

A subarray is a contiguous **non-empty** sequence of elements within an array.

## Constraints
- `2 <= nums.length <= 100`
- `1 <= nums[i] <= 10^4`

## Examples
### Example 1
- **Input:** `nums = [2,3,4,3,4]`
- **Output:** `4`
- **Explanation:** The alternating subarrays are `[2, 3]`, `[3,4]`, `[3,4,3]`, and `[3,4,3,4]`. The longest of these is `[3,4,3,4]`, which is of length 4.

### Example 2
- **Input:** `nums = [4,5,6]`
- **Output:** `2`
- **Explanation:** `[4,5]` and `[5,6]` are the only two alternating subarrays. They are both of length 2.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Longest Alternating Subarray**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,3,4,3,4]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** The alternating subarrays are `[2, 3]`, `[3,4]`, `[3,4,3]`, and `[3,4,3,4]`. The longest of these is `[3,4,3,4]`, which is of length 4.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution(object):
    def alternatingSubarray(self, nums):
        max_len = -1
        curr_len = 0
        expected_diff = 1

        for i in range(1, len(nums)):
            diff = nums[i] - nums[i - 1]
            if curr_len > 0 and diff == expected_diff:
                curr_len += 1
                expected_diff = -expected_diff
                max_len = max(max_len, curr_len)
            elif diff == 1:
                curr_len = 2
                expected_diff = -1
                max_len = max(max_len, 2)
            else:
                curr_len = 0

        return max_len
```

## Why This Works
By utilizing **Array / General**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [3830. Longest Alternating Subarray After Removing At Most One Element](../../4001-4500/4198-longest-alternating-subarray-after-removing-at-most-one-element/)
- [978. Longest Turbulent Subarray](../../1001-1500/1020-longest-turbulent-subarray/)
- [1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit](../../1501-2000/1549-longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longest-alternating-subarray/)
