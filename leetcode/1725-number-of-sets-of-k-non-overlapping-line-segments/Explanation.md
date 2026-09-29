# Number Of Sets Of K Non Overlapping Line Segments

## Problem Explanation
Given `n` points on a 1D line and integer `k`, count the number of ways to draw `k` non-overlapping line segments where each segment connects two of the `n` points, modulo `10^9+7`.

## How the Code Works
The code uses an optimized **DP with prefix sums**.

1. `dp[j]` = number of ways to choose `j` segments using points processed so far.
2. `prefix[j]` accumulates the sum of `dp[j-1]` values, enabling efficient transitions.
3. For each new point `i` (from 1 to n-1), update the prefix sums and then use them to update `dp[j]`.

Time complexity is $O(N \times K)$ and space complexity is $O(K)$.
