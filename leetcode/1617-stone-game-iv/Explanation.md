# Stone Game IV

## Problem Explanation
Alice and Bob take turns removing a perfect square number of stones. The player who cannot make a move loses. Alice goes first. Return `true` if Alice wins with optimal play.

## How the Code Works
The code uses **Dynamic Programming** where `dp[i]` = whether the current player wins with `i` stones.

1. `dp[0] = false` (no stones = current player loses).
2. For each `i` from 1 to n: try removing every perfect square `k*k <= i`. If any `dp[i - k*k]` is `false` (meaning the opponent would lose), then `dp[i] = true`.
3. Return `dp[n]`.

Time complexity is $O(N\sqrt{N})$ and space complexity is $O(N)$.
