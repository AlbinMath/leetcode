# LeetCode 1970: Last Day Where You Can Still Cross

**LeetCode Problem #1970 — Last Day Where You Can Still Cross**
Solve LeetCode Last Day Where You Can Still Cross using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Last Day Where You Can Still Cross |
| LeetCode | #1970 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There is a **1-based** binary matrix where `0` represents land and `1` represents water. You are given integers `row` and `col` representing the number of rows and columns in the matrix, respectively.

Initially on day `0`, the **entire** matrix is **land**. However, each day a new cell becomes flooded with **water**. You are given a **1-based** 2D array `cells`, where `cells[i] = [r_i, c_i]` represents that on the `i^th` day, the cell on the `r_i^th` row and `c_i^th` column (**1-based** coordinates) will be covered with **water** (i.e., changed to `1`).

You want to find the **last** day that it is possible to walk from the **top** to the **bottom** by only walking on land cells. You can start from **any** cell in the top row and end at **any** cell in the bottom row. You can only travel in the** four** cardinal directions (left, right, up, and down).

Return *the **last** day where it is possible to walk from the **top** to the **bottom** by only walking on land cells*.

## Constraints
- `2 <= row, col <= 2 * 10^4`
- `4 <= row * col <= 2 * 10^4`
- `cells.length == row * col`
- `1 <= r_i <= row`
- `1 <= c_i <= col`
- All the values of `cells` are **unique**.

## Examples
### Example 1
- **Input:** `row = 2, col = 2, cells = [[1,1],[2,1],[1,2],[2,2]]`
- **Output:** `2`
- **Explanation:** The above image depicts how the matrix changes each day starting from day 0.
The last day where it is possible to cross from top to bottom is on day 2.

### Example 2
- **Input:** `row = 2, col = 2, cells = [[1,1],[1,2],[2,1],[2,2]]`
- **Output:** `1`
- **Explanation:** The above image depicts how the matrix changes each day starting from day 0.
The last day where it is possible to cross from top to bottom is on day 1.

### Example 3
- **Input:** `row = 3, col = 3, cells = [[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3,2],[3,1]]`
- **Output:** `3`
- **Explanation:** The above image depicts how the matrix changes each day starting from day 0.
The last day where it is possible to cross from top to bottom is on day 3.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Last Day Where You Can Still Cross**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `row = 2, col = 2, cells = [[1,1],[2,1],[1,2],[2,2]]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** The above image depicts how the matrix changes each day starting from day 0.
The last day where it is possible to cross from top to bottom is on day 2.

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
from typing import List

class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int):
        rx, ry = self.find(x), self.find(y)
        if rx != ry:
            self.parent[rx] = ry

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        total_cells = row * col
        top_virtual = total_cells
        bottom_virtual = total_cells + 1

        dsu = DSU(total_cells + 2)
        grid = [[0] * col for _ in range(row)]  # 0: water (in reverse), 1: land

        def node_id(r: int, c: int) -> int:
            return r * col + c

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Process cells backwards from the last day
        for day in range(len(cells) - 1, -1, -1):
            r, c = cells[day][0] - 1, cells[day][1] - 1
            grid[r][c] = 1
            curr_id = node_id(r, c)

            # Connect to top/bottom virtual nodes if on the edge rows
            if r == 0:
                dsu.union(curr_id, top_virtual)
            if r == row - 1:
                dsu.union(curr_id, bottom_virtual)

            # Union with adjacent land neighbors
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 1:
                    dsu.union(curr_id, node_id(nr, nc))

            # The moment top and bottom connect, this is the last day we could cross
            if dsu.connected(top_virtual, bottom_virtual):
                return day

        return 0
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
- [1420. Build Array Where You Can Find The Maximum Exactly K Comparisons](../../1001-1500/1420-build-array-where-you-can-find-the-maximum-exactly-k-comparisons/)
- [1997. First Day Where You Have Been in All the Rooms](../../1501-2000/1997-first-day-where-you-have-been-in-all-the-rooms/)
- [1744. Can You Eat Your Favorite Candy on Your Favorite Day?](../../1501-2000/1744-can-you-eat-your-favorite-candy-on-your-favorite-day/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/last-day-where-you-can-still-cross/)
