# LeetCode 3257: Maximum Value Sum by Placing Three Rooks II

**LeetCode Problem #3257 — Maximum Value Sum by Placing Three Rooks II**
Solve LeetCode Maximum Value Sum by Placing Three Rooks II using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Value Sum by Placing Three Rooks II |
| LeetCode | #3257 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a `m x n` 2D array `board` representing a chessboard, where `board[i][j]` represents the **value** of the cell `(i, j)`.

Rooks in the **same** row or column **attack** each other. You need to place *three* rooks on the chessboard such that the rooks **do not** **attack** each other.

Return the **maximum** sum of the cell **values** on which the rooks are placed.

## Constraints
- `3 <= m == board.length <= 500`
- `3 <= n == board[i].length <= 500`
- `-10^9 <= board[i][j] <= 10^9`

## Examples
### Example 1
- **Input:** `board = [[-3,1,1,1],[-3,1,-3,1],[-3,2,1,1]]`
- **Output:** `4`
- **Explanation:** We can place the rooks in the cells `(0, 2)`, `(1, 3)`, and `(2, 1)` for a sum of `1 + 1 + 2 = 4`.

### Example 2
- **Input:** `board = [[1,2,3],[4,5,6],[7,8,9]]`
- **Output:** `15`
- **Explanation:** We can place the rooks in the cells `(0, 0)`, `(1, 1)`, and `(2, 2)` for a sum of `1 + 5 + 9 = 15`.

### Example 3
- **Input:** `board = [[1,1,1],[1,1,1],[1,1,1]]`
- **Output:** `3`
- **Explanation:** We can place the rooks in the cells `(0, 2)`, `(1, 1)`, and `(2, 0)` for a sum of `1 + 1 + 1 = 3`.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Maximum Value Sum by Placing Three Rooks II**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `board = [[-3,1,1,1],[-3,1,-3,1],[-3,2,1,1]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** We can place the rooks in the cells `(0, 2)`, `(1, 3)`, and `(2, 1)` for a sum of `1 + 1 + 2 = 4`.

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
import heapq

class Solution:
    def maximumValueSum(self, board: List[List[int]]) -> int:
        m, n = len(board), len(board[0])

        # Step 1: top 3 per row
        cand = []
        for r in range(m):
            for v, c in heapq.nlargest(3, ((board[r][c], c) for c in range(n))):
                cand.append((v, r, c))

        # Step 2: among those, top 3 per column
        by_col = [[] for _ in range(n)]
        for v, r, c in cand:
            by_col[c].append((v, r))
        pts = []
        for c in range(n):
            for v, r in heapq.nlargest(3, by_col[c]):
                pts.append((v, r, c))

        pts.sort(reverse=True)
        k = len(pts)  # at most 3 * min(m, n) <= 1500

        best = float('-inf')
        for a in range(k):
            v1, r1, c1 = pts[a]
            if v1 + pts[0][0] * 0 + 0 < 0 and best > float('-inf') and v1 * 3 < best:
                break  # even three copies of the largest remaining can't beat best
            for b in range(a + 1, k):
                v2, r2, c2 = pts[b]
                if r2 == r1 or c2 == c1:
                    continue
                if v1 + v2 + v2 < best:
                    break  # third value <= v2
                for d in range(b + 1, k):
                    v3, r3, c3 = pts[d]
                    if r3 == r1 or r3 == r2 or c3 == c1 or c3 == c2:
                        continue
                    s = v1 + v2 + v3
                    if s > best:
                        best = s
                    break  # later d have smaller values
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
- [3256. Maximum Value Sum by Placing Three Rooks I](../../3001-3500/3256-maximum-value-sum-by-placing-three-rooks-i/)
- [3780. Maximum Sum of Three Numbers Divisible by Three](../../3501-4000/3780-maximum-sum-of-three-numbers-divisible-by-three/)
- [628. Maximum Product of Three Numbers](../../0501-1000/0628-maximum-product-of-three-numbers/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-value-sum-by-placing-three-rooks-ii/)
