# LeetCode 3523: Make Array Non-decreasing

**LeetCode Problem #3523 — Make Array Non-decreasing**
Solve LeetCode Make Array Non-decreasing using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Make Array Non-decreasing |
| LeetCode | #3523 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums`. In one operation, you can select a subarray and replace it with a single element equal to its **maximum** value.

Return the **maximum possible size** of the array after performing zero or more operations such that the resulting array is **non-decreasing**.

## Constraints
- `1 <= nums.length <= 2 * 10^5`
- `1 <= nums[i] <= 2 * 10^5`

## Examples
### Example 1
- **Input:** `nums = [4,2,5,3,5]`
- **Output:** `3`
- **Explanation:** One way to achieve the maximum size is: 

 
 Replace subarray `nums[1..2] = [2, 5]` with `5` &rarr; `[4, 5, 3, 5]`. 
 Replace subarray `nums[2..3] = [3, 5]` with `5` &rarr; `[4, 5, 5]`. 
 

 The final array `[4, 5, 5]` is non-decreasing with size 3.

### Example 2
- **Input:** `nums = [1,2,3]`
- **Output:** `3`
- **Explanation:** No operation is needed as the array `[1,2,3]` is already non-decreasing.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Make Array Non-decreasing**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [4,2,5,3,5]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** One way to achieve the maximum size is: 

 
 Replace subarray `nums[1..2] = [2, 5]` with `5` &rarr; `[4, 5, 3, 5]`. 
 Replace subarray `nums[2..3] = [3, 5]` with `5` &rarr; `[4, 5, 5]`. 
 

 The final array `[4, 5, 5]` is non-decreasing with size 3.

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
    def maximumPossibleSize(self, nums: List[int]) -> int:
        mx = 0
        count = 0
        for x in nums:
            if x >= mx:
                mx = x
                count += 1
        return count
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
- [2289. Steps to Make Array Non-decreasing](../../2001-2500/2289-steps-to-make-array-non-decreasing/)
- [3326. Minimum Division Operations to Make Array Non Decreasing](../../3001-3500/3326-minimum-division-operations-to-make-array-non-decreasing/)
- [2945. Find Maximum Non-decreasing Array Length](../../2501-3000/2945-find-maximum-non-decreasing-array-length/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/make-array-non-decreasing/)
