# LeetCode 2962: Count Subarrays Where Max Element Appears at Least K Times

**LeetCode Problem #2962 — Count Subarrays Where Max Element Appears at Least K Times**
Solve LeetCode Count Subarrays Where Max Element Appears at Least K Times using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Subarrays Where Max Element Appears at Least K Times |
| LeetCode | #2962 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums` and a **positive** integer `k`.

Return *the number of subarrays where the **maximum** element of *`nums`* appears **at least** *`k`* times in that subarray.*

A **subarray** is a contiguous sequence of elements within an array.

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^6`
- `1 <= k <= 10^5`

## Examples
### Example 1
- **Input:** `nums = [1,3,2,3,3], k = 2`
- **Output:** `6`
- **Explanation:** The subarrays that contain the element 3 at least 2 times are: [1,3,2,3], [1,3,2,3,3], [3,2,3], [3,2,3,3], [2,3,3] and [3,3].

### Example 2
- **Input:** `nums = [1,4,2,1], k = 3`
- **Output:** `0`
- **Explanation:** No subarray contains the element 4 at least 3 times.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Count Subarrays Where Max Element Appears at Least K Times**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,3,2,3,3], k = 2`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `6`.
4. **Verification:** The subarrays that contain the element 3 at least 2 times are: [1,3,2,3], [1,3,2,3,3], [3,2,3], [3,2,3,3], [2,3,3] and [3,3].

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
from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        M = max(nums)
        cnt = 0
        l = 0
        ans = 0
        for x in nums:
            if x == M:
                cnt += 1
            while cnt >= k:
                if nums[l] == M:
                    cnt -= 1
                l += 1
            ans += l
        return ans
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
- [2302. Count Subarrays With Score Less Than K](../../2001-2500/2302-count-subarrays-with-score-less-than-k/)
- [2488. Count Subarrays With Median K](../../2001-2500/2488-count-subarrays-with-median-k/)
- [3420. Count Non-Decreasing Subarrays After K Operations](../../3001-3500/3420-count-non-decreasing-subarrays-after-k-operations/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/)
