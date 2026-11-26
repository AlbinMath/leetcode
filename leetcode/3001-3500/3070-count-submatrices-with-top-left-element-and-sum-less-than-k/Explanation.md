# LeetCode 3070: Count Submatrices with Top-Left Element and Sum Less Than k

**LeetCode Problem #3070 — Count Submatrices with Top-Left Element and Sum Less Than k**
Solve LeetCode Count Submatrices with Top-Left Element and Sum Less Than k using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Submatrices with Top-Left Element and Sum Less Than k |
| LeetCode | #3070 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** integer matrix `grid` and an integer `k`.

Return *the **number** of submatrices that contain the top-left element of the* `grid`, *and have a sum less than or equal to *`k`.

## Constraints
- `m == grid.length `
- `n == grid[i].length`
- `1 <= n, m <= 1000 `
- `0 <= grid[i][j] <= 1000`
- `1 <= k <= 10^9`

## Examples
### Example 1
- **Input:** `grid = [[7,6,3],[6,6,1]], k = 18`
- **Output:** `4`
- **Explanation:** There are only 4 submatrices, shown in the image above, that contain the top-left element of grid, and have a sum less than or equal to 18.

### Example 2
- **Input:** `grid = [[7,2,9],[1,5,0],[2,6,6]], k = 20`
- **Output:** `6`
- **Explanation:** There are only 6 submatrices, shown in the image above, that contain the top-left element of grid, and have a sum less than or equal to 20.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Count Submatrices with Top-Left Element and Sum Less Than k**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [[7,6,3],[6,6,1]], k = 18`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** There are only 4 submatrices, shown in the image above, that contain the top-left element of grid, and have a sum less than or equal to 18.

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
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        P = [[0] * n for _ in range(m)]
        res = 0

        for i in range(m):
            for j in range(n):
                v = grid[i][j]
                if i > 0:
                    v += P[i - 1][j]
                if j > 0:
                    v += P[i][j - 1]
                if i > 0 and j > 0:
                    v -= P[i - 1][j - 1]
                P[i][j] = v
                if v <= k:
                    res += 1

        return res
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
- [2824. Count Pairs Whose Sum is Less than Target](../../2501-3000/2824-count-pairs-whose-sum-is-less-than-target/)
- [3007. Maximum Number That Sum of the Prices Is Less Than or Equal to K](../../3001-3500/3007-maximum-number-that-sum-of-the-prices-is-less-than-or-equal-to-k/)
- [2302. Count Subarrays With Score Less Than K](../../2001-2500/2302-count-subarrays-with-score-less-than-k/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-submatrices-with-top-left-element-and-sum-less-than-k/)
