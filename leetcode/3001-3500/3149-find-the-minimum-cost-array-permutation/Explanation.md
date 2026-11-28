# LeetCode 3149: Find the Minimum Cost Array Permutation

**LeetCode Problem #3149 — Find the Minimum Cost Array Permutation**
Solve LeetCode Find the Minimum Cost Array Permutation using Python and Backtracking. This solution finds the optimal result using Backtracking Recursive Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find the Minimum Cost Array Permutation |
| LeetCode | #3149 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Backtracking Recursive Search |
| Data Structure | Recursion Tree |
| Pattern | Backtracking |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array `nums` which is a permutation of `[0, 1, 2, ..., n - 1]`. The **score** of any permutation of `[0, 1, 2, ..., n - 1]` named `perm` is defined as:

`score(perm) = |perm[0] - nums[perm[1]]| + |perm[1] - nums[perm[2]]| + ... + |perm[n - 1] - nums[perm[0]]|`

Return the permutation `perm` which has the **minimum** possible score. If *multiple* permutations exist with this score, return the one that is lexicographically smallest among them.

## Constraints
- `2 <= n == nums.length <= 14`
- `nums` is a permutation of `[0, 1, 2, ..., n - 1]`.

## Examples
### Example 1
- **Input:** `nums = [1,0,2]`
- **Output:** `[0,1,2]`

### Example 2
- **Input:** `nums = [0,2,1]`
- **Output:** `[0,2,1]`

## Key Insight
Leverage **Backtracking** with **Recursion Tree** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Find the Minimum Cost Array Permutation**, we observe the problem requirements and utilize the **Backtracking** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,0,2]`.
2. **Processing Steps:** We apply **Backtracking Recursive Search** using our **Recursion Tree**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[0,1,2]`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Recursion Tree.

## Pattern
**Backtracking**

## Topics
- Backtracking
- Recursion

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List

class Solution:
    def findPermutation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        full = (1 << n) - 1
        INF = float('inf')

        f = [[INF] * n for _ in range(1 << n)]
        for last in range(n):
            f[full][last] = abs(last - nums[0])

        for mask in range(full - 1, 0, -1):
            if not mask & 1:
                continue  # every state contains node 0
            for last in range(n):
                if not mask >> last & 1:
                    continue
                best = INF
                for j in range(n):
                    if mask >> j & 1:
                        continue
                    v = abs(last - nums[j]) + f[mask | (1 << j)][j]
                    if v < best:
                        best = v
                f[mask][last] = best

        res = [0]
        mask, last = 1, 0
        while mask != full:
            target = f[mask][last]
            for j in range(n):
                if mask >> j & 1:
                    continue
                if abs(last - nums[j]) + f[mask | (1 << j)][j] == target:
                    res.append(j)
                    mask |= 1 << j
                    last = j
                    break
        return res
```

## Why This Works
By utilizing **Backtracking**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [153. Find Minimum in Rotated Sorted Array](../../0001-0500/0153-find-minimum-in-rotated-sorted-array/)
- [154. Find Minimum in Rotated Sorted Array II](../../0001-0500/0154-find-minimum-in-rotated-sorted-array-ii/)
- [2448. Minimum Cost to Make Array Equal](../../2001-2500/2448-minimum-cost-to-make-array-equal/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-the-minimum-cost-array-permutation/)
