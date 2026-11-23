# LeetCode 1590: Make Sum Divisible by P

**LeetCode Problem #1590 — Make Sum Divisible by P**
Solve LeetCode Make Sum Divisible by P using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Make Sum Divisible by P |
| LeetCode | #1590 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an array of positive integers `nums`, remove the **smallest** subarray (possibly **empty**) such that the **sum** of the remaining elements is divisible by `p`. It is **not** allowed to remove the whole array.

Return *the length of the smallest subarray that you need to remove, or *`-1`* if it's impossible*.

A **subarray** is defined as a contiguous block of elements in the array.

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`
- `1 <= p <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [3,1,4,2], p = 6`
- **Output:** `1`
- **Explanation:** The sum of the elements in nums is 10, which is not divisible by 6. We can remove the subarray [4], and the sum of the remaining elements is 6, which is divisible by 6.

### Example 2
- **Input:** `nums = [6,3,5,2], p = 9`
- **Output:** `2`
- **Explanation:** We cannot remove a single element to get a sum divisible by 9. The best way is to remove the subarray [5,2], leaving us with [6,3] with sum 9.

### Example 3
- **Input:** `nums = [1,2,3], p = 3`
- **Output:** `0`
- **Explanation:** Here the sum is 6. which is already divisible by 3. Thus we do not need to remove anything.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Make Sum Divisible by P**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [3,1,4,2], p = 6`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** The sum of the elements in nums is 10, which is not divisible by 6. We can remove the subarray [4], and the sum of the remaining elements is 6, which is divisible by 6.

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
    def minSubarray(self, nums, p):
        r = sum(nums) % p
        if r == 0:
            return 0
        d, s, ans = {0: -1}, 0, len(nums)
        for i, x in enumerate(nums):
            s = (s + x) % p
            d[s] = i
            j = d.get((s - r) % p)
            if j is not None:
                ans = min(ans, i - j)
        return ans if ans < len(nums) else -1
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
- [2344. Minimum Deletions to Make Array Divisible](../../2001-2500/2423-minimum-deletions-to-make-array-divisible/)
- [3091. Apply Operations to Make Sum of Array Greater Than or Equal to k](../../3001-3500/3328-apply-operations-to-make-sum-of-array-greater-than-or-equal-to-k/)
- [3927. Minimize Array Sum Using Divisible Replacements](../../4001-4500/4301-minimize-array-sum-using-divisible-replacements/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/make-sum-divisible-by-p/)
