# LeetCode 1765: Map of Highest Peak

**LeetCode Problem #1765 — Map of Highest Peak**
Solve LeetCode Map of Highest Peak using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Map of Highest Peak |
| LeetCode | #1765 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer matrix `isWater` of size `m x n` that represents a map of **land** and **water** cells.

If `isWater[i][j] == 0`, cell `(i, j)` is a **land** cell. 
 If `isWater[i][j] == 1`, cell `(i, j)` is a **water** cell.

You must assign each cell a height in a way that follows these rules:

The height of each cell must be non-negative. 
 If the cell is a **water** cell, its height must be `0`. 
 Any two adjacent cells must have an absolute height difference of **at most** `1`. A cell is adjacent to another cell if the former is directly north, east, south, or west of the latter (i.e., their sides are touching).

Find an assignment of heights such that the maximum height in the matrix is **maximized**.

Return *an integer matrix *`height`* of size *`m x n`* where *`height[i][j]`* is cell *`(i, j)`*'s height. If there are multiple solutions, return **any** of them*.

## Constraints
- `m == isWater.length`
- `n == isWater[i].length`
- `1 <= m, n <= 1000`
- `isWater[i][j]` is `0` or `1`.
- There is at least **one** water cell.

## Examples
### Example 1
- **Input:** `isWater = [[0,1],[0,0]]`
- **Output:** `[[1,0],[2,1]]`
- **Explanation:** The image shows the assigned heights of each cell.
The blue cell is the water cell, and the green cells are the land cells.

### Example 2
- **Input:** `isWater = [[0,0,1],[1,0,0],[0,0,0]]`
- **Output:** `[[1,1,0],[0,1,1],[1,2,2]]`
- **Explanation:** A height of 2 is the maximum possible height of any assignment.
Any height assignment that has a maximum height of 2 while still meeting the rules will also be accepted.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Map of Highest Peak**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `isWater = [[0,1],[0,0]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[[1,0],[2,1]]`.
4. **Verification:** The image shows the assigned heights of each cell.
The blue cell is the water cell, and the green cells are the land cells.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from collections import deque
class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        q = deque()
        h = [[-1]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if isWater[i][j]:
                    h[i][j] = 0
                    q.append((i,j))
        for i,j in q:
            pass
        while q:
            i,j = q.popleft()
            for x,y in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
                if 0 <= x < m and 0 <= y < n and h[x][y] == -1:
                    h[x][y] = h[i][j] + 1
                    q.append((x,y))
        return h
```

## Why This Works
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [677. Map Sum Pairs](../../0501-1000/0677-map-sum-pairs/)
- [176. Second Highest Salary](../../0001-0500/0176-second-highest-salary/)
- [177. Nth Highest Salary](../../0001-0500/0177-nth-highest-salary/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/map-of-highest-peak/)
