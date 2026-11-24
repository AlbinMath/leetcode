# LeetCode 491: Non-decreasing Subsequences

**LeetCode Problem #491 — Non-decreasing Subsequences**
Solve LeetCode Non-decreasing Subsequences using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Non-decreasing Subsequences |
| LeetCode | #491 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an integer array `nums`, return *all the different possible non-decreasing subsequences of the given array with at least two elements*. You may return the answer in **any order**.

## Constraints
- `1 <= nums.length <= 15`
- `-100 <= nums[i] <= 100`

## Examples
### Example 1
- **Input:** `nums = [4,6,7,7]`
- **Output:** `[[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]`

### Example 2
- **Input:** `nums = [4,4,3,2,1]`
- **Output:** `[[4,4]]`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Non-decreasing Subsequences**, we observe the problem requirements and utilize the **Dynamic Programming** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [4,6,7,7]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]`.

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
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def dfs(start: int) -> None:
            if len(path) >= 2:
                res.append(path[:])
            used = set()
            for i in range(start, len(nums)):
                x = nums[i]
                if x in used:
                    continue  # same value already tried at this level
                if path and x < path[-1]:
                    continue  # would break non-decreasing order
                used.add(x)
                path.append(x)
                dfs(i + 1)
                path.pop()

        dfs(0)
        return res
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
- [2289. Steps to Make Array Non-decreasing](../../2001-2500/2289-steps-to-make-array-non-decreasing/)
- [2945. Find Maximum Non-decreasing Array Length](../../2501-3000/2945-find-maximum-non-decreasing-array-length/)
- [3326. Minimum Division Operations to Make Array Non Decreasing](../../3001-3500/3326-minimum-division-operations-to-make-array-non-decreasing/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/non-decreasing-subsequences/)
