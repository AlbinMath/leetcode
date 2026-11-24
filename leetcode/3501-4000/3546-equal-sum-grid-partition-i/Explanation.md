# LeetCode 3546: Equal Sum Grid Partition I

**LeetCode Problem #3546 — Equal Sum Grid Partition I**
Solve LeetCode Equal Sum Grid Partition I using Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Equal Sum Grid Partition I |
| LeetCode | #3546 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an `m x n` matrix `grid` of positive integers. Your task is to determine if it is possible to make **either one horizontal or one vertical cut** on the grid such that:

Each of the two resulting sections formed by the cut is **non-empty**. 
 The sum of the elements in both sections is **equal**.

Return `true` if such a partition exists; otherwise return `false`.

## Constraints
- `1 <= m == grid.length <= 10^5`
- `1 <= n == grid[i].length <= 10^5`
- `2 <= m * n <= 10^5`
- `1 <= grid[i][j] <= 10^5`

## Examples
### Example 1
- **Input:** `grid = [[1,4],[2,3]]`
- **Output:** `true`
- **Explanation:** A horizontal cut between row 0 and row 1 results in two non-empty sections, each with a sum of 5. Thus, the answer is `true`.

### Example 2
- **Input:** `grid = [[1,3],[2,4]]`
- **Output:** `false`
- **Explanation:** No horizontal or vertical cut results in two non-empty sections with equal sums. Thus, the answer is `false`.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Equal Sum Grid Partition I**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [[1,4],[2,3]]`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** A horizontal cut between row 0 and row 1 results in two non-empty sections, each with a sum of 5. Thus, the answer is `true`.

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
from typing import List

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        total = sum(map(sum, grid))
        if total % 2:
            return False
        half = total // 2

        # horizontal cuts: after row i, for i in 0..m-2
        acc = 0
        for i in range(m - 1):
            acc += sum(grid[i])
            if acc == half:
                return True

        # vertical cuts: after column j, for j in 0..n-2
        col = [0] * n
        for row in grid:
            for j, v in enumerate(row):
                col[j] += v
        acc = 0
        for j in range(n - 1):
            acc += col[j]
            if acc == half:
                return True

        return False
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
- [3548. Equal Sum Grid Partition II](../../3501-4000/3548-equal-sum-grid-partition-ii/)
- [416. Partition Equal Subset Sum](../../0001-0500/0416-partition-equal-subset-sum/)
- [698. Partition to K Equal Sum Subsets](../../0501-1000/0698-partition-to-k-equal-sum-subsets/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/equal-sum-grid-partition-i/)
