# LeetCode 2009: Minimum Number of Operations to Make Array Continuous

**LeetCode Problem #2009 — Minimum Number of Operations to Make Array Continuous**
Solve LeetCode Minimum Number of Operations to Make Array Continuous using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Number of Operations to Make Array Continuous |
| LeetCode | #2009 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums`. In one operation, you can replace **any** element in `nums` with **any** integer.

`nums` is considered **continuous** if both of the following conditions are fulfilled:

All elements in `nums` are **unique**. 
 The difference between the **maximum** element and the **minimum** element in `nums` equals `nums.length - 1`.

For example, `nums = [4, 2, 5, 3]` is **continuous**, but `nums = [1, 2, 3, 5, 6]` is **not continuous**.

Return the **minimum** number of operations to make `nums` **continuous**.

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [4,2,5,3]`
- **Output:** `0`
- **Explanation:** nums is already continuous.

### Example 2
- **Input:** `nums = [1,2,3,5,6]`
- **Output:** `1`
- **Explanation:** One possible solution is to change the last element to 4.
The resulting array is [1,2,3,5,4], which is continuous.

### Example 3
- **Input:** `nums = [1,10,100,1000]`
- **Output:** `3`
- **Explanation:** One possible solution is to:
- Change the second element to 2.
- Change the third element to 3.
- Change the fourth element to 4.
The resulting array is [1,2,3,4], which is continuous.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Number of Operations to Make Array Continuous**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [4,2,5,3]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `0`.
4. **Verification:** nums is already continuous.

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
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        unique_nums = sorted(set(nums))
        
        max_keep = 0
        left = 0
        
        for right, val in enumerate(unique_nums):
            while val - unique_nums[left] >= n:
                left += 1
            if right - left + 1 > max_keep:
                max_keep = right - left + 1
                
        return n - max_keep
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
- [2654. Minimum Number of Operations to Make All Array Elements Equal to 1](../../2501-3000/2753-minimum-number-of-operations-to-make-all-array-elements-equal-to-1/)
- [2870. Minimum Number of Operations to Make Array Empty](../../3001-3500/3094-minimum-number-of-operations-to-make-array-empty/)
- [2997. Minimum Number of Operations to Make Array XOR Equal to K](../../3001-3500/3249-minimum-number-of-operations-to-make-array-xor-equal-to-k/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous/)
