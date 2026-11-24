# LeetCode 861: Score After Flipping Matrix

**LeetCode Problem #861 — Score After Flipping Matrix**
Solve LeetCode Score After Flipping Matrix using Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Score After Flipping Matrix |
| LeetCode | #861 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an `m x n` binary matrix `grid`.

A **move** consists of choosing any row or column and toggling each value in that row or column (i.e., changing all `0`'s to `1`'s, and all `1`'s to `0`'s).

Every row of the matrix is interpreted as a binary number, and the **score** of the matrix is the sum of these numbers.

Return *the highest possible **score** after making any number of **moves** (including zero moves)*.

## Constraints
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 20`
- `grid[i][j]` is either `0` or `1`.

## Examples
### Example 1
- **Input:** `grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]`
- **Output:** `39`
- **Explanation:** 0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39

### Example 2
- **Input:** `grid = [[0]]`
- **Output:** `1`

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Score After Flipping Matrix**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `39`.
4. **Verification:** 0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution(object):
    def matrixScore(self, grid):
        m, n = len(grid), len(grid[0])

        # Column 0 becomes all 1s after row flips: each row contributes 2^(n-1)
        score = m * (1 << (n - 1))

        for j in range(1, n):
            # Number of ones in column j after normalizing rows so grid[i][0] == 1
            ones = sum(grid[i][j] ^ grid[i][0] for i in range(m))
            # Flip the column if that gives more ones
            score += max(ones, m - ones) * (1 << (n - 1 - j))

        return score
```

## Why This Works
By utilizing **Stack & Queue**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [2946. Matrix Similarity After Cyclic Shifts](../../2501-3000/2946-matrix-similarity-after-cyclic-shifts/)
- [1422. Maximum Score After Splitting a String](../../1001-1500/1422-maximum-score-after-splitting-a-string/)
- [1799. Maximize Score After N Operations](../../1501-2000/1799-maximize-score-after-n-operations/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/score-after-flipping-matrix/)
