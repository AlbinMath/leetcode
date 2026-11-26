# LeetCode 3698: Split Array With Minimum Difference

**LeetCode Problem #3698 — Split Array With Minimum Difference**
Solve LeetCode Split Array With Minimum Difference using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Split Array With Minimum Difference |
| LeetCode | #3698 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums`.

Split the array into **exactly** two subarrays , `left` and `right`, such that `left` is ** strictly increasing ** and `right` is ** strictly decreasing **.

Return the **minimum possible absolute difference** between the sums of `left` and `right`. If no valid split exists, return `-1`.

## Constraints
- `2 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^5`

## Examples
### Example 1
- **Input:** `nums = [1,3,2]`
- **Output:** `2`
- **Explanation:** `i` 
 `left` 
 `right` 
 Validity 
 `left` sum 
 `right` sum 
 Absolute difference 
 
 
 
 
 0 
 [1] 
 [3, 2] 
 Yes 
 1 
 5 
 `|1 - 5| = 4` 
 
 
 1 
 [1, 3] 
 [2] 
 Yes 
 4 
 2 
 `|4 - 2| = 2` 
 
 
 

 Thus, the minimum absolute difference is 2.

### Example 2
- **Input:** `nums = [1,2,4,3]`
- **Output:** `4`
- **Explanation:** `i` 
 `left` 
 `right` 
 Validity 
 `left` sum 
 `right` sum 
 Absolute difference 
 
 
 
 
 0 
 [1] 
 [2, 4, 3] 
 No 
 1 
 9 
 - 
 
 
 1 
 [1, 2] 
 [4, 3] 
 Yes 
 3 
 7 
 `|3 - 7| = 4` 
 
 
 2 
 [1, 2, 4] 
 [3] 
 Yes 
 7 
 3 
 `|7 - 3| = 4` 
 
 
 

 Thus, the minimum absolute difference is 4.

### Example 3
- **Input:** `nums = [3,1,2]`
- **Output:** `-1`
- **Explanation:** No valid split exists, so the answer is -1.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Split Array With Minimum Difference**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,3,2]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** `i` 
 `left` 
 `right` 
 Validity 
 `left` sum 
 `right` sum 
 Absolute difference 
 
 
 
 
 0 
 [1] 
 [3, 2] 
 Yes 
 1 
 5 
 `|1 - 5| = 4` 
 
 
 1 
 [1, 3] 
 [2] 
 Yes 
 4 
 2 
 `|4 - 2| = 2` 
 
 
 

 Thus, the minimum absolute difference is 2.

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
    def splitArray(self, nums: List[int]) -> int:
        n = len(nums)
        P = [0] * (n + 1)
        for i, v in enumerate(nums):
            P[i + 1] = P[i] + v

        inc = [False] * n
        inc[0] = True
        for i in range(1, n):
            inc[i] = inc[i - 1] and nums[i] > nums[i - 1]

        dec = [False] * n
        dec[n - 1] = True
        for i in range(n - 2, -1, -1):
            dec[i] = dec[i + 1] and nums[i] > nums[i + 1]

        best = -1
        for i in range(n - 1):
            if inc[i] and dec[i + 1]:
                diff = abs(P[i + 1] - (P[n] - P[i + 1]))
                if best == -1 or diff < best:
                    best = diff
        return best
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
- [2547. Minimum Cost to Split an Array](../../2501-3000/2547-minimum-cost-to-split-an-array/)
- [410. Split Array Largest Sum](../../0001-0500/0410-split-array-largest-sum/)
- [659. Split Array into Consecutive Subsequences](../../0501-1000/0659-split-array-into-consecutive-subsequences/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/split-array-with-minimum-difference/)
