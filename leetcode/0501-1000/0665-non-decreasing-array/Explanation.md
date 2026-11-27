# LeetCode 665: Non-decreasing Array

**LeetCode Problem #665 — Non-decreasing Array**
Solve LeetCode Non-decreasing Array using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Non-decreasing Array |
| LeetCode | #665 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an array `nums` with `n` integers, your task is to check if it could become non-decreasing by modifying **at most one element**.

We define an array is non-decreasing if `nums[i] <= nums[i + 1]` holds for every `i` (**0-based**) such that (`0 <= i <= n - 2`).

## Constraints
- `n == nums.length`
- `1 <= n <= 10^4`
- `-10^5 <= nums[i] <= 10^5`

## Examples
### Example 1
- **Input:** `nums = [4,2,3]`
- **Output:** `true`
- **Explanation:** You could modify the first 4 to 1 to get a non-decreasing array.

### Example 2
- **Input:** `nums = [4,2,1]`
- **Output:** `false`
- **Explanation:** You cannot get a non-decreasing array by modifying at most one element.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Non-decreasing Array**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [4,2,3]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** You could modify the first 4 to 1 to get a non-decreasing array.

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
    def checkPossibility(self, nums: List[int]) -> bool:
        changed = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if changed:
                    return False
                changed = True
                if i == 0 or nums[i - 1] <= nums[i + 1]:
                    nums[i] = nums[i + 1]
                else:
                    nums[i + 1] = nums[i]
        return True
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
- [2945. Find Maximum Non-decreasing Array Length](../../2501-3000/2945-find-maximum-non-decreasing-array-length/)
- [3326. Minimum Division Operations to Make Array Non Decreasing](../../3001-3500/3326-minimum-division-operations-to-make-array-non-decreasing/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/non-decreasing-array/)
