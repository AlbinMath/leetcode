# LeetCode 4016: Maximum Area of Two Non-Overlapping Square Submatrices

**LeetCode Problem #4016 — Maximum Area of Two Non-Overlapping Square Submatrices**
Solve LeetCode Maximum Area of Two Non-Overlapping Square Submatrices using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Area of Two Non-Overlapping Square Submatrices |
| LeetCode | #4016 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a 2D integer matrix `mat` of size `m &times; n`, where:

`mat[r][c] == 1` means the cell at row `r` and column `c` is usable. 
 `mat[r][c] == 0` means it is not usable.

Your task is to find **two submatrices ** that satisfy the following conditions:

Both submatrices must be squares of the same side length `k`. 
 The two submatrices must not share any cell. 
 Each submatrix can only cover cells where `mat[r][c] == 1`.

Return the **maximum possible area** of each of the two squares. If it is not possible to choose two such squares, return 0.

## Constraints
- `mat.length == m`
- `mat[i].length == n`
- `1 <= m, n <= 500`
- `mat[i][j]` is either 0 or 1.

## Examples
### Example 1
- **Input:** `mat = [[1,1,1,0],[1,1,1,1],[0,0,1,1]]`
- **Output:** `4`
- **Explanation:** The largest equal non-overlapping squares have side length `k = 2` with area 4. 

 
 First square starts at top-left `(0, 0)` and covers cells `(0, 0)`, `(0, 1)`, `(1, 0)`, and `(1, 1)`. 
 Second square starts at top-left `(1, 2)` and covers cells `(1, 2)`, `(1, 3)`, `(2, 2)`, and `(2, 3)`. 
 

 Thus, the answer is 4.

### Example 2
- **Input:** `mat = [[0,1],[1,0]]`
- **Output:** `1`
- **Explanation:** The largest equal non-overlapping squares have side length `k = 1` with area 1. 

 
 First square starts at top-left `(0, 1)` and covers cell `(0, 1)`. 
 Second square starts at top-left `(1, 0)` and covers cell `(1, 0)`. 
 

 Thus, the answer is 1.

### Example 3
- **Input:** `mat = [[0,0],[0,1]]`
- **Output:** `0`
- **Explanation:** There is only one usable cell, so it is impossible to choose two non-overlapping squares. Thus, the answer is 0.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Maximum Area of Two Non-Overlapping Square Submatrices**, we observe the problem requirements and utilize the **Array / General** technique. We decompose the problem into overlapping subproblems using a **Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `mat = [[1,1,1,0],[1,1,1,1],[0,0,1,1]]`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** The largest equal non-overlapping squares have side length `k = 2` with area 4. 

 
 First square starts at top-left `(0, 0)` and covers cells `(0, 0)`, `(0, 1)`, `(1, 0)`, and `(1, 1)`. 
 Second square starts at top-left `(1, 2)` and covers cells `(1, 2)`, `(1, 3)`, `(2, 2)`, and `(2, 3)`. 
 

 Thus, the answer is 4.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for DP Table / Array.

## Pattern
**Dynamic Programming**

## Topics
- Dynamic Programming
- Memoization
- State Transition

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List

class Solution:
    def maxArea(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])

        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j]:
                    if i and j:
                        dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                    else:
                        dp[i][j] = 1

        def ok(k: int) -> bool:
            INF = float('inf')
            min_bot_r, max_top_r = INF, -INF
            min_bot_c, max_top_c = INF, -INF
            for i in range(k - 1, m):
                row = dp[i]
                for j in range(k - 1, n):
                    if row[j] >= k:
                        min_bot_r = min(min_bot_r, i)
                        max_top_r = max(max_top_r, i - k + 1)
                        min_bot_c = min(min_bot_c, j)
                        max_top_c = max(max_top_c, j - k + 1)
            return min_bot_r < max_top_r or min_bot_c < max_top_c

        lo, hi = 0, min(m, n)
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if ok(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo * lo
```

## Why This Works
By utilizing **Dynamic Programming**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Incorrect base case initialization.
2. Flawed state transition equation.
3. Storing unnecessary state leading to Memory Limit Exceeded (MLE).

## Interview Notes
- **Tests:** Subproblem decomposition, state transition logic, and space optimization.
- **Follow-up:** Can space complexity be reduced from $O(n^2)$ to $O(n)$ or $O(1)$?

## Related Problems
- [1031. Maximum Sum of Two Non-Overlapping Subarrays](../../1001-1500/1031-maximum-sum-of-two-non-overlapping-subarrays/)
- [689. Maximum Sum of 3 Non-Overlapping Subarrays](../../0501-1000/0689-maximum-sum-of-3-non-overlapping-subarrays/)
- [1477. Find Two Non-overlapping Sub-arrays Each With Target Sum](../../1001-1500/1477-find-two-non-overlapping-sub-arrays-each-with-target-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-area-of-two-non-overlapping-square-submatrices/)
