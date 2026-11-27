# LeetCode 2033: Minimum Operations to Make a Uni-Value Grid

**LeetCode Problem #2033 — Minimum Operations to Make a Uni-Value Grid**
Solve LeetCode Minimum Operations to Make a Uni-Value Grid using Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Operations to Make a Uni-Value Grid |
| LeetCode | #2033 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a 2D integer `grid` of size `m x n` and an integer `x`.

In one operation, you can **add** `x` to or **subtract** `x` from any element in the `grid`.

A **uni-value grid** is a grid where all the elements of it are equal.

Return the **minimum** number of operations to make the grid **uni-value**. If it is not possible, return -1.

## Constraints
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 10^5`
- `1 <= m * n <= 10^5`
- `1 <= x, grid[i][j] <= 10^4`

## Examples
### Example 1
- **Input:** `grid = [[2,4],[6,8]], x = 2`
- **Output:** `4`
- **Explanation:** We can make every element equal to 4 by doing the following: 
- Add x to 2 once.
- Subtract x from 6 once.
- Subtract x from 8 twice.
A total of 4 operations were used.

### Example 2
- **Input:** `grid = [[1,5],[2,3]], x = 1`
- **Output:** `5`
- **Explanation:** We can make every element equal to 3.

### Example 3
- **Input:** `grid = [[1,2],[3,4]], x = 2`
- **Output:** `-1`
- **Explanation:** It is impossible to make every element equal.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Operations to Make a Uni-Value Grid**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [[2,4],[6,8]], x = 2`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** We can make every element equal to 4 by doing the following: 
- Add x to 2 once.
- Subtract x from 6 once.
- Subtract x from 8 twice.
A total of 4 operations were used.

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
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        vals = [v for row in grid for v in row]
        r = vals[0] % x
        for v in vals:
            if v % x != r:
                return -1

        vals.sort()
        med = vals[len(vals) // 2]
        return sum(abs(v - med) // x for v in vals)
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
- [3066. Minimum Operations to Exceed Threshold Value II](../../3001-3500/3066-minimum-operations-to-exceed-threshold-value-ii/)
- [1368. Minimum Cost to Make at Least One Valid Path in a Grid](../../1001-1500/1368-minimum-cost-to-make-at-least-one-valid-path-in-a-grid/)
- [3071. Minimum Operations to Write the Letter Y on a Grid](../../3001-3500/3071-minimum-operations-to-write-the-letter-y-on-a-grid/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/)
