# Stone Game

## Problem Explanation
Alice and Bob play a game with piles of stones. There is an even number of piles, and each pile has a positive number of stones. Players take turns picking from either the first or last pile. The player with the most stones wins. Both play optimally. Return `true` if Alice wins.

## How the Code Works
The code simply returns `true`.

This is a **mathematical insight**: With an even number of piles, Alice can always win. She can always choose to take either all even-indexed piles or all odd-indexed piles (by choosing left or right strategically). Since the total number of stones is odd (all piles are positive), one group must have more stones than the other. Alice, going first, can always pick the more favorable group. Therefore, Alice always wins.
