# LeetCode 2146: K Highest Ranked Items Within a Price Range

**LeetCode Problem #2146 — K Highest Ranked Items Within a Price Range**
Solve LeetCode K Highest Ranked Items Within a Price Range using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | K Highest Ranked Items Within a Price Range |
| LeetCode | #2146 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** 2D integer array `grid` of size `m x n` that represents a map of the items in a shop. The integers in the grid represent the following:

`0` represents a wall that you cannot pass through. 
 `1` represents an empty cell that you can freely move to and from. 
 All other positive integers represent the price of an item in that cell. You may also freely move to and from these item cells.

It takes `1` step to travel between adjacent grid cells.

You are also given integer arrays `pricing` and `start` where `pricing = [low, high]` and `start = [row, col]` indicates that you start at the position `(row, col)` and are interested only in items with a price in the range of `[low, high]` (**inclusive**). You are further given an integer `k`.

You are interested in the **positions** of the `k` **highest-ranked** items whose prices are **within** the given price range. The rank is determined by the **first** of these criteria that is different:

Distance, defined as the length of the shortest path from the `start` (**shorter** distance has a higher rank). 
 Price (**lower** price has a higher rank, but it must be **in the price range**). 
 The row number (**smaller** row number has a higher rank). 
 The column number (**smaller** column number has a higher rank).

Return *the *`k`* highest-ranked items within the price range **sorted** by their rank (highest to lowest)*. If there are fewer than `k` reachable items within the price range, return ***all** of them*.

## Constraints
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 10^5`
- `1 <= m * n <= 10^5`
- `0 <= grid[i][j] <= 10^5`
- `pricing.length == 2`
- `2 <= low <= high <= 10^5`
- `start.length == 2`
- `0 <= row <= m - 1`
- `0 <= col <= n - 1`
- `grid[row][col] > 0`
- `1 <= k <= m * n`

## Examples
### Example 1
- **Input:** `grid = [[1,2,0,1],[1,3,0,1],[0,2,5,1]], pricing = [2,5], start = [0,0], k = 3`
- **Output:** `[[0,1],[1,1],[2,1]]`
- **Explanation:** You start at (0,0).
With a price range of [2,5], we can take items from (0,1), (1,1), (2,1) and (2,2).
The ranks of these items are:
- (0,1) with distance 1
- (1,1) with distance 2
- (2,1) with distance 3
- (2,2) with distance 4
Thus, the 3 highest ranked items in the price range are (0,1), (1,1), and (2,1).

### Example 2
- **Input:** `grid = [[1,2,0,1],[1,3,3,1],[0,2,5,1]], pricing = [2,3], start = [2,3], k = 2`
- **Output:** `[[2,1],[1,2]]`
- **Explanation:** You start at (2,3).
With a price range of [2,3], we can take items from (0,1), (1,1), (1,2) and (2,1).
The ranks of these items are:
- (2,1) with distance 2, price 2
- (1,2) with distance 2, price 3
- (1,1) with distance 3
- (0,1) with distance 4
Thus, the 2 highest ranked items in the price range are (2,1) and (1,2).

### Example 3
- **Input:** `grid = [[1,1,1],[0,0,1],[2,3,4]], pricing = [2,3], start = [0,0], k = 3`
- **Output:** `[[2,1],[2,0]]`
- **Explanation:** You start at (0,0).
With a price range of [2,3], we can take items from (2,0) and (2,1). 
The ranks of these items are: 
- (2,1) with distance 5
- (2,0) with distance 6
Thus, the 2 highest ranked items in the price range are (2,1) and (2,0). 
Note that k = 3 but there are only 2 reachable items within the price range.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **K Highest Ranked Items Within a Price Range**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [[1,2,0,1],[1,3,0,1],[0,2,5,1]], pricing = [2,5], start = [0,0], k = 3`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[[0,1],[1,1],[2,1]]`.
4. **Verification:** You start at (0,0).
With a price range of [2,5], we can take items from (0,1), (1,1), (2,1) and (2,2).
The ranks of these items are:
- (0,1) with distance 1
- (1,1) with distance 2
- (2,1) with distance 3
- (2,2) with distance 4
Thus, the 3 highest ranked items in the price range are (0,1), (1,1), and (2,1).

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
from typing import List

class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        low, high = pricing
        sr, sc = start

        seen = [[False] * n for _ in range(m)]
        seen[sr][sc] = True
        layer = [(sr, sc)]
        ans = []

        while layer and len(ans) < k:
            items = []
            nxt = []
            for r, c in layer:
                p = grid[r][c]
                if low <= p <= high:
                    items.append((p, r, c))
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] != 0 and not seen[nr][nc]:
                        seen[nr][nc] = True
                        nxt.append((nr, nc))
            items.sort()
            for p, r, c in items:
                ans.append([r, c])
            layer = nxt

        return ans[:k]
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
- [787. Cheapest Flights Within K Stops](../../0501-1000/0787-cheapest-flights-within-k-stops/)
- [3505. Minimum Operations to Make Elements Within K Subarrays Equal](../../3501-4000/3505-minimum-operations-to-make-elements-within-k-subarrays-equal/)
- [3824. Minimum K to Reduce Array Within Limit](../../3501-4000/3824-minimum-k-to-reduce-array-within-limit/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/k-highest-ranked-items-within-a-price-range/)
