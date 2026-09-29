# Stone Game VIII

## Problem Explanation
Alice and Bob play with stones. On each turn, a player takes the first `x >= 2` stones, replaces them with their sum, and scores that sum. Both play optimally. Return the difference Alice - Bob.

## How the Code Works
The code uses **DP with prefix sums**. After computing prefix sums, the problem reduces to choosing optimal split points. Working backwards, `dp[i]` = max difference the current player can achieve starting from index `i`. The recurrence is `dp[i] = max(dp[i+1], prefix[i] - dp[i+1])`.

Time complexity is $O(N)$ and space complexity is $O(1)$.
