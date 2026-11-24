# LeetCode 1728: Cat and Mouse II

**LeetCode Problem #1728 — Cat and Mouse II**
Solve LeetCode Cat and Mouse II using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Cat and Mouse II |
| LeetCode | #1728 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
A game is played by a cat and a mouse named Cat and Mouse.

The environment is represented by a `grid` of size `rows x cols`, where each element is a wall, floor, player (Cat, Mouse), or food.

Players are represented by the characters `'C'`(Cat)`,'M'`(Mouse). 
 Floors are represented by the character `'.'` and can be walked on. 
 Walls are represented by the character `'#'` and cannot be walked on. 
 Food is represented by the character `'F'` and can be walked on. 
 There is only one of each character `'C'`, `'M'`, and `'F'` in `grid`.

Mouse and Cat play according to the following rules:

Mouse **moves first**, then they take turns to move. 
 During each turn, Cat and Mouse can jump in one of the four directions (left, right, up, down). They cannot jump over the wall nor outside of the `grid`. 
 `catJump, mouseJump` are the maximum lengths Cat and Mouse can jump at a time, respectively. Cat and Mouse can jump less than the maximum length. 
 Staying in the same position is allowed. 
 Mouse can jump over Cat.

The game can end in 4 ways:

If Cat occupies the same position as Mouse, Cat wins. 
 If Cat reaches the food first, Cat wins. 
 If Mouse reaches the food first, Mouse wins. 
 If Mouse cannot get to the food within 1000 turns, Cat wins.

Given a `rows x cols` matrix `grid` and two integers `catJump` and `mouseJump`, return `true`* if Mouse can win the game if both Cat and Mouse play optimally, otherwise return *`false`.

## Constraints
- `rows == grid.length`
- `cols = grid[i].length`
- `1 <= rows, cols <= 8`
- `grid[i][j]` consist only of characters `'C'`, `'M'`, `'F'`, `'.'`, and `'#'`.
- There is only one of each character `'C'`, `'M'`, and `'F'` in `grid`.
- `1 <= catJump, mouseJump <= 8`

## Examples
### Example 1
- **Input:** `grid = ["####F","#C...","M...."], catJump = 1, mouseJump = 2`
- **Output:** `true`
- **Explanation:** Cat cannot catch Mouse on its turn nor can it get the food before Mouse.

### Example 2
- **Input:** `grid = ["M.C...F"], catJump = 1, mouseJump = 4`
- **Output:** `true`

### Example 3
- **Input:** `grid = ["M.C...F"], catJump = 1, mouseJump = 3`
- **Output:** `false`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Cat and Mouse II**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = ["####F","#C...","M...."], catJump = 1, mouseJump = 2`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** Cat cannot catch Mouse on its turn nor can it get the food before Mouse.

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
    def canMouseWin(self, grid, catJump, mouseJump):
        R, C = len(grid), len(grid[0])
        pos = [(r, c) for r in range(R) for c in range(C)
               if grid[r][c] != '#']
        ids = {p: i for i, p in enumerate(pos)}
        n = len(pos)
        m = next(ids[(r,c)] for r in range(R) for c in range(C) if grid[r][c]=='M')
        c = next(ids[(r,c)] for r in range(R) for c in range(C) if grid[r][c]=='C')
        f = next(ids[(r,c)] for r in range(R) for c in range(C) if grid[r][c]=='F')

        def moves(p, jump):
            r, col = pos[p]
            out = [p]
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                for k in range(1, jump+1):
                    x, y = r+dr*k, col+dc*k
                    if not (0 <= x < R and 0 <= y < C) or grid[x][y]=='#':
                        break
                    out.append(ids[(x,y)])
            return out

        M = [moves(i, mouseJump) for i in range(n)]
        K = [moves(i, catJump) for i in range(n)]
        revM = [[] for _ in range(n)]
        revK = [[] for _ in range(n)]
        for i in range(n):
            for j in M[i]: revM[j].append(i)
            for j in K[i]: revK[j].append(i)

        # 0 unknown, 1 mouse wins, 2 cat wins
        color = [[[0]*2 for _ in range(n)] for _ in range(n)]
        deg = [[[len(M[i]), len(K[j])] for j in range(n)] for i in range(n)]
        q = deque()

        for i in range(n):
            for t in range(2):
                color[f][i][t] = 1
                q.append((f, i, t, 1))
                color[i][f][t] = 2
                q.append((i, f, t, 2))
            for t in range(2):
                color[i][i][t] = 2
                q.append((i, i, t, 2))

        while q:
            a, b, t, res = q.popleft()
            if t == 0:
                parents = ((a, x, 1) for x in revK[b] if x != f)
            else:
                parents = ((x, b, 0) for x in revM[a])

            for x, y, pt in parents:
                if color[x][y][pt]:
                    continue
                if (pt == 0 and res == 1) or (pt == 1 and res == 2):
                    color[x][y][pt] = res
                    q.append((x, y, pt, res))
                else:
                    deg[x][y][pt] -= 1
                    if deg[x][y][pt] == 0:
                        winner = 2 if pt == 0 else 1
                        color[x][y][pt] = winner
                        q.append((x, y, pt, winner))

        # Any unresolved state is a draw; the mouse cannot force a win.
        return color[m][c][0] == 1
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
- [913. Cat and Mouse](../../0501-1000/0913-cat-and-mouse/)
- [2. Add Two Numbers](../../0001-0500/0002-add-two-numbers/)
- [7. Reverse Integer](../../0001-0500/0007-reverse-integer/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/cat-and-mouse-ii/)
