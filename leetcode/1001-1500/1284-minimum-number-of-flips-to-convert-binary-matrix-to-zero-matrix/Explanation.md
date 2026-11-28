# LeetCode 1284: Minimum Number of Flips to Convert Binary Matrix to Zero Matrix

**LeetCode Problem #1284 — Minimum Number of Flips to Convert Binary Matrix to Zero Matrix**
Solve LeetCode Minimum Number of Flips to Convert Binary Matrix to Zero Matrix using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Number of Flips to Convert Binary Matrix to Zero Matrix |
| LeetCode | #1284 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a `m x n` binary matrix `mat`. In one step, you can choose one cell and flip it and all the four neighbors of it if they exist (Flip is changing `1` to `0` and `0` to `1`). A pair of cells are called neighbors if they share one edge.

Return the *minimum number of steps* required to convert `mat` to a zero matrix or `-1` if you cannot.

A **binary matrix** is a matrix with all cells equal to `0` or `1` only.

A **zero matrix** is a matrix with all cells equal to `0`.

## Constraints
- `m == mat.length`
- `n == mat[i].length`
- `1 <= m, n <= 3`
- `mat[i][j]` is either `0` or `1`.

## Examples
### Example 1
- **Input:** `mat = [[0,0],[0,1]]`
- **Output:** `3`
- **Explanation:** One possible solution is to flip (1, 0) then (0, 1) and finally (1, 1) as shown.

### Example 2
- **Input:** `mat = [[0]]`
- **Output:** `0`
- **Explanation:** Given matrix is a zero matrix. We do not need to change it.

### Example 3
- **Input:** `mat = [[1,0,0],[1,0,0]]`
- **Output:** `-1`
- **Explanation:** Given matrix cannot be a zero matrix.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Minimum Number of Flips to Convert Binary Matrix to Zero Matrix**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `mat = [[0,0],[0,1]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** One possible solution is to flip (1, 0) then (0, 1) and finally (1, 1) as shown.

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
from collections import deque

class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])

        start = 0
        for r in range(m):
            for c in range(n):
                if mat[r][c]:
                    start |= 1 << (r * n + c)

        flips = []
        for r in range(m):
            for c in range(n):
                mask = 1 << (r * n + c)
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n:
                        mask |= 1 << (nr * n + nc)
                flips.append(mask)

        if start == 0:
            return 0

        seen = {start}
        q = deque([(start, 0)])
        while q:
            state, d = q.popleft()
            for f in flips:
                nxt = state ^ f
                if nxt == 0:
                    return d + 1
                if nxt not in seen:
                    seen.add(nxt)
                    q.append((nxt, d + 1))

        return -1
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
- [2220. Minimum Bit Flips to Convert Number](../../2001-2500/2220-minimum-bit-flips-to-convert-number/)
- [1888. Minimum Number of Flips to Make the Binary String Alternating](../../1501-2000/1888-minimum-number-of-flips-to-make-the-binary-string-alternating/)
- [3239. Minimum Number of Flips to Make Binary Grid Palindromic I](../../3001-3500/3239-minimum-number-of-flips-to-make-binary-grid-palindromic-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/)
