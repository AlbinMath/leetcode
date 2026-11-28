# LeetCode 1039: Minimum Score Triangulation of Polygon

**LeetCode Problem #1039 — Minimum Score Triangulation of Polygon**
Solve LeetCode Minimum Score Triangulation of Polygon using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Score Triangulation of Polygon |
| LeetCode | #1039 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You have a convex `n`-sided polygon where each vertex has an integer value. You are given an integer array `values` where `values[i]` is the value of the `i^th` vertex in **clockwise order**.

**Polygon** **triangulation** is a process where you divide a polygon into a set of triangles and the vertices of each triangle must also be vertices of the original polygon. Note that no other shapes other than triangles are allowed in the division. This process will result in `n - 2` triangles.

You will **triangulate** the polygon. For each triangle, the *weight* of that triangle is the product of the values at its vertices. The total score of the triangulation is the sum of these *weights* over all `n - 2` triangles.

Return the* minimum possible score *that you can achieve with some* ***triangulation*** *of the polygon.

## Constraints
- `n == values.length`
- `3 <= n <= 50`
- `1 <= values[i] <= 100`

## Examples
### Example 1
- **Input:** `values = [1,2,3]`
- **Output:** `6`
- **Explanation:** The polygon is already triangulated, and the score of the only triangle is 6.

### Example 2
- **Input:** `values = [3,7,4,5]`
- **Output:** `144`
- **Explanation:** There are two triangulations, with possible scores: 3*7*5 + 4*5*7 = 245, or 3*4*5 + 3*4*7 = 144. 
The minimum score is 144.

### Example 3
- **Input:** `values = [1,3,1,4,1,5]`
- **Output:** `13`
- **Explanation:** The minimum score triangulation is 1*1*3 + 1*1*4 + 1*1*5 + 1*1*1 = 13.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Minimum Score Triangulation of Polygon**, we observe the problem requirements and utilize the **Array / General** technique. We decompose the problem into overlapping subproblems using a **Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `values = [1,2,3]`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `6`.
4. **Verification:** The polygon is already triangulated, and the score of the only triangle is 6.

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
class Solution:
    def minScoreTriangulation(self, values: list[int]) -> int:
        n = len(values)
        dp = [[0] * n for _ in range(n)]
        
        for length in range(2, n):
            for i in range(n - length):
                j = i + length
                base_prod = values[i] * values[j]
                dp[i][j] = min(
                    dp[i][k] + dp[k][j] + base_prod * values[k]
                    for k in range(i + 1, j)
                )
                
        return dp[0][n - 1]
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
- [2139. Minimum Moves to Reach Target Score](../../2001-2500/2139-minimum-moves-to-reach-target-score/)
- [2322. Minimum Score After Removals on a Tree](../../2001-2500/2322-minimum-score-after-removals-on-a-tree/)
- [2492. Minimum Score of a Path Between Two Cities](../../2001-2500/2492-minimum-score-of-a-path-between-two-cities/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-score-triangulation-of-polygon/)
