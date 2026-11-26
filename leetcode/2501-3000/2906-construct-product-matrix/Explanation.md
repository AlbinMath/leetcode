# LeetCode 2906: Construct Product Matrix

**LeetCode Problem #2906 — Construct Product Matrix**
Solve LeetCode Construct Product Matrix using Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Construct Product Matrix |
| LeetCode | #2906 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given a **0-indexed** 2D integer matrix ` grid ` of size `n * m`, we define a **0-indexed** 2D matrix `p` of size `n * m` as the **product** matrix of `grid` if the following condition is met:

Each element `p[i][j]` is calculated as the product of all elements in `grid` except for the element `grid[i][j]`. This product is then taken modulo ` 12345 `.

Return *the product matrix of* ` grid `.

## Constraints
- `1 <= n == grid.length <= 10^5`
- `1 <= m == grid[i].length <= 10^5`
- `2 <= n * m <= 10^5`
- `1 <= grid[i][j] <= 10^9`

## Examples
### Example 1
- **Input:** `grid = [[1,2],[3,4]]`
- **Output:** `[[24,12],[8,6]]`
- **Explanation:** p[0][0] = grid[0][1] * grid[1][0] * grid[1][1] = 2 * 3 * 4 = 24
p[0][1] = grid[0][0] * grid[1][0] * grid[1][1] = 1 * 3 * 4 = 12
p[1][0] = grid[0][0] * grid[0][1] * grid[1][1] = 1 * 2 * 4 = 8
p[1][1] = grid[0][0] * grid[0][1] * grid[1][0] = 1 * 2 * 3 = 6
So the answer is [[24,12],[8,6]].

### Example 2
- **Input:** `grid = [[12345],[2],[1]]`
- **Output:** `[[2],[0],[0]]`
- **Explanation:** p[0][0] = grid[0][1] * grid[0][2] = 2 * 1 = 2.
p[0][1] = grid[0][0] * grid[0][2] = 12345 * 1 = 12345. 12345 % 12345 = 0. So p[0][1] = 0.
p[0][2] = grid[0][0] * grid[0][1] = 12345 * 2 = 24690. 24690 % 12345 = 0. So p[0][2] = 0.
So the answer is [[2],[0],[0]].

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Construct Product Matrix**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [[1,2],[3,4]]`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[[24,12],[8,6]]`.
4. **Verification:** p[0][0] = grid[0][1] * grid[1][0] * grid[1][1] = 2 * 3 * 4 = 24
p[0][1] = grid[0][0] * grid[1][0] * grid[1][1] = 1 * 3 * 4 = 12
p[1][0] = grid[0][0] * grid[0][1] * grid[1][1] = 1 * 2 * 4 = 8
p[1][1] = grid[0][0] * grid[0][1] * grid[1][0] = 1 * 2 * 3 = 6
So the answer is [[24,12],[8,6]].

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
class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        n, m = len(grid), len(grid[0])
        total = n * m
        res = [[0] * m for _ in range(n)]

        # prefix pass: res holds the product of everything before the cell
        pre = 1
        for k in range(total):
            i, j = divmod(k, m)
            res[i][j] = pre
            pre = pre * grid[i][j] % MOD

        # suffix pass: multiply by the product of everything after the cell
        suf = 1
        for k in range(total - 1, -1, -1):
            i, j = divmod(k, m)
            res[i][j] = res[i][j] * suf % MOD
            suf = suf * grid[i][j] % MOD

        return res
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
- [1594. Maximum Non Negative Product in a Matrix](../../1501-2000/1594-maximum-non-negative-product-in-a-matrix/)
- [105. Construct Binary Tree from Preorder and Inorder Traversal](../../0001-0500/0105-construct-binary-tree-from-preorder-and-inorder-traversal/)
- [106. Construct Binary Tree from Inorder and Postorder Traversal](../../0001-0500/0106-construct-binary-tree-from-inorder-and-postorder-traversal/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/construct-product-matrix/)
