# LeetCode 910: Smallest Range II

**LeetCode Problem #910 — Smallest Range II**
Solve LeetCode Smallest Range II using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Smallest Range II |
| LeetCode | #910 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums` and an integer `k`.

For each index `i` where `0 <= i < nums.length`, change `nums[i]` to be either `nums[i] + k` or `nums[i] - k`.

The **score** of `nums` is the difference between the maximum and minimum elements in `nums`.

Return *the minimum **score** of *`nums`* after changing the values at each index*.

## Constraints
- `1 <= nums.length <= 10^4`
- `0 <= nums[i] <= 10^4`
- `0 <= k <= 10^4`

## Examples
### Example 1
- **Input:** `nums = [1], k = 0`
- **Output:** `0`
- **Explanation:** The score is max(nums) - min(nums) = 1 - 1 = 0.

### Example 2
- **Input:** `nums = [0,10], k = 2`
- **Output:** `6`
- **Explanation:** Change nums to be [2, 8]. The score is max(nums) - min(nums) = 8 - 2 = 6.

### Example 3
- **Input:** `nums = [1,3,6], k = 3`
- **Output:** `3`
- **Explanation:** Change nums to be [4, 6, 3]. The score is max(nums) - min(nums) = 6 - 3 = 3.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Smallest Range II**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1], k = 0`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `0`.
4. **Verification:** The score is max(nums) - min(nums) = 1 - 1 = 0.

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
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        ans = nums[-1] - nums[0]
        for i in range(n - 1):
            hi = max(nums[i] + k, nums[-1] - k)
            lo = min(nums[0] + k, nums[i + 1] - k)
            ans = min(ans, hi - lo)
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
- [632. Smallest Range Covering Elements from K Lists](../../0501-1000/0632-smallest-range-covering-elements-from-k-lists/)
- [908. Smallest Range I](../../0501-1000/0908-smallest-range-i/)
- [201. Bitwise AND of Numbers Range](../../0001-0500/0201-bitwise-and-of-numbers-range/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/smallest-range-ii/)
