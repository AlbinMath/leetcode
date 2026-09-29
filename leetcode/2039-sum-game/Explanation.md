# Sum Game

## Problem Explanation
A string of digits and `?` is split into two halves. Alice and Bob take turns replacing `?` with digits (0–9). Alice wins if the left and right halves have different sums; Bob wins if they're equal. Return whether Alice wins with optimal play.

## How the Code Works
The code counts the number of `?` marks and digit sums in each half. If the total `?` count is odd, Alice always wins (she has the last move). If even, Bob wins only if he can balance the sums, which requires the sum difference to be exactly `9 * (question marks difference / 2)`.

Time complexity is $O(N)$ and space complexity is $O(1)$.
