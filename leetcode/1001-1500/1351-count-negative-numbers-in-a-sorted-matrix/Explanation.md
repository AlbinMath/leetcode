# LeetCode 1351: Count Negative Numbers in a Sorted Matrix

**LeetCode Problem #1351 — Count Negative Numbers in a Sorted Matrix**
Solve LeetCode Count Negative Numbers in a Sorted Matrix using Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Negative Numbers in a Sorted Matrix |
| LeetCode | #1351 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given a `m x n` matrix `grid` which is sorted in non-increasing order both row-wise and column-wise, return *the number of **negative** numbers in* `grid`.

## Constraints
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 100`
- `-100 <= grid[i][j] <= 100`

## Examples
### Example 1
- **Input:** `grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]`
- **Output:** `8`
- **Explanation:** There are 8 negatives number in the matrix.

### Example 2
- **Input:** `grid = [[3,2],[1,0]]`
- **Output:** `0`

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Count Negative Numbers in a Sorted Matrix**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `8`.
4. **Verification:** There are 8 negatives number in the matrix.

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
    def countNegatives(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        row, col = m - 1, 0
        count = 0

        while row >= 0 and col < n:
            if grid[row][col] < 0:
                count += n - col
                row -= 1
            else:
                col += 1

        return count
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
- [378. Kth Smallest Element in a Sorted Matrix](../../0001-0500/0378-kth-smallest-element-in-a-sorted-matrix/)
- [1380. Lucky Numbers in a Matrix](../../1001-1500/1380-lucky-numbers-in-a-matrix/)
- [1439. Find the Kth Smallest Sum of a Matrix With Sorted Rows](../../1001-1500/1439-find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/)
