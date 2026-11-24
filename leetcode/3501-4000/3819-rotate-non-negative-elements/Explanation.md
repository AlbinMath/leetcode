# LeetCode 3819: Rotate Non Negative Elements

**LeetCode Problem #3819 — Rotate Non Negative Elements**
Solve LeetCode Rotate Non Negative Elements using Python and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Rotate Non Negative Elements |
| LeetCode | #3819 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums` and an integer `k`.

Rotate only the **non-negative** elements of the array to the **left** by `k` positions, in a cyclic manner.

All **negative** elements must stay in their original positions and must not move.

After rotation, place the **non-negative** elements back into the array in the new order, filling only the positions that originally contained **non-negative** values and **skipping all negative** positions.

Return the resulting array.

## Constraints
- `1 <= nums.length <= 10^5`
- `-10^5 <= nums[i] <= 10^5`
- `0 <= k <= 10^5`

## Examples
### Example 1
- **Input:** `nums = [1,-2,3,-4], k = 3`
- **Output:** `[3,-2,1,-4]`
- **Explanation:** ​​​​​​​ 

 
 The non-negative elements, in order, are `[1, 3]`. 
 Left rotation with `k = 3` results in:
 
 `[1, 3] -> [3, 1] -> [1, 3] -> [3, 1]` 
 
 
 Placing them back into the non-negative indices results in `[3, -2, 1, -4]`.

### Example 2
- **Input:** `nums = [-3,-2,7], k = 1`
- **Output:** `[-3,-2,7]`
- **Explanation:** The non-negative elements, in order, are `[7]`. 
 Left rotation with `k = 1` results in `[7]`. 
 Placing them back into the non-negative indices results in `[-3, -2, 7]`.

### Example 3
- **Input:** `nums = [5,4,-9,6], k = 2`
- **Output:** `[6,5,-9,4]`
- **Explanation:** The non-negative elements, in order, are `[5, 4, 6]`. 
 Left rotation with `k = 2` results in `[6, 5, 4]`. 
 Placing them back into the non-negative indices results in `[6, 5, -9, 4]`.

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Rotate Non Negative Elements**, we observe the problem requirements and utilize the **Math & Logic** technique. We iterate through the inputs using **Mathematical Simulation & Modular Arithmetic**, leveraging a **Primitive Types** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Primitive Types**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,-2,3,-4], k = 3`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[3,-2,1,-4]`.
4. **Verification:** ​​​​​​​ 

 
 The non-negative elements, in order, are `[1, 3]`. 
 Left rotation with `k = 3` results in:
 
 `[1, 3] -> [3, 1] -> [1, 3] -> [3, 1]` 
 
 
 Placing them back into the non-negative indices results in `[3, -2, 1, -4]`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Primitive Types.

## Pattern
**Math & Logic**

## Topics
- Math
- Simulation

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def rotateElements(self, nums: list[int], k: int) -> list[int]:
        vals = [x for x in nums if x >= 0]
        m = len(vals)
        if m == 0:
            return nums
        k %= m
        vals = vals[k:] + vals[:k]
        j = 0
        for i in range(len(nums)):
            if nums[i] >= 0:
                nums[i] = vals[j]
                j += 1
        return nums
```

## Why This Works
By utilizing **Math & Logic**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [600. Non-negative Integers without Consecutive Ones](../../0501-1000/0600-non-negative-integers-without-consecutive-ones/)
- [1969. Minimum Non-Zero Product of the Array Elements](../../1501-2000/1969-minimum-non-zero-product-of-the-array-elements/)
- [3165. Maximum Sum of Subsequence With Non-adjacent Elements](../../3001-3500/3165-maximum-sum-of-subsequence-with-non-adjacent-elements/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/rotate-non-negative-elements/)
