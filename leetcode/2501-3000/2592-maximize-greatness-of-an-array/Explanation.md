# LeetCode 2592: Maximize Greatness of an Array

**LeetCode Problem #2592 — Maximize Greatness of an Array**
Solve LeetCode Maximize Greatness of an Array using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximize Greatness of an Array |
| LeetCode | #2592 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a 0-indexed integer array `nums`. You are allowed to permute `nums` into a new array `perm` of your choosing.

We define the **greatness** of `nums` be the number of indices `0 <= i < nums.length` for which `perm[i] > nums[i]`.

Return *the **maximum** possible greatness you can achieve after permuting* `nums`.

## Constraints
- `1 <= nums.length <= 10^5`
- `0 <= nums[i] <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [1,3,5,2,1,3,1]`
- **Output:** `4`
- **Explanation:** One of the optimal rearrangements is perm = [2,5,1,3,3,1,1].
At indices = 0, 1, 3, and 4, perm[i] > nums[i]. Hence, we return 4.

### Example 2
- **Input:** `nums = [1,2,3,4]`
- **Output:** `3`
- **Explanation:** We can prove the optimal perm is [2,3,4,1].
At indices = 0, 1, and 2, perm[i] > nums[i]. Hence, we return 3.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximize Greatness of an Array**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,3,5,2,1,3,1]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** One of the optimal rearrangements is perm = [2,5,1,3,3,1,1].
At indices = 0, 1, 3, and 4, perm[i] > nums[i]. Hence, we return 4.

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
    def maximizeGreatness(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        for x in nums:
            if x > nums[i]:
                i += 1
        return i
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
- [1005. Maximize Sum Of Array After K Negations](../../1001-1500/1005-maximize-sum-of-array-after-k-negations/)
- [1330. Reverse Subarray To Maximize Array Value](../../1001-1500/1330-reverse-subarray-to-maximize-array-value/)
- [2587. Rearrange Array to Maximize Prefix Score](../../2501-3000/2587-rearrange-array-to-maximize-prefix-score/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximize-greatness-of-an-array/)
