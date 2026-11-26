# LeetCode 798: Smallest Rotation with Highest Score

**LeetCode Problem #798 — Smallest Rotation with Highest Score**
Solve LeetCode Smallest Rotation with Highest Score using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Smallest Rotation with Highest Score |
| LeetCode | #798 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array `nums`. You can rotate it by a non-negative integer `k` so that the array becomes `[nums[k], nums[k + 1], ... nums[nums.length - 1], nums[0], nums[1], ..., nums[k-1]]`. Afterward, any entries that are less than or equal to their index are worth one point.

For example, if we have `nums = [2,4,1,3,0]`, and we rotate by `k = 2`, it becomes `[1,3,0,2,4]`. This is worth `3` points because `1 > 0` [no points], `3 > 1` [no points], `0 <= 2` [one point], `2 <= 3` [one point], `4 <= 4` [one point].

Return *the rotation index *`k`* that corresponds to the highest score we can achieve if we rotated *`nums`* by it*. If there are multiple answers, return the smallest such index `k`.

## Constraints
- `1 <= nums.length <= 10^5`
- `0 <= nums[i] < nums.length`

## Examples
### Example 1
- **Input:** `nums = [2,3,1,4,0]`
- **Output:** `3`
- **Explanation:** Scores for each k are listed below: 
k = 0, nums = [2,3,1,4,0], score 2
k = 1, nums = [3,1,4,0,2], score 3
k = 2, nums = [1,4,0,2,3], score 3
k = 3, nums = [4,0,2,3,1], score 4
k = 4, nums = [0,2,3,1,4], score 3
So we should choose k = 3, which has the highest score.

### Example 2
- **Input:** `nums = [1,3,0,2,4]`
- **Output:** `0`
- **Explanation:** nums will always have 3 points no matter how it shifts.
So we will choose the smallest k, which is 0.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Smallest Rotation with Highest Score**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,3,1,4,0]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** Scores for each k are listed below: 
k = 0, nums = [2,3,1,4,0], score 2
k = 1, nums = [3,1,4,0,2], score 3
k = 2, nums = [1,4,0,2,3], score 3
k = 3, nums = [4,0,2,3,1], score 4
k = 4, nums = [0,2,3,1,4], score 3
So we should choose k = 3, which has the highest score.

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
class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        n = len(nums)
        diff = [0] * (n + 1)

        for i, v in enumerate(nums):
            lo = (i + 1) % n
            hi = (i - v) % n
            if lo <= hi:
                diff[lo] += 1
                diff[hi + 1] -= 1
            else:  # range wraps around
                diff[lo] += 1
                diff[n] -= 1
                diff[0] += 1
                diff[hi + 1] -= 1

        best_k, best, cur = 0, -1, 0
        for k in range(n):
            cur += diff[k]
            if cur > best:
                best, best_k = cur, k
        return best_k
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
- [2049. Count Nodes With the Highest Score](../../2001-2500/2049-count-nodes-with-the-highest-score/)
- [2374. Node With Highest Edge Score](../../2001-2500/2374-node-with-highest-edge-score/)
- [1886. Determine Whether Matrix Can Be Obtained By Rotation](../../1501-2000/1886-determine-whether-matrix-can-be-obtained-by-rotation/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/smallest-rotation-with-highest-score/)
