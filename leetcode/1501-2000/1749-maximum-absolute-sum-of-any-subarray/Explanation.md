# LeetCode 1749: Maximum Absolute Sum of Any Subarray

**LeetCode Problem #1749 — Maximum Absolute Sum of Any Subarray**
Solve LeetCode Maximum Absolute Sum of Any Subarray using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Absolute Sum of Any Subarray |
| LeetCode | #1749 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums`. The **absolute sum** of a subarray `[nums_l, nums_l+1, ..., nums_r-1, nums_r]` is `abs(nums_l + nums_l+1 + ... + nums_r-1 + nums_r)`.

Return *the **maximum** absolute sum of any **(possibly empty)** subarray of *`nums`.

Note that `abs(x)` is defined as follows:

If `x` is a negative integer, then `abs(x) = -x`. 
 If `x` is a non-negative integer, then `abs(x) = x`.

## Constraints
- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

## Examples
### Example 1
- **Input:** `nums = [1,-3,2,3,-4]`
- **Output:** `5`
- **Explanation:** The subarray [2,3] has absolute sum = abs(2+3) = abs(5) = 5.

### Example 2
- **Input:** `nums = [2,-5,1,-4,3,-2]`
- **Output:** `8`
- **Explanation:** The subarray [-5,1,-4] has absolute sum = abs(-5+1-4) = abs(-8) = 8.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Absolute Sum of Any Subarray**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,-3,2,3,-4]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `5`.
4. **Verification:** The subarray [2,3] has absolute sum = abs(2+3) = abs(5) = 5.

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
    def maxAbsoluteSum(self, nums: list[int]) -> int:
        prefix_sum = 0
        max_prefix = 0
        min_prefix = 0
        
        for x in nums:
            prefix_sum += x
            if prefix_sum > max_prefix:
                max_prefix = prefix_sum
            elif prefix_sum < min_prefix:
                min_prefix = prefix_sum
                
        return max_prefix - min_prefix
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
- [1589. Maximum Sum Obtained of Any Permutation](../../1501-2000/1589-maximum-sum-obtained-of-any-permutation/)
- [918. Maximum Sum Circular Subarray](../../0501-1000/0918-maximum-sum-circular-subarray/)
- [1186. Maximum Subarray Sum with One Deletion](../../1001-1500/1186-maximum-subarray-sum-with-one-deletion/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/)
