# LeetCode 363: Max Sum of Rectangle No Larger Than K

**LeetCode Problem #363 — Max Sum of Rectangle No Larger Than K**
Solve LeetCode Max Sum of Rectangle No Larger Than K using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Max Sum of Rectangle No Larger Than K |
| LeetCode | #363 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an `m x n` matrix `matrix` and an integer `k`, return *the max sum of a rectangle in the matrix such that its sum is no larger than* `k`.

It is **guaranteed** that there will be a rectangle with a sum no larger than `k`.

## Constraints
- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 100`
- `-100 <= matrix[i][j] <= 100`
- `-10^5 <= k <= 10^5`

## Examples
### Example 1
- **Input:** `matrix = [[1,0,1],[0,-2,3]], k = 2`
- **Output:** `2`
- **Explanation:** Because the sum of the blue rectangle [[0, 1], [-2, 3]] is 2, and 2 is the max number no larger than k (k = 2).

### Example 2
- **Input:** `matrix = [[2,2,-1]], k = 3`
- **Output:** `3`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Max Sum of Rectangle No Larger Than K**, we observe the problem requirements and utilize the **Math & Logic** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `matrix = [[1,0,1],[0,-2,3]], k = 2`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** Because the sum of the blue rectangle [[0, 1], [-2, 3]] is 2, and 2 is the max number no larger than k (k = 2).

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
from bisect import bisect_left, insort

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        if m > n:  # make the pair loop run over the smaller dimension
            matrix = [list(r) for r in zip(*matrix)]
            m, n = n, m
        best = float('-inf')
        for top in range(m):
            cols = [0] * n
            for bottom in range(top, m):
                row = matrix[bottom]
                for c in range(n):
                    cols[c] += row[c]
                prefixes = [0]
                p = 0
                for v in cols:
                    p += v
                    i = bisect_left(prefixes, p - k)
                    if i < len(prefixes):
                        s = p - prefixes[i]
                        if s > best:
                            best = s
                            if best == k:
                                return k
                    insort(prefixes, p)
        return best
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
- [3007. Maximum Number That Sum of the Prices Is Less Than or Equal to K](../../3001-3500/3007-maximum-number-that-sum-of-the-prices-is-less-than-or-equal-to-k/)
- [3070. Count Submatrices with Top-Left Element and Sum Less Than k](../../3001-3500/3070-count-submatrices-with-top-left-element-and-sum-less-than-k/)
- [3091. Apply Operations to Make Sum of Array Greater Than or Equal to k](../../3001-3500/3091-apply-operations-to-make-sum-of-array-greater-than-or-equal-to-k/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/)
