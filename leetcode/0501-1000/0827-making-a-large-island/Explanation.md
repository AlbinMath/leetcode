# LeetCode 827: Making A Large Island

**LeetCode Problem #827 — Making A Large Island**
Solve LeetCode Making A Large Island using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Making A Large Island |
| LeetCode | #827 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an `n x n` binary matrix `grid`. You are allowed to change **at most one** `0` to be `1`.

Return *the size of the largest **island** in* `grid` *after applying this operation*.

An **island** is a 4-directionally connected group of `1`s.

## Constraints
- `n == grid.length`
- `n == grid[i].length`
- `1 <= n <= 500`
- `grid[i][j]` is either `0` or `1`.

## Examples
### Example 1
- **Input:** `grid = [[1,0],[0,1]]`
- **Output:** `3`
- **Explanation:** Change one 0 to 1 and connect two 1s, then we get an island with area = 3.

### Example 2
- **Input:** `grid = [[1,1],[1,0]]`
- **Output:** `4`
- **Explanation:** Change the 0 to 1 and make the island bigger, only one island with area = 4.

### Example 3
- **Input:** `grid = [[1,1],[1,1]]`
- **Output:** `4`
- **Explanation:** Can't change any 0 to 1, only one island with area = 4.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Making A Large Island**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [[1,0],[0,1]]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** Change one 0 to 1 and connect two 1s, then we get an island with area = 3.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Dictionary / Hash Map.

## Pattern
**Hash Map**

## Topics
- Hash Table
- Array
- Complement Lookup

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        island_id = 2
        area = {}
        
        # 1. Label each island and compute its size
        def dfs(r, c, label):
            count = 1
            grid[r][c] = label
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                    count += dfs(nr, nc, label)
            return count

        max_area = 0
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    size = dfs(r, c, island_id)
                    area[island_id] = size
                    max_area = max(max_area, size)
                    island_id += 1
                    
        # If the entire grid is already all 1s
        if max_area == n * n:
            return n * n

        # 2. Try flipping each 0 to 1
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    seen_islands = set()
                    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] > 1:
                            seen_islands.add(grid[nr][nc])
                    
                    combined = 1 + sum(area[i_id] for i_id in seen_islands)
                    max_area = max(max_area, combined)
                    
        return max_area
```

## Why This Works
By utilizing **Hash Map**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Using the same element twice.
2. Checking the map before inserting elements in the correct order.
3. Inefficient hash functions or unnecessary duplicate key updates.

## Interview Notes
- **Tests:** Hash map usage, complement/frequency lookup, and $O(n)$ time optimization.
- **Follow-up:** Can you solve the problem in $O(1)$ extra space if the input array is sorted?

## Related Problems
- [830. Positions of Large Groups](../../0501-1000/0830-positions-of-large-groups/)
- [1036. Escape a Large Maze](../../1001-1500/1036-escape-a-large-maze/)
- [1093. Statistics from a Large Sample](../../1001-1500/1093-statistics-from-a-large-sample/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/making-a-large-island/)
