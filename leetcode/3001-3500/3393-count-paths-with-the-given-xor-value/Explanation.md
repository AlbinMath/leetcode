# LeetCode 3393: Count Paths With the Given XOR Value

**LeetCode Problem #3393 — Count Paths With the Given XOR Value**
Solve LeetCode Count Paths With the Given XOR Value using Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Paths With the Given XOR Value |
| LeetCode | #3393 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a 2D integer array `grid` with size `m x n`. You are also given an integer `k`.

Your task is to calculate the number of paths you can take from the top-left cell `(0, 0)` to the bottom-right cell `(m - 1, n - 1)` satisfying the following **constraints**:

You can either move to the right or down. Formally, from the cell `(i, j)` you may move to the cell `(i, j + 1)` or to the cell `(i + 1, j)` if the target cell *exists*. 
 The `XOR` of all the numbers on the path must be **equal** to `k`.

Return the total number of such paths.

Since the answer can be very large, return the result **modulo** `10^9 + 7`.

## Constraints
- You can either move to the right or down. Formally, from the cell `(i, j)` you may move to the cell `(i, j + 1)` or to the cell `(i + 1, j)` if the target cell *exists*.
- The `XOR` of all the numbers on the path must be **equal** to `k`.
- `(0, 0) &rarr; (1, 0) &rarr; (2, 0) &rarr; (2, 1) &rarr; (2, 2)`
- `(0, 0) &rarr; (1, 0) &rarr; (1, 1) &rarr; (1, 2) &rarr; (2, 2)`
- `(0, 0) &rarr; (0, 1) &rarr; (1, 1) &rarr; (2, 1) &rarr; (2, 2)`
- `(0, 0) &rarr; (1, 0) &rarr; (2, 0) &rarr; (2, 1) &rarr; (2, 2) &rarr; (2, 3)`
- `(0, 0) &rarr; (1, 0) &rarr; (1, 1) &rarr; (2, 1) &rarr; (2, 2) &rarr; (2, 3)`
- `(0, 0) &rarr; (1, 0) &rarr; (1, 1) &rarr; (1, 2) &rarr; (1, 3) &rarr; (2, 3)`
- `(0, 0) &rarr; (0, 1) &rarr; (1, 1) &rarr; (1, 2) &rarr; (2, 2) &rarr; (2, 3)`
- `(0, 0) &rarr; (0, 1) &rarr; (0, 2) &rarr; (1, 2) &rarr; (2, 2) &rarr; (2, 3)`
- `1 <= m == grid.length <= 300`
- `1 <= n == grid[r].length <= 300`
- `0 <= grid[r][c] < 16`
- `0 <= k < 16`

## Examples
### Example 1
- **Input:** `grid = [[2, 1, 5], [7, 10, 0], [12, 6, 4]], k = 11`
- **Output:** `3`
- **Explanation:** The 3 paths are: 

 
 `(0, 0) &rarr; (1, 0) &rarr; (2, 0) &rarr; (2, 1) &rarr; (2, 2)` 
 `(0, 0) &rarr; (1, 0) &rarr; (1, 1) &rarr; (1, 2) &rarr; (2, 2)` 
 `(0, 0) &rarr; (0, 1) &rarr; (1, 1) &rarr; (2, 1) &rarr; (2, 2)`

### Example 2
- **Input:** `grid = [[1, 3, 3, 3], [0, 3, 3, 2], [3, 0, 1, 1]], k = 2`
- **Output:** `5`
- **Explanation:** The 5 paths are: 

 
 `(0, 0) &rarr; (1, 0) &rarr; (2, 0) &rarr; (2, 1) &rarr; (2, 2) &rarr; (2, 3)` 
 `(0, 0) &rarr; (1, 0) &rarr; (1, 1) &rarr; (2, 1) &rarr; (2, 2) &rarr; (2, 3)` 
 `(0, 0) &rarr; (1, 0) &rarr; (1, 1) &rarr; (1, 2) &rarr; (1, 3) &rarr; (2, 3)` 
 `(0, 0) &rarr; (0, 1) &rarr; (1, 1) &rarr; (1, 2) &rarr; (2, 2) &rarr; (2, 3)` 
 `(0, 0) &rarr; (0, 1) &rarr; (0, 2) &rarr; (1, 2) &rarr; (2, 2) &rarr; (2, 3)`

### Example 3
- **Input:** `grid = [[1, 1, 1, 2], [3, 0, 3, 2], [3, 0, 2, 2]], k = 10`
- **Output:** `0`

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Count Paths With the Given XOR Value**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [[2, 1, 5], [7, 10, 0], [12, 6, 4]], k = 11`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** The 3 paths are: 

 
 `(0, 0) &rarr; (1, 0) &rarr; (2, 0) &rarr; (2, 1) &rarr; (2, 2)` 
 `(0, 0) &rarr; (1, 0) &rarr; (1, 1) &rarr; (1, 2) &rarr; (2, 2)` 
 `(0, 0) &rarr; (0, 1) &rarr; (1, 1) &rarr; (2, 1) &rarr; (2, 2)`

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
    def countPathsWithXorValue(self, grid, k):
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        prev = [[0] * 16 for _ in range(n)]
        for i in range(m):
            cur = [[0] * 16 for _ in range(n)]
            for j in range(n):
                g = grid[i][j]
                if i == 0 and j == 0:
                    cur[0][g] = 1
                    continue
                up = prev[j] if i > 0 else None
                left = cur[j - 1] if j > 0 else None
                row = cur[j]
                for x in range(16):
                    t = x ^ g
                    v = 0
                    if up is not None:
                        v += up[t]
                    if left is not None:
                        v += left[t]
                    row[x] = v % MOD
            prev = cur
        return prev[n - 1][k]
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
- [828. Count Unique Characters of All Substrings of a Given String](../../0501-1000/0828-count-unique-characters-of-all-substrings-of-a-given-string/)
- [1442. Count Triplets That Can Form Two Arrays of Equal XOR](../../1001-1500/1442-count-triplets-that-can-form-two-arrays-of-equal-xor/)
- [1803. Count Pairs With XOR in a Range](../../1501-2000/1803-count-pairs-with-xor-in-a-range/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-paths-with-the-given-xor-value/)
