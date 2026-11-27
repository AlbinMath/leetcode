# LeetCode 764: Largest Plus Sign

**LeetCode Problem #764 — Largest Plus Sign**
Solve LeetCode Largest Plus Sign using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Largest Plus Sign |
| LeetCode | #764 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer `n`. You have an `n x n` binary grid `grid` with all values initially `1`'s except for some indices given in the array `mines`. The `i^th` element of the array `mines` is defined as `mines[i] = [x_i, y_i]` where `grid[x_i][y_i] == 0`.

Return *the order of the largest **axis-aligned** plus sign of *1*'s contained in *`grid`. If there is none, return `0`.

An **axis-aligned plus sign** of `1`'s of order `k` has some center `grid[r][c] == 1` along with four arms of length `k - 1` going up, down, left, and right, and made of `1`'s. Note that there could be `0`'s or `1`'s beyond the arms of the plus sign, only the relevant area of the plus sign is checked for `1`'s.

## Constraints
- `1 <= n <= 500`
- `1 <= mines.length <= 5000`
- `0 <= x_i, y_i < n`
- All the pairs `(x_i, y_i)` are **unique**.

## Examples
### Example 1
- **Input:** `n = 5, mines = [[4,2]]`
- **Output:** `2`
- **Explanation:** In the above grid, the largest plus sign can only be of order 2. One of them is shown.

### Example 2
- **Input:** `n = 1, mines = [[0,0]]`
- **Output:** `0`
- **Explanation:** There is no plus sign, so return 0.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Largest Plus Sign**, we observe the problem requirements and utilize the **Array / General** technique. We decompose the problem into overlapping subproblems using a **Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 5, mines = [[4,2]]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** In the above grid, the largest plus sign can only be of order 2. One of them is shown.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: list[list[int]]) -> int:
        dp = [[n] * n for _ in range(n)]
        for r, c in mines:
            dp[r][c] = 0
            
        for r in range(n):
            count = 0
            for c in range(n):
                count = 0 if dp[r][c] == 0 else count + 1
                dp[r][c] = min(dp[r][c], count)
                
            count = 0
            for c in range(n - 1, -1, -1):
                count = 0 if dp[r][c] == 0 else count + 1
                dp[r][c] = min(dp[r][c], count)
                
        ans = 0
        for c in range(n):
            count = 0
            for r in range(n):
                count = 0 if dp[r][c] == 0 else count + 1
                dp[r][c] = min(dp[r][c], count)
                
            count = 0
            for r in range(n - 1, -1, -1):
                count = 0 if dp[r][c] == 0 else count + 1
                dp[r][c] = min(dp[r][c], count)
                if dp[r][c] > ans:
                    ans = dp[r][c]
                    
        return ans
```

## Why This Works
By utilizing **Array / General**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1822. Sign of the Product of an Array](../../1501-2000/1822-sign-of-the-product-of-an-array/)
- [2149. Rearrange Array Elements by Sign](../../2001-2500/2149-rearrange-array-elements-by-sign/)
- [66. Plus One](../../0001-0500/0066-plus-one/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/largest-plus-sign/)
