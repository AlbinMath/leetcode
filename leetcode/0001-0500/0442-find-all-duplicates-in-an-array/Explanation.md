# LeetCode 442: Find All Duplicates in an Array

**LeetCode Problem #442 — Find All Duplicates in an Array**
Solve LeetCode Find All Duplicates in an Array using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find All Duplicates in an Array |
| LeetCode | #442 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an integer array `nums` of length `n` where all the integers of `nums` are in the range `[1, n]` and each integer appears **at most** **twice**, return *an array of all the integers that appears **twice***.

You must write an algorithm that runs in `O(n)` time and uses only *constant* auxiliary space, excluding the space needed to store the output

## Constraints
- `n == nums.length`
- `1 <= n <= 10^5`
- `1 <= nums[i] <= n`
- Each element in `nums` appears **once** or **twice**.

## Examples
### Example 1
- **Input:** `nums = [4,3,2,7,8,2,3,1]`
- **Output:** `[2,3]`

### Example 2
- **Input:** `nums = [1,1,2]`
- **Output:** `[1]`

### Example 3
- **Input:** `nums = [1]`
- **Output:** `[]`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Find All Duplicates in an Array**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [4,3,2,7,8,2,3,1]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[2,3]`.

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
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = []
        
        for num in nums:
            index = abs(num) - 1
            if nums[index] < 0:
                duplicates.append(abs(num))
            else:
                nums[index] = -nums[index]
                
        return duplicates
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
- [448. Find All Numbers Disappeared in an Array](../../0001-0500/0448-find-all-numbers-disappeared-in-an-array/)
- [2150. Find All Lonely Numbers in the Array](../../2001-2500/2150-find-all-lonely-numbers-in-the-array/)
- [2593. Find Score of an Array After Marking All Elements](../../2501-3000/2593-find-score-of-an-array-after-marking-all-elements/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-all-duplicates-in-an-array/)
