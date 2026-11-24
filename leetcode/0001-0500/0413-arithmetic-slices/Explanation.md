# LeetCode 413: Arithmetic Slices

**LeetCode Problem #413 — Arithmetic Slices**
Solve LeetCode Arithmetic Slices using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Arithmetic Slices |
| LeetCode | #413 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
An integer array is called arithmetic if it consists of **at least three elements** and if the difference between any two consecutive elements is the same.

For example, `[1,3,5,7,9]`, `[7,7,7,7]`, and `[3,-1,-5,-9]` are arithmetic sequences.

Given an integer array `nums`, return *the number of arithmetic **subarrays** of* `nums`.

A **subarray** is a contiguous subsequence of the array.

## Constraints
- `1 <= nums.length <= 5000`
- `-1000 <= nums[i] <= 1000`

## Examples
### Example 1
- **Input:** `nums = [1,2,3,4]`
- **Output:** `3`
- **Explanation:** We have 3 arithmetic slices in nums: [1, 2, 3], [2, 3, 4] and [1,2,3,4] itself.

### Example 2
- **Input:** `nums = [1]`
- **Output:** `0`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Arithmetic Slices**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,3,4]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** We have 3 arithmetic slices in nums: [1, 2, 3], [2, 3, 4] and [1,2,3,4] itself.

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
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        total = 0
        curr = 0
        
        for i in range(2, len(nums)):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                curr += 1
                total += curr
            else:
                curr = 0
                
        return total
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
- [446. Arithmetic Slices II - Subsequence](../../0001-0500/0446-arithmetic-slices-ii-subsequence/)
- [1027. Longest Arithmetic Subsequence](../../1001-1500/1027-longest-arithmetic-subsequence/)
- [1307. Verbal Arithmetic Puzzle](../../1001-1500/1307-verbal-arithmetic-puzzle/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/arithmetic-slices/)
