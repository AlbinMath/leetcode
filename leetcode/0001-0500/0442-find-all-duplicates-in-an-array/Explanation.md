# LeetCode 442: Find All Duplicates in an Array

**LeetCode Problem #442 — Find All Duplicates in an Array**
Solve LeetCode Find All Duplicates in an Array using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find All Duplicates in an Array |
| LeetCode | #442 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
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
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Find All Duplicates in an Array**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [4,3,2,7,8,2,3,1]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[2,3]`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

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
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [448. Find All Numbers Disappeared in an Array](../../0001-0500/0448-find-all-numbers-disappeared-in-an-array/)
- [2150. Find All Lonely Numbers in the Array](../../2001-2500/2150-find-all-lonely-numbers-in-the-array/)
- [2593. Find Score of an Array After Marking All Elements](../../2501-3000/2593-find-score-of-an-array-after-marking-all-elements/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-all-duplicates-in-an-array/)
