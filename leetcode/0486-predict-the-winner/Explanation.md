# Predict The Winner

## Problem Explanation
Two players take turns picking numbers from either end of an integer array `nums`. Each player adds the picked number to their score. Player 1 goes first. Return `true` if Player 1 can win or tie, assuming both players play optimally.

## How the Code Works
The code uses **Interval DP** where `dp[i][j]` represents the maximum score advantage the current player can achieve from the subarray `nums[i..j]`.

1. **Base Case:** `dp[i][i] = nums[i]` — if only one number is left, the current player takes it.
2. **Transition:** For each subarray of length `len` from `2` to `n`:
   - `dp[i][j] = max(nums[i] - dp[i+1][j], nums[j] - dp[i][j-1])`
   - The current player picks either the left (`nums[i]`) or right (`nums[j]`) element. After picking, the opponent becomes the "current player" for the remaining subarray, so we subtract `dp` of the remaining range (since that represents the opponent's advantage).
3. **Result:** `dp[0][n-1] >= 0` means Player 1's advantage over the entire array is non-negative, so Player 1 wins or ties.

Time complexity is $O(N^2)$ and space complexity is $O(N^2)$.
