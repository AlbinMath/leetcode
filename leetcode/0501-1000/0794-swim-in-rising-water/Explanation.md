# LeetCode 778: Swim in Rising Water

**LeetCode Problem #778 — Swim in Rising Water**
Solve LeetCode Swim in Rising Water using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Swim in Rising Water |
| LeetCode | #778 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an `n x n` integer matrix `grid` where each value `grid[i][j]` represents the elevation at that point `(i, j)`.

It starts raining, and water gradually rises over time. At time `t`, the water level is `t`, meaning **any** cell with elevation less than equal to `t` is submerged or reachable.

You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most `t`. You can swim infinite distances in zero time. Of course, you must stay within the boundaries of the grid during your swim.

Return *the minimum time until you can reach the bottom right square *`(n - 1, n - 1)`* if you start at the top left square *`(0, 0)`.

## Constraints
- `n == grid.length`
- `n == grid[i].length`
- `1 <= n <= 50`
- `0 <= grid[i][j] < n^2`
- Each value `grid[i][j]` is **unique**.

## Examples
### Example 1
- **Input:** `grid = [[0,2],[1,3]]`
- **Output:** `3`

### Example 2
- **Input:** `grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]`
- **Output:** `16`
- **Explanation:** The final route is shown.
We need to wait until time 16 so that (0, 0) and (4, 4) are connected.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Swim in Rising Water**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [[0,2],[1,3]]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
import heapq

class Solution:
    def swimInWater(self, grid):
        n = len(grid)
        q = [(grid[0][0], 0, 0)]
        seen = {(0, 0)}

        while q:
            t, r, c = heapq.heappop(q)
            if (r, c) == (n-1, n-1):
                return t
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                x, y = r+dr, c+dc
                if 0 <= x < n and 0 <= y < n and (x,y) not in seen:
                    seen.add((x,y))
                    heapq.heappush(q, (max(t, grid[x][y]), x, y))
```

## Why This Works
By utilizing **Array / General**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [197. Rising Temperature](../../0001-0500/0197-rising-temperature/)
- [11. Container With Most Water](../../0001-0500/0011-container-with-most-water/)
- [42. Trapping Rain Water](../../0001-0500/0042-trapping-rain-water/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/swim-in-rising-water/)
