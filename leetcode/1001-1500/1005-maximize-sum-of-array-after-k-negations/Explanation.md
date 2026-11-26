# LeetCode 1005: Maximize Sum Of Array After K Negations

**LeetCode Problem #1005 — Maximize Sum Of Array After K Negations**
Solve LeetCode Maximize Sum Of Array After K Negations using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximize Sum Of Array After K Negations |
| LeetCode | #1005 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an integer array `nums` and an integer `k`, modify the array in the following way:

choose an index `i` and replace `nums[i]` with `-nums[i]`.

You should apply this process exactly `k` times. You may choose the same index `i` multiple times.

Return *the largest possible sum of the array after modifying it in this way*.

## Constraints
- `1 <= nums.length <= 10^4`
- `-100 <= nums[i] <= 100`
- `1 <= k <= 10^4`

## Examples
### Example 1
- **Input:** `nums = [4,2,3], k = 1`
- **Output:** `5`
- **Explanation:** Choose index 1 and nums becomes [4,-2,3].

### Example 2
- **Input:** `nums = [3,-1,0,2], k = 3`
- **Output:** `6`
- **Explanation:** Choose indices (1, 2, 2) and nums becomes [3,1,0,2].

### Example 3
- **Input:** `nums = [2,-3,-1,5,-4], k = 2`
- **Output:** `13`
- **Explanation:** Choose indices (1, 4) and nums becomes [2,3,-1,5,4].

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximize Sum Of Array After K Negations**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [4,2,3], k = 1`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `5`.
4. **Verification:** Choose index 1 and nums becomes [4,-2,3].

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
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()

        for i in range(len(nums)):
            if nums[i] < 0 and k > 0:
                nums[i] = -nums[i]
                k -= 1

        if k % 2 == 1:
            nums.sort()
            nums[0] = -nums[0]

        return sum(nums)
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
- [3091. Apply Operations to Make Sum of Array Greater Than or Equal to k](../../3001-3500/3091-apply-operations-to-make-sum-of-array-greater-than-or-equal-to-k/)
- [3264. Final Array State After K Multiplication Operations I](../../3001-3500/3264-final-array-state-after-k-multiplication-operations-i/)
- [3266. Final Array State After K Multiplication Operations II](../../3001-3500/3266-final-array-state-after-k-multiplication-operations-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/)
