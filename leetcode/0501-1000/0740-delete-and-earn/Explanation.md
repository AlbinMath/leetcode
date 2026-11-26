# LeetCode 740: Delete and Earn

**LeetCode Problem #740 — Delete and Earn**
Solve LeetCode Delete and Earn using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Delete and Earn |
| LeetCode | #740 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums`. You want to maximize the number of points you get by performing the following operation any number of times:

Pick any `nums[i]` and delete it to earn `nums[i]` points. Afterwards, you must delete every element equal to `nums[i] - 1` and **every** element equal to `nums[i] + 1`.

Return *the **maximum number of points** you can earn by applying the above operation some number of times*.

## Constraints
- `1 <= nums.length <= 2 * 10^4`
- `1 <= nums[i] <= 10^4`

## Examples
### Example 1
- **Input:** `nums = [3,4,2]`
- **Output:** `6`
- **Explanation:** You can perform the following operations:
- Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2].
- Delete 2 to earn 2 points. nums = [].
You earn a total of 6 points.

### Example 2
- **Input:** `nums = [2,2,3,3,3,4]`
- **Output:** `9`
- **Explanation:** You can perform the following operations:
- Delete a 3 to earn 3 points. All 2's and 4's are also deleted. nums = [3,3].
- Delete a 3 again to earn 3 points. nums = [3].
- Delete a 3 once more to earn 3 points. nums = [].
You earn a total of 9 points.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Delete and Earn**, we observe the problem requirements and utilize the **Array / General** technique. We decompose the problem into overlapping subproblems using a **Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [3,4,2]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `6`.
4. **Verification:** You can perform the following operations:
- Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2].
- Delete 2 to earn 2 points. nums = [].
You earn a total of 6 points.

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
    def deleteAndEarn(self, nums: List[int]) -> int:
        max_val = max(nums)
        points = [0] * (max_val + 1)
        for num in nums:
            points[num] += num
        prev2 = 0  # dp[i - 2]
        prev1 = 0  # dp[i - 1]
        
        for pts in points:
            curr = max(prev1, prev2 + pts)
            prev2 = prev1
            prev1 = curr
            
        return prev1
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
- [3332. Maximum Points Tourist Can Earn](../../3001-3500/3332-maximum-points-tourist-can-earn/)
- [3418. Maximum Amount of Money Robot Can Earn](../../3001-3500/3418-maximum-amount-of-money-robot-can-earn/)
- [196. Delete Duplicate Emails](../../0001-0500/0196-delete-duplicate-emails/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/delete-and-earn/)
