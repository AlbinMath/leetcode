# Number Of Paths With Max Score

## Problem Explanation
You have a square board with digits, obstacles (`X`), a start (`S`) at the bottom-right, and an end (`E`) at the top-left. You can move left, up, or diagonally (up-left). Find the maximum score and the number of paths that achieve it.

## How the Code Works
The code uses **2D Dynamic Programming** processing from `S` toward `E`.

1. **Two DP Tables:** `score[i][j]` stores the maximum score reachable from `(i,j)` to `S`. `ways[i][j]` stores the number of paths achieving that score. `-1` means unreachable.
2. **Base Case:** `score[n-1][n-1] = 0`, `ways[n-1][n-1] = 1` (at `S`).
3. **Transition:** For each cell `(i,j)` processed right-to-left, bottom-to-top:
   - Skip obstacles (`X`).
   - Check three neighbors: down `(i+1,j)`, right `(i,j+1)`, diagonal `(i+1,j+1)`.
   - Take the neighbor with the highest score. If multiple neighbors tie, sum their path counts.
   - Add the current cell's digit value to the best score.
4. **Result:** `[score[0][0], ways[0][0]]`, or `[0, 0]` if unreachable.

Time complexity is $O(N^2)$ and space complexity is $O(N^2)$.
