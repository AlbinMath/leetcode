# Stone Game V

## Problem Explanation
Alice has a row of stones. She splits the row into two non-empty parts, discards the part with the larger sum (or either if equal), and scores the smaller sum. She repeats until one stone remains. Return her maximum score.

## How the Code Works
The code uses **Interval DP** where `dp[left][right]` = maximum score from the subarray `[left, right]`.

1. **Prefix Sums:** Compute prefix sums for fast range sum queries.
2. **DP Transition:** For every split point `mid` in `[left, right-1]`:
   - Compute `leftSum` and `rightSum`.
   - If `leftSum < rightSum`: discard right, score `leftSum`, recurse on `[left, mid]`.
   - If `leftSum > rightSum`: discard left, score `rightSum`, recurse on `[mid+1, right]`.
   - If equal: try both options and take the maximum.
3. Return `dp[0][n-1]`.

Time complexity is $O(N^3)$ and space complexity is $O(N^2)$.
