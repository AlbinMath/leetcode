# LeetCode 3701: Compute Alternating Sum

**LeetCode Problem #3701 — Compute Alternating Sum**
Solve LeetCode Compute Alternating Sum using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Compute Alternating Sum |
| LeetCode | #3701 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums`.

The **alternating sum** of `nums` is the value obtained by **adding** elements at even indices and **subtracting** elements at odd indices. That is, `nums[0] - nums[1] + nums[2] - nums[3]...`

Return an integer denoting the alternating sum of `nums`.

## Constraints
- `1 <= nums.length <= 100`
- `1 <= nums[i] <= 100`

## Examples
### Example 1
- **Input:** `nums = [1,3,5,7]`
- **Output:** `-4`
- **Explanation:** Elements at even indices are `nums[0] = 1` and `nums[2] = 5` because 0 and 2 are even numbers. 
 Elements at odd indices are `nums[1] = 3` and `nums[3] = 7` because 1 and 3 are odd numbers. 
 The alternating sum is `nums[0] - nums[1] + nums[2] - nums[3] = 1 - 3 + 5 - 7 = -4`.

### Example 2
- **Input:** `nums = [100]`
- **Output:** `100`
- **Explanation:** The only element at even indices is `nums[0] = 100` because 0 is an even number. 
 There are no elements on odd indices. 
 The alternating sum is `nums[0] = 100`.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Compute Alternating Sum**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,3,5,7]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `-4`.
4. **Verification:** Elements at even indices are `nums[0] = 1` and `nums[2] = 5` because 0 and 2 are even numbers. 
 Elements at odd indices are `nums[1] = 3` and `nums[3] = 7` because 1 and 3 are odd numbers. 
 The alternating sum is `nums[0] - nums[1] + nums[2] - nums[3] = 1 - 3 + 5 - 7 = -4`.

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
    def alternatingSum(self, nums: list[int]) -> int:
        return sum(nums[0::2]) - sum(nums[1::2])
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
- [3695. Maximize Alternating Sum Using Swaps](../../4001-4500/4010-maximize-alternating-sum-using-swaps/)
- [3727. Maximum Alternating Sum of Squares](../../4001-4500/4078-maximum-alternating-sum-of-squares/)
- [693. Binary Number with Alternating Bits](../../0501-1000/0693-binary-number-with-alternating-bits/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/compute-alternating-sum/)
