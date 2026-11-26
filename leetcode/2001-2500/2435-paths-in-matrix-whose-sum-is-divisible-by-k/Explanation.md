# LeetCode 2435: Paths in Matrix Whose Sum Is Divisible by K

**LeetCode Problem #2435 — Paths in Matrix Whose Sum Is Divisible by K**
Solve LeetCode Paths in Matrix Whose Sum Is Divisible by K using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Paths in Matrix Whose Sum Is Divisible by K |
| LeetCode | #2435 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a **0-indexed** `m x n` integer matrix `grid` and an integer `k`. You are currently at position `(0, 0)` and you want to reach position `(m - 1, n - 1)` moving only **down** or **right**.

Return* the number of paths where the sum of the elements on the path is divisible by *`k`. Since the answer may be very large, return it **modulo** `10^9 + 7`.

## Constraints
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 5 * 10^4`
- `1 <= m * n <= 5 * 10^4`
- `0 <= grid[i][j] <= 100`
- `1 <= k <= 50`

## Examples
### Example 1
- **Input:** `grid = [[5,2,4],[3,0,5],[0,7,2]], k = 3`
- **Output:** `2`
- **Explanation:** There are two paths where the sum of the elements on the path is divisible by k.
The first path highlighted in red has a sum of 5 + 2 + 4 + 5 + 2 = 18 which is divisible by 3.
The second path highlighted in blue has a sum of 5 + 3 + 0 + 5 + 2 = 15 which is divisible by 3.

### Example 2
- **Input:** `grid = [[0,0]], k = 5`
- **Output:** `1`
- **Explanation:** The path highlighted in red has a sum of 0 + 0 = 0 which is divisible by 5.

### Example 3
- **Input:** `grid = [[7,3,4,9],[2,3,6,2],[2,3,7,0]], k = 1`
- **Output:** `10`
- **Explanation:** Every integer is divisible by 1 so the sum of the elements on every possible path is divisible by k.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Paths in Matrix Whose Sum Is Divisible by K**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [[5,2,4],[3,0,5],[0,7,2]], k = 3`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** There are two paths where the sum of the elements on the path is divisible by k.
The first path highlighted in red has a sum of 5 + 2 + 4 + 5 + 2 = 18 which is divisible by 3.
The second path highlighted in blue has a sum of 5 + 3 + 0 + 5 + 2 = 15 which is divisible by 3.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Dictionary / Hash Map.

## Pattern
**Hash Map**

## Topics
- Hash Table
- Array
- Complement Lookup

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        prev = [[0] * k for _ in range(n)]  # dp for the previous row

        for i in range(m):
            cur = [[0] * k for _ in range(n)]
            for j in range(n):
                v = grid[i][j] % k
                if i == 0 and j == 0:
                    cur[0][v] = 1
                    continue
                up = prev[j]
                left = cur[j - 1] if j > 0 else None
                for r in range(k):
                    total = up[r]
                    if left is not None:
                        total += left[r]
                    if total:
                        cur[j][(r + v) % k] = total % MOD
            prev = cur

        return prev[n - 1][0]
```

## Why This Works
By utilizing **Hash Map**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Using the same element twice.
2. Checking the map before inserting elements in the correct order.
3. Inefficient hash functions or unnecessary duplicate key updates.

## Interview Notes
- **Tests:** Hash map usage, complement/frequency lookup, and $O(n)$ time optimization.
- **Follow-up:** Can you solve the problem in $O(1)$ extra space if the input array is sorted?

## Related Problems
- [3381. Maximum Subarray Sum With Length Divisible by K](../../3001-3500/3381-maximum-subarray-sum-with-length-divisible-by-k/)
- [3712. Sum of Elements With Frequency Divisible by K](../../3501-4000/3712-sum-of-elements-with-frequency-divisible-by-k/)
- [363. Max Sum of Rectangle No Larger Than K](../../0001-0500/0363-max-sum-of-rectangle-no-larger-than-k/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k/)
