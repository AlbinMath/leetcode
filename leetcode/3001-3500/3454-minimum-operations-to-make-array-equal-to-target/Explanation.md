# LeetCode 3229: Minimum Operations to Make Array Equal to Target

**LeetCode Problem #3229 — Minimum Operations to Make Array Equal to Target**
Solve LeetCode Minimum Operations to Make Array Equal to Target using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Operations to Make Array Equal to Target |
| LeetCode | #3229 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two positive integer arrays `nums` and `target`, of the same length.

In a single operation, you can select any subarray of `nums` and increment each element within that subarray by 1 or decrement each element within that subarray by 1.

Return the **minimum** number of operations required to make `nums` equal to the array `target`.

## Constraints
- `1 <= nums.length == target.length <= 10^5`
- `1 <= nums[i], target[i] <= 10^8`

## Examples
### Example 1
- **Input:** `nums = [3,5,1,2], target = [4,6,2,4]`
- **Output:** `2`
- **Explanation:** We will perform the following operations to make `nums` equal to `target`: 
- Increment `nums[0..3]` by 1, `nums = [4,6,2,3]`. 
- Increment `nums[3..3]` by 1, `nums = [4,6,2,4]`.

### Example 2
- **Input:** `nums = [1,3,2], target = [2,1,4]`
- **Output:** `5`
- **Explanation:** We will perform the following operations to make `nums` equal to `target`: 
- Increment `nums[0..0]` by 1, `nums = [2,3,2]`. 
- Decrement `nums[1..1]` by 1, `nums = [2,2,2]`. 
- Decrement `nums[1..1]` by 1, `nums = [2,1,2]`. 
- Increment `nums[2..2]` by 1, `nums = [2,1,3]`. 
- Increment `nums[2..2]` by 1, `nums = [2,1,4]`.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Operations to Make Array Equal to Target**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [3,5,1,2], target = [4,6,2,4]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** We will perform the following operations to make `nums` equal to `target`: 
- Increment `nums[0..3]` by 1, `nums = [4,6,2,3]`. 
- Increment `nums[3..3]` by 1, `nums = [4,6,2,4]`.

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
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        ans = 0
        prev = 0
        for a, b in zip(nums, target):
            cur = b - a
            if cur > 0:
                ans += max(0, cur - max(prev, 0))
            elif cur < 0:
                ans += max(0, -cur - max(-prev, 0))
            prev = cur
        return ans
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
- [2997. Minimum Number of Operations to Make Array XOR Equal to K](../../3001-3500/3249-minimum-number-of-operations-to-make-array-xor-equal-to-k/)
- [3191. Minimum Operations to Make Binary Array Elements Equal to One I](../../3001-3500/3475-minimum-operations-to-make-binary-array-elements-equal-to-one-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-operations-to-make-array-equal-to-target/)
