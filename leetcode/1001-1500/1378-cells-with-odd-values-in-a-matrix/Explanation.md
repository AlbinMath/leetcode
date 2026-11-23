# LeetCode 1252: Cells with Odd Values in a Matrix

**LeetCode Problem #1252 — Cells with Odd Values in a Matrix**
Solve LeetCode Cells with Odd Values in a Matrix using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Cells with Odd Values in a Matrix |
| LeetCode | #1252 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There is an `m x n` matrix that is initialized to all `0`'s. There is also a 2D array `indices` where each `indices[i] = [r_i, c_i]` represents a **0-indexed location** to perform some increment operations on the matrix.

For each location `indices[i]`, do **both** of the following:

Increment **all** the cells on row `r_i`. 
 Increment **all** the cells on column `c_i`.

Given `m`, `n`, and `indices`, return *the **number of odd-valued cells** in the matrix after applying the increment to all locations in *`indices`.

## Constraints
- `1 <= m, n <= 50`
- `1 <= indices.length <= 100`
- `0 <= r_i < m`
- `0 <= c_i < n`

## Examples
### Example 1
- **Input:** `m = 2, n = 3, indices = [[0,1],[1,1]]`
- **Output:** `6`
- **Explanation:** Initial matrix = [[0,0,0],[0,0,0]].
After applying first increment it becomes [[1,2,1],[0,1,0]].
The final matrix is [[1,3,1],[1,3,1]], which contains 6 odd numbers.

### Example 2
- **Input:** `m = 2, n = 2, indices = [[1,1],[0,0]]`
- **Output:** `0`
- **Explanation:** Final matrix = [[2,2],[2,2]]. There are no odd numbers in the final matrix.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Cells with Odd Values in a Matrix**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `m = 2, n = 3, indices = [[0,1],[1,1]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `6`.
4. **Verification:** Initial matrix = [[0,0,0],[0,0,0]].
After applying first increment it becomes [[1,2,1],[0,1,0]].
The final matrix is [[1,3,1],[1,3,1]], which contains 6 odd numbers.

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
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        rows = [0] * m
        cols = [0] * n

        for r, c in indices:
            rows[r] += 1
            cols[c] += 1

        count = 0

        for r in range(m):
            for c in range(n):
                if (rows[r] + cols[c]) % 2 == 1:
                    count += 1

        return count
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
- [1030. Matrix Cells in Distance Order](../../1001-1500/1094-matrix-cells-in-distance-order/)
- [2713. Maximum Strictly Increasing Cells in a Matrix](../../2501-3000/2818-maximum-strictly-increasing-cells-in-a-matrix/)
- [328. Odd Even Linked List](../../0001-0500/0328-odd-even-linked-list/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/)
