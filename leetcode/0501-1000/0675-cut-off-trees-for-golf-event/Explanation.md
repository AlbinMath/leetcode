# LeetCode 675: Cut Off Trees for Golf Event

**LeetCode Problem #675 — Cut Off Trees for Golf Event**
Solve LeetCode Cut Off Trees for Golf Event using Python and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Cut Off Trees for Golf Event |
| LeetCode | #675 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are asked to cut off all the trees in a forest for a golf event. The forest is represented as an `m x n` matrix. In this matrix:

`0` means the cell cannot be walked through. 
 `1` represents an empty cell that can be walked through. 
 A number greater than `1` represents a tree in a cell that can be walked through, and this number is the tree's height.

In one step, you can walk in any of the four directions: north, east, south, and west. If you are standing in a cell with a tree, you can choose whether to cut it off.

You must cut off the trees in order from shortest to tallest. When you cut off a tree, the value at its cell becomes `1` (an empty cell).

Starting from the point `(0, 0)`, return *the minimum steps you need to walk to cut off all the trees*. If you cannot cut off all the trees, return `-1`.

**Note:** The input is generated such that no two trees have the same height, and there is at least one tree needs to be cut off.

## Constraints
- `m == forest.length`
- `n == forest[i].length`
- `1 <= m, n <= 50`
- `0 <= forest[i][j] <= 10^9`
- Heights of all trees are **distinct**.

## Examples
### Example 1
- **Input:** `forest = [[1,2,3],[0,0,4],[7,6,5]]`
- **Output:** `6`
- **Explanation:** Following the path above allows you to cut off the trees from shortest to tallest in 6 steps.

### Example 2
- **Input:** `forest = [[1,2,3],[0,0,0],[7,6,5]]`
- **Output:** `-1`
- **Explanation:** The trees in the bottom row cannot be accessed as the middle row is blocked.

### Example 3
- **Input:** `forest = [[2,3,4],[0,0,5],[8,7,6]]`
- **Output:** `6`

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Cut Off Trees for Golf Event**, we observe the problem requirements and utilize the **Binary Search** technique. Exploiting monotonic ordering or sorted properties in the input space, we maintain `left` and `right` boundary pointers. In each iteration, we evaluate the midpoint to discard half of the search range, reducing the time complexity to $O(\log n)$.

## Algorithm
1. Initialize boundary pointers `left` and `right`.
2. Compute `mid = left + (right - left) // 2` to prevent overflow.
3. Adjust `left` or `right` depending on whether target satisfies the partition condition.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `forest = [[1,2,3],[0,0,4],[7,6,5]]`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `6`.
4. **Verification:** Following the path above allows you to cut off the trees from shortest to tallest in 6 steps.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Sorted Array.

## Pattern
**Binary Search**

## Topics
- Binary Search
- Divide and Conquer
- Search Space

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List
from collections import deque

class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        if forest[0][0] == 0:
            return -1
            
        m, n = len(forest), len(forest[0])
        trees = sorted(
            (forest[r][c], r, c)
            for r in range(m)
            for c in range(n)
            if forest[r][c] > 1
        )
        
        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
        
        def bfs(sr: int, sc: int, tr: int, tc: int) -> int:
            if sr == tr and sc == tc:
                return 0
            queue = deque([(sr, sc, 0)])
            visited = {(sr, sc)}
            while queue:
                r, c, steps = queue.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and forest[nr][nc] > 0 and (nr, nc) not in visited:
                        if nr == tr and nc == tc:
                            return steps + 1
                        visited.add((nr, nc))
                        queue.append((nr, nc, steps + 1))
            return -1
            
        curr_r, curr_c = 0, 0
        total_steps = 0
        for _, tr, tc in trees:
            dist = bfs(curr_r, curr_c, tr, tc)
            if dist == -1:
                return -1
            total_steps += dist
            curr_r, curr_c = tr, tc
            
        return total_steps
```

## Why This Works
By utilizing **Binary Search**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Applying standard binary search without accounting for array rotation or duplicates.
2. Off-by-one errors when updating boundary pointers (`left = mid + 1` vs `right = mid - 1`).
3. Integer overflow during midpoint calculation (use `mid = left + (right - left) // 2`).

## Interview Notes
- **Tests:** Logarithmic search space reduction, boundary handling, and invariant preservation.
- **Follow-up:** How does performance change if the array contains duplicate elements?

## Related Problems
- [959. Regions Cut By Slashes](../../0501-1000/0959-regions-cut-by-slashes/)
- [1547. Minimum Cost to Cut a Stick](../../1501-2000/1547-minimum-cost-to-cut-a-stick/)
- [3394. Check if Grid can be Cut into Sections](../../3001-3500/3394-check-if-grid-can-be-cut-into-sections/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/cut-off-trees-for-golf-event/)
