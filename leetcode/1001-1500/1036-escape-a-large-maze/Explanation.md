# LeetCode 1036: Escape a Large Maze

**LeetCode Problem #1036 — Escape a Large Maze**
Solve LeetCode Escape a Large Maze using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Escape a Large Maze |
| LeetCode | #1036 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There is a 1 million by 1 million grid on an XY-plane, and the coordinates of each grid square are `(x, y)`.

We start at the `source = [s_x, s_y]` square and want to reach the `target = [t_x, t_y]` square. There is also an array of `blocked` squares, where each `blocked[i] = [x_i, y_i]` represents a blocked square with coordinates `(x_i, y_i)`.

Each move, we can walk one square north, east, south, or west if the square is **not** in the array of `blocked` squares. We are also not allowed to walk outside of the grid.

Return `true`* if and only if it is possible to reach the *`target`* square from the *`source`* square through a sequence of valid moves*.

## Constraints
- `0 <= blocked.length <= 200`
- `blocked[i].length == 2`
- `0 <= x_i, y_i < 10^6`
- `source.length == target.length == 2`
- `0 <= s_x, s_y, t_x, t_y < 10^6`
- `source != target`
- It is guaranteed that `source` and `target` are not blocked.

## Examples
### Example 1
- **Input:** `blocked = [[0,1],[1,0]], source = [0,0], target = [0,2]`
- **Output:** `false`
- **Explanation:** The target square is inaccessible starting from the source square because we cannot move.
We cannot move north or east because those squares are blocked.
We cannot move south or west because we cannot go outside of the grid.

### Example 2
- **Input:** `blocked = [], source = [0,0], target = [999999,999999]`
- **Output:** `true`
- **Explanation:** Because there are no blocked cells, it is possible to reach the target square.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Escape a Large Maze**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `blocked = [[0,1],[1,0]], source = [0,0], target = [0,2]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `false`.
4. **Verification:** The target square is inaccessible starting from the source square because we cannot move.
We cannot move north or east because those squares are blocked.
We cannot move south or west because we cannot go outside of the grid.

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
class Solution:
    def isEscapePossible(self, blocked: list[list[int]], source: list[int], target: list[int]) -> bool:
        blocked = set(map(tuple, blocked))
        limit = len(blocked) * (len(blocked) - 1) // 2

        def bfs(start, end):
            q, seen = [tuple(start)], {tuple(start)}
            while q and len(seen) <= limit:
                x, y = q.pop()
                if [x, y] == end:
                    return True
                for nx, ny in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
                    p = (nx, ny)
                    if 0 <= nx < 10**6 and 0 <= ny < 10**6 and p not in blocked and p not in seen:
                        seen.add(p)
                        q.append(p)
            return len(seen) > limit

        return bfs(source, target) and bfs(target, source)
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
- [1926. Nearest Exit from Entrance in Maze](../../1501-2000/1926-nearest-exit-from-entrance-in-maze/)
- [789. Escape The Ghosts](../../0501-1000/0789-escape-the-ghosts/)
- [2258. Escape the Spreading Fire](../../2001-2500/2258-escape-the-spreading-fire/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/escape-a-large-maze/)
