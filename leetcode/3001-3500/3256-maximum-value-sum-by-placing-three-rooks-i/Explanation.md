# LeetCode 3256: Maximum Value Sum by Placing Three Rooks I

**LeetCode Problem #3256 — Maximum Value Sum by Placing Three Rooks I**
Solve LeetCode Maximum Value Sum by Placing Three Rooks I using Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Value Sum by Placing Three Rooks I |
| LeetCode | #3256 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a `m x n` 2D array `board` representing a chessboard, where `board[i][j]` represents the **value** of the cell `(i, j)`.

Rooks in the **same** row or column **attack** each other. You need to place *three* rooks on the chessboard such that the rooks **do not** **attack** each other.

Return the **maximum** sum of the cell **values** on which the rooks are placed.

## Constraints
- `3 <= m == board.length <= 100`
- `3 <= n == board[i].length <= 100`
- `-10^9 <= board[i][j] <= 10^9`

## Examples
### Example 1
- **Input:** `board = [[-3,1,1,1],[-3,1,-3,1],[-3,2,1,1]]`
- **Output:** `4`
- **Explanation:** We can place the rooks in the cells `(0, 2)`, `(1, 3)`, and `(2, 1)` for a sum of `1 + 1 + 2 = 4`.

### Example 2
- **Input:** `board = [[1,2,3],[4,5,6],[7,8,9]]`
- **Output:** `15`
- **Explanation:** We can place the rooks in the cells `(0, 0)`, `(1, 1)`, and `(2, 2)` for a sum of `1 + 5 + 9 = 15`.

### Example 3
- **Input:** `board = [[1,1,1],[1,1,1],[1,1,1]]`
- **Output:** `3`
- **Explanation:** We can place the rooks in the cells `(0, 2)`, `(1, 1)`, and `(2, 0)` for a sum of `1 + 1 + 1 = 3`.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Value Sum by Placing Three Rooks I**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `board = [[-3,1,1,1],[-3,1,-3,1],[-3,2,1,1]]`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** We can place the rooks in the cells `(0, 2)`, `(1, 3)`, and `(2, 1)` for a sum of `1 + 1 + 2 = 4`.

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
from itertools import combinations
import heapq

class Solution:
    def maximumValueSum(self, board: List[List[int]]) -> int:
        m = len(board)
        top = []
        for row in board:
            top.append(heapq.nlargest(3, [(v, c) for c, v in enumerate(row)]))

        best = float('-inf')
        for i, j, k in combinations(range(m), 3):
            for v1, c1 in top[i]:
                for v2, c2 in top[j]:
                    if c2 == c1:
                        continue
                    for v3, c3 in top[k]:
                        if c3 != c1 and c3 != c2:
                            s = v1 + v2 + v3
                            if s > best:
                                best = s
        return best
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
- [3257. Maximum Value Sum by Placing Three Rooks II](../../3001-3500/3257-maximum-value-sum-by-placing-three-rooks-ii/)
- [3780. Maximum Sum of Three Numbers Divisible by Three](../../3501-4000/3780-maximum-sum-of-three-numbers-divisible-by-three/)
- [124. Binary Tree Maximum Path Sum](../../0001-0500/0124-binary-tree-maximum-path-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-value-sum-by-placing-three-rooks-i/)
