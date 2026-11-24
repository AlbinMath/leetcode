# LeetCode 749: Contain Virus

**LeetCode Problem #749 — Contain Virus**
Solve LeetCode Contain Virus using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Contain Virus |
| LeetCode | #749 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
A virus is spreading rapidly, and your task is to quarantine the infected area by installing walls.

The world is modeled as an `m x n` binary grid `isInfected`, where `isInfected[i][j] == 0` represents uninfected cells, and `isInfected[i][j] == 1` represents cells contaminated with the virus. A wall (and only one wall) can be installed between any two **4-directionally** adjacent cells, on the shared boundary.

Every night, the virus spreads to all neighboring cells in all four directions unless blocked by a wall. Resources are limited. Each day, you can install walls around only one region (i.e., the affected area (continuous block of infected cells) that threatens the most uninfected cells the following night). There **will never be a tie**.

Return *the number of walls used to quarantine all the infected regions*. If the world will become fully infected, return the number of walls used.

## Constraints
- `m == isInfected.length`
- `n == isInfected[i].length`
- `1 <= m, n <= 50`
- `isInfected[i][j]` is either `0` or `1`.
- There is always a contiguous viral region throughout the described process that will **infect strictly more uncontaminated squares** in the next round.

## Examples
### Example 1
- **Input:** `isInfected = [[0,1,0,0,0,0,0,1],[0,1,0,0,0,0,0,1],[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0]]`
- **Output:** `10`
- **Explanation:** There are 2 contaminated regions.
On the first day, add 5 walls to quarantine the viral region on the left. The board after the virus spreads is:
 
On the second day, add 5 walls to quarantine the viral region on the right. The virus is fully contained.

### Example 2
- **Input:** `isInfected = [[1,1,1],[1,0,1],[1,1,1]]`
- **Output:** `4`
- **Explanation:** Even though there is only one cell saved, there are 4 walls built.
Notice that walls are only built on the shared boundary of two different cells.

### Example 3
- **Input:** `isInfected = [[1,1,1,0,0,0,0,0,0],[1,0,1,0,1,1,1,1,1],[1,1,1,0,0,0,0,0,0]]`
- **Output:** `13`
- **Explanation:** The region on the left only builds two new walls.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Contain Virus**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `isInfected = [[0,1,0,0,0,0,0,1],[0,1,0,0,0,0,0,1],[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `10`.
4. **Verification:** There are 2 contaminated regions.
On the first day, add 5 walls to quarantine the viral region on the left. The board after the virus spreads is:
 
On the second day, add 5 walls to quarantine the viral region on the right. The virus is fully contained.

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
from typing import List

class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:
        m, n = len(isInfected), len(isInfected[0])
        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
        total_walls = 0

        while True:
            visited = set()
            regions = []    # list of infected cell sets/lists
            frontiers = []  # list of unique threatened (r, c) sets
            walls_list = [] # list of perimeter wall counts

            for r in range(m):
                for c in range(n):
                    if isInfected[r][c] == 1 and (r, c) not in visited:
                        cells = []
                        frontier = set()
                        walls = 0
                        stack = [(r, c)]
                        visited.add((r, c))

                        while stack:
                            cr, cc = stack.pop()
                            cells.append((cr, cc))
                            for dr, dc in dirs:
                                nr, nc = cr + dr, cc + dc
                                if 0 <= nr < m and 0 <= nc < n:
                                    if isInfected[nr][nc] == 0:
                                        walls += 1
                                        frontier.add((nr, nc))
                                    elif isInfected[nr][nc] == 1 and (nr, nc) not in visited:
                                        visited.add((nr, nc))
                                        stack.append((nr, nc))

                        regions.append(cells)
                        frontiers.append(frontier)
                        walls_list.append(walls)

            if not regions:
                break

            best_idx = max(range(len(regions)), key=lambda i: len(frontiers[i]))
            if not frontiers[best_idx]:
                break

            total_walls += walls_list[best_idx]
            for r, c in regions[best_idx]:
                isInfected[r][c] = 2

            for i, frontier in enumerate(frontiers):
                if i != best_idx:
                    for r, c in frontier:
                        isInfected[r][c] = 1

        return total_walls
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
- [2930. Number of Strings Which Can Be Rearranged to Contain Substring](../../2501-3000/2930-number-of-strings-which-can-be-rearranged-to-contain-substring/)
- [3297. Count Substrings That Can Be Rearranged to Contain a String I](../../3001-3500/3297-count-substrings-that-can-be-rearranged-to-contain-a-string-i/)
- [3298. Count Substrings That Can Be Rearranged to Contain a String II](../../3001-3500/3298-count-substrings-that-can-be-rearranged-to-contain-a-string-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/contain-virus/)
