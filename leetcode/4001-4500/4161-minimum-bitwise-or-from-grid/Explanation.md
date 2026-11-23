# LeetCode 3858: Minimum Bitwise OR From Grid

**LeetCode Problem #3858 — Minimum Bitwise OR From Grid**
Solve LeetCode Minimum Bitwise OR From Grid using Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Bitwise OR From Grid |
| LeetCode | #3858 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a 2D integer array `grid` of size `m x n`.

You must select **exactly one** integer from each row of the grid.

Return an integer denoting the **minimum possible bitwise OR** of the selected integers from each row.

## Constraints
- `1 <= m == grid.length <= 10^5`
- `1 <= n == grid[i].length <= 10^5`
- `m * n <= 10^5`
- `1 <= grid[i][j] <= 10^5​​​​​​​`

## Examples
### Example 1
- **Input:** `grid = [[1,5],[2,4]]`
- **Output:** `3`
- **Explanation:** Choose 1 from the first row and 2 from the second row. 
 The bitwise OR of `1 | 2 = 3`​​​​​​​, which is the minimum possible.

### Example 2
- **Input:** `grid = [[3,5],[6,4]]`
- **Output:** `5`
- **Explanation:** Choose 5 from the first row and 4 from the second row. 
 The bitwise OR of `5 | 4 = 5`​​​​​​​, which is the minimum possible.

### Example 3
- **Input:** `grid = [[7,9,8]]`
- **Output:** `7`
- **Explanation:** Choosing 7 gives the minimum bitwise OR.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Bitwise OR From Grid**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [[1,5],[2,4]]`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** Choose 1 from the first row and 2 from the second row. 
 The bitwise OR of `1 | 2 = 3`​​​​​​​, which is the minimum possible.

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
    def minimumOR(self, grid):
        ans = (1 << 17) - 1
        for b in range(16, -1, -1):
            cand = ans ^ (1 << b)
            ok = True
            for row in grid:
                found = False
                for x in row:
                    if x | cand == cand:
                        found = True
                        break
                if not found:
                    ok = False
                    break
            if ok:
                ans = cand
        return ans
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
- [3314. Construct the Minimum Bitwise Array I](../../3501-4000/3605-construct-the-minimum-bitwise-array-i/)
- [3315. Construct the Minimum Bitwise Array II](../../3501-4000/3611-construct-the-minimum-bitwise-array-ii/)
- [1130. Minimum Cost Tree From Leaf Values](../../1001-1500/1228-minimum-cost-tree-from-leaf-values/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-bitwise-or-from-grid/)
