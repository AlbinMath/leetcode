# LeetCode 1673: Find the Most Competitive Subsequence

**LeetCode Problem #1673 — Find the Most Competitive Subsequence**
Solve LeetCode Find the Most Competitive Subsequence using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find the Most Competitive Subsequence |
| LeetCode | #1673 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an integer array `nums` and a positive integer `k`, return *the most** competitive** subsequence of *`nums` *of size *`k`.

An array's subsequence is a resulting sequence obtained by erasing some (possibly zero) elements from the array.

We define that a subsequence `a` is more **competitive** than a subsequence `b` (of the same length) if in the first position where `a` and `b` differ, subsequence `a` has a number **less** than the corresponding number in `b`. For example, `[1,3,4]` is more competitive than `[1,3,5]` because the first position they differ is at the final number, and `4` is less than `5`.

## Constraints
- `1 <= nums.length <= 10^5`
- `0 <= nums[i] <= 10^9`
- `1 <= k <= nums.length`

## Examples
### Example 1
- **Input:** `nums = [3,5,2,6], k = 2`
- **Output:** `[2,6]`
- **Explanation:** Among the set of every possible subsequence: {[3,5], [3,2], [3,6], [5,2], [5,6], [2,6]}, [2,6] is the most competitive.

### Example 2
- **Input:** `nums = [2,4,3,3,5,4,9,6], k = 4`
- **Output:** `[2,3,3,4]`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Find the Most Competitive Subsequence**, we observe the problem requirements and utilize the **Dynamic Programming** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [3,5,2,6], k = 2`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[2,6]`.
4. **Verification:** Among the set of every possible subsequence: {[3,5], [3,2], [3,6], [5,2], [5,6], [2,6]}, [2,6] is the most competitive.

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
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        stack = []
        for i, x in enumerate(nums):
            while stack and stack[-1] > x and len(stack) + n - i > k:
                stack.pop()
            if len(stack) < k:
                stack.append(x)
        return stack
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
- [2099. Find Subsequence of Length K With the Largest Sum](../../2001-2500/2204-find-subsequence-of-length-k-with-the-largest-sum/)
- [1606. Find Servers That Handled Most Number of Requests](../../1501-2000/1710-find-servers-that-handled-most-number-of-requests/)
- [3527. Find the Most Common Response](../../3501-4000/3707-find-the-most-common-response/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-the-most-competitive-subsequence/)
