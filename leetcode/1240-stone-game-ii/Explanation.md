# Stone Game II

## Problem Explanation
Alice and Bob play a game with piles of stones. On each turn, a player can take the first `X` piles where `1 <= X <= 2M`. After taking `X` piles, `M` becomes `max(M, X)`. Alice goes first with `M = 1`. Both play optimally. Return the maximum stones Alice can get.

## How the Code Works
The code uses **Bottom-Up DP** with a suffix sum optimization.

1. **Suffix Sum:** `suffix[i]` is the total stones from pile `i` to the end.
2. **DP Definition:** `dp[i][M]` = maximum stones the current player can take from pile `i` onward with the given `M`.
3. **Base Case:** If `i + 2*M >= n`, the player takes all remaining piles: `dp[i][M] = suffix[i]`.
4. **Transition:** Try each valid `X` from `1` to `2*M`:
   - The current player gets `suffix[i] - dp[i+X][max(M,X)]`. This works because `suffix[i]` is the total remaining and `dp[i+X][...]` is what the *opponent* will optimally take.
   - Maximize over all choices of `X`.
5. **Answer:** `dp[0][1]` — Alice starts at pile 0 with M = 1.

Time complexity is $O(N^3)$ and space complexity is $O(N^2)$.
