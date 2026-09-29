# Stone Game III

## Problem Explanation
Alice and Bob play a game with piles of stones. On each turn, a player takes 1, 2, or 3 piles from the front. Both play optimally. Return "Alice", "Bob", or "Tie" based on who gets more stones.

## How the Code Works
The code uses **Dynamic Programming** where `dp[i]` = max stones the current player can score from piles `i` onward.

1. Process from the last pile backwards.
2. For each position `i`, try taking 1, 2, or 3 piles. The current player gets `suffix[i] - dp[i + take]` (total remaining minus what the opponent gets).
3. Compare `dp[0]` (Alice's score) with `suffix[0] - dp[0]` (Bob's score).

Time complexity is $O(N)$ and space complexity is $O(N)$.
