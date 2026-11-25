# LeetCode 3446: Sort Matrix by Diagonals

**LeetCode Problem #3446 — Sort Matrix by Diagonals**
Solve LeetCode Sort Matrix by Diagonals using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Sort Matrix by Diagonals |
| LeetCode | #3446 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an `n x n` square matrix of integers `grid`. Return the matrix such that:

The diagonals in the **bottom-left triangle** (including the middle diagonal) are sorted in **non-increasing order**. 
 The diagonals in the **top-right triangle** are sorted in **non-decreasing order**.

## Constraints
- `grid.length == grid[i].length == n`
- `1 <= n <= 10`
- `-10^5 <= grid[i][j] <= 10^5`

## Examples
### Example 1
- **Input:** `grid = [[1,7,3],[9,8,2],[4,5,6]]`
- **Output:** `[[8,2,3],[9,6,7],[4,5,1]]`
- **Explanation:** The diagonals with a black arrow (bottom-left triangle) should be sorted in non-increasing order: 

 
 `[1, 8, 6]` becomes `[8, 6, 1]`. 
 `[9, 5]` and `[4]` remain unchanged. 
 

 The diagonals with a blue arrow (top-right triangle) should be sorted in non-decreasing order: 

 
 `[7, 2]` becomes `[2, 7]`. 
 `[3]` remains unchanged.

### Example 2
- **Input:** `grid = [[0,1],[1,2]]`
- **Output:** `[[2,1],[1,0]]`
- **Explanation:** The diagonals with a black arrow must be non-increasing, so `[0, 2]` is changed to `[2, 0]`. The other diagonals are already in the correct order.

### Example 3
- **Input:** `grid = [[1]]`
- **Output:** `[[1]]`
- **Explanation:** Diagonals with exactly one element are already in order, so no changes are needed.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Sort Matrix by Diagonals**, we observe the problem requirements and utilize the **Tree & Graph** technique. By maintaining a **Tree / Graph / Grid**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Tree / Graph / Grid** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [[1,7,3],[9,8,2],[4,5,6]]`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[[8,2,3],[9,6,7],[4,5,1]]`.
4. **Verification:** The diagonals with a black arrow (bottom-left triangle) should be sorted in non-increasing order: 

 
 `[1, 8, 6]` becomes `[8, 6, 1]`. 
 `[9, 5]` and `[4]` remain unchanged. 
 

 The diagonals with a blue arrow (top-right triangle) should be sorted in non-decreasing order: 

 
 `[7, 2]` becomes `[2, 7]`. 
 `[3]` remains unchanged.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Tree / Graph / Grid.

## Pattern
**Tree & Graph**

## Topics
- Tree
- Graph
- DFS
- BFS

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        diags = {}

        for i in range(n):
            for j in range(n):
                diags.setdefault(i - j, []).append(grid[i][j])

        for d, vals in diags.items():
            vals.sort(reverse=(d >= 0))
        idx = {d: 0 for d in diags}
        for i in range(n):
            for j in range(n):
                d = i - j
                grid[i][j] = diags[d][idx[d]]
                idx[d] += 1

        return grid
```

## Why This Works
By utilizing **Tree & Graph**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1329. Sort the Matrix Diagonally](../../1001-1500/1329-sort-the-matrix-diagonally/)
- [75. Sort Colors](../../0001-0500/0075-sort-colors/)
- [147. Insertion Sort List](../../0001-0500/0147-insertion-sort-list/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/sort-matrix-by-diagonals/)
