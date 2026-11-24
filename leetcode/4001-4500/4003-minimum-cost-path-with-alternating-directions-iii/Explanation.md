# LeetCode 4003: Minimum Cost Path with Alternating Directions III

**LeetCode Problem #4003 — Minimum Cost Path with Alternating Directions III**
Solve LeetCode Minimum Cost Path with Alternating Directions III using Python and Heap. This solution finds the optimal result using Min/Max Heap Priority Selection in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Cost Path with Alternating Directions III |
| LeetCode | #4003 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Min/Max Heap Priority Selection |
| Data Structure | Heap / Priority Queue |
| Pattern | Heap |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given two integers `m` and `n` representing the number of rows and columns of a grid. Your goal is to reach cell `(m - 1, n - 1)`. You are also given a 2D integer array `penalty`.

The cost to enter cell `(i, j)` is `(i + 1) * (j + 1)`.

You begin at cell `(0, 0)` and initially pay its entrance cost. Actions performed after entering `(0, 0)` are numbered starting from 1.

On each action, you may move to an **adjacent** cell or wait in the current cell. A move follows the parity rule if:

On an **odd-numbered** action, you move **right** or **down**. 
 On an **even-numbered** action, you move **left** or **up**.

The cost of an action is determined as follows:

If you move according to the parity rule, pay only the entrance cost of the destination cell. 
 If you move in a direction that **violates** the parity rule, pay the entrance cost of the destination cell plus `penalty[i][j]`, where `(i, j)` is the cell you move from. 
 If you **wait** in cell `(i, j)`, pay `penalty[i][j]`.

After every move or wait, the action number increases by 1. Therefore, the required parity alternates after every action, regardless of whether a penalty was paid.

Return the **minimum** total cost required to reach `(m - 1, n - 1)`.

## Constraints
- `1 <= m, n <= 10^5`
- `2 <= m * n <= 10^5`
- `penalty.length == m`
- `penalty[i].length == n`
- `0 <= penalty[i][j] <= 10^5`

## Examples
### Example 1
- **Input:** `m = 2, n = 2, penalty = [[5,3],[1,4]]`
- **Output:** `8`
- **Explanation:** The optimal path is: 

 
 Start at cell `(0, 0)` with entry cost `(0 + 1) * (0 + 1) = 1`.

### Example 2
- **Input:** `m = 2, n = 2, penalty = [[0,7],[3,2]]`
- **Output:** `7`
- **Explanation:** The optimal path is: 

 
 Start at cell `(0, 0)` with entry cost `(0 + 1) * (0 + 1) = 1`.

### Example 3
- **Input:** `m = 2, n = 3, penalty = [[8,0,9],[7,4,1]]`
- **Output:** `12`
- **Explanation:** The optimal path is: 

 
 Start at cell `(0, 0)` with entry cost `(0 + 1) * (0 + 1) = 1`.

## Key Insight
Leverage **Heap** with **Heap / Priority Queue** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Cost Path with Alternating Directions III**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `m = 2, n = 2, penalty = [[5,3],[1,4]]`.
2. **Processing Steps:** We apply **Min/Max Heap Priority Selection** using our **Heap / Priority Queue**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `8`.
4. **Verification:** The optimal path is: 

 
 Start at cell `(0, 0)` with entry cost `(0 + 1) * (0 + 1) = 1`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Heap / Priority Queue.

## Pattern
**Heap**

## Topics
- Heap
- Priority Queue
- Sorting

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
import heapq

class Solution:
    def minCost(self, m: int, n: int, penalty: list[list[int]]) -> int:
        # Entrance cost function
        def enter_cost(r: int, c: int) -> int:
            return (r + 1) * (c + 1)

        # dist[r][c][p] stores the minimum cost to reach (r, c)
        # where the next action will have parity p (1 = odd, 0 = even).
        # We can flatten (r, c, p) to 2 * (r * n + c) + p
        num_cells = m * n
        INF = float('inf')
        dist = [INF] * (2 * num_cells)

        start_cost = enter_cost(0, 0)
        # Initially at (0, 0) before action 1 (odd parity -> p = 1)
        start_idx = 2 * 0 + 1
        dist[start_idx] = start_cost

        # Priority queue stores (cost, r, c, p)
        pq = [(start_cost, 0, 0, 1)]

        # Directions: (dr, dc, is_odd_friendly)
        # Right (0, 1) and Down (1, 0) are odd-friendly (p = 1)
        # Left (0, -1) and Up (-1, 0) are even-friendly (p = 0)
        moves = [
            (0, 1, 1),
            (1, 0, 1),
            (0, -1, 0),
            (-1, 0, 0)
        ]

        while pq:
            d, r, c, p = heapq.heappop(pq)

            idx = 2 * (r * n + c) + p
            if d > dist[idx]:
                continue

            # If we reached the target cell, this is the optimal cost
            if r == m - 1 and c == n - 1:
                return d

            next_p = 1 - p
            pen = penalty[r][c]

            # Option 1: Wait at current cell
            wait_cost = d + pen
            wait_idx = 2 * (r * n + c) + next_p
            if wait_cost < dist[wait_idx]:
                dist[wait_idx] = wait_cost
                heapq.heappush(pq, (wait_cost, r, c, next_p))

            # Option 2: Move to adjacent cells
            for dr, dc, move_parity in moves:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    extra = 0 if move_parity == p else pen
                    move_cost = d + enter_cost(nr, nc) + extra
                    next_idx = 2 * (nr * n + nc) + next_p

                    if move_cost < dist[next_idx]:
                        dist[next_idx] = move_cost
                        heapq.heappush(pq, (move_cost, nr, nc, next_p))

        return -1
```

## Why This Works
By utilizing **Heap**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1368. Minimum Cost to Make at Least One Valid Path in a Grid](../../1001-1500/1368-minimum-cost-to-make-at-least-one-valid-path-in-a-grid/)
- [2662. Minimum Cost of a Path With Special Roads](../../2501-3000/2662-minimum-cost-of-a-path-with-special-roads/)
- [3650. Minimum Cost Path with Edge Reversals](../../3501-4000/3650-minimum-cost-path-with-edge-reversals/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-cost-path-with-alternating-directions-iii/)
