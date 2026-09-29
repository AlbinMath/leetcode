# Stone Game IX

## Problem Explanation
Alice and Bob play with stones labeled by values. On each turn, a player removes a stone. The game is lost if the sum of removed stones is divisible by 3 (except on the first move). Alice wants to win; Bob wants Alice to lose. Return whether Alice wins.

## How the Code Works
The code counts stones by their value mod 3 (groups 0, 1, 2). The key insights are:
- Mod-0 stones flip the game state (like a "pass" that changes who benefits).
- Alice needs to choose a starting stone (mod 1 or mod 2) that forces Bob into a losing position.
- The solution analyzes both possible starting moves and checks if either leads to a win for Alice based on the counts.

Time complexity is $O(N)$ and space complexity is $O(1)$.
