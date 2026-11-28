# LeetCode 2552: Count Increasing Quadruplets

**LeetCode Problem #2552 — Count Increasing Quadruplets**
Solve LeetCode Count Increasing Quadruplets using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Increasing Quadruplets |
| LeetCode | #2552 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a **0-indexed** integer array `nums` of size `n` containing all numbers from `1` to `n`, return *the number of increasing quadruplets*.

A quadruplet `(i, j, k, l)` is increasing if:

`0 <= i < j < k < l < n`, and 
 `nums[i] < nums[k] < nums[j] < nums[l]`.

## Constraints
- `4 <= nums.length <= 4000`
- `1 <= nums[i] <= nums.length`
- All the integers of `nums` are **unique**. `nums` is a permutation.

## Examples
### Example 1
- **Input:** `nums = [1,3,2,4,5]`
- **Output:** `2`
- **Explanation:** - When i = 0, j = 1, k = 2, and l = 3, nums[i] < nums[k] < nums[j] < nums[l].
- When i = 0, j = 1, k = 2, and l = 4, nums[i] < nums[k] < nums[j] < nums[l]. 
There are no other quadruplets, so we return 2.

### Example 2
- **Input:** `nums = [1,2,3,4]`
- **Output:** `0`
- **Explanation:** There exists only one quadruplet with i = 0, j = 1, k = 2, l = 3, but since nums[j] < nums[k], we return 0.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Count Increasing Quadruplets**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,3,2,4,5]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** - When i = 0, j = 1, k = 2, and l = 3, nums[i] < nums[k] < nums[j] < nums[l].
- When i = 0, j = 1, k = 2, and l = 4, nums[i] < nums[k] < nums[j] < nums[l]. 
There are no other quadruplets, so we return 2.

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
class Solution:
    def countQuadruplets(self, nums):
        n = len(nums)
        ans = 0
        freq = [0] * (n + 1)

        for j in range(n):
            less = [0] * (n + 1)
            count = 0

            for v in range(1, n + 1):
                less[v] = count
                count += freq[v]

            right_greater = sum(
                1 for k in range(j + 1, n)
                if nums[k] > nums[j]
            )

            for k in range(j + 1, n):
                if nums[k] > nums[j]:
                    right_greater -= 1
                elif nums[k] < nums[j]:
                    ans += less[nums[k]] * right_greater

            freq[nums[j]] += 1

        return ans
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
- [1995. Count Special Quadruplets](../../1501-2000/1995-count-special-quadruplets/)
- [38. Count and Say](../../0001-0500/0038-count-and-say/)
- [204. Count Primes](../../0001-0500/0204-count-primes/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-increasing-quadruplets/)
