# Maximum Number Of Jumps To Reach The Last Index

## Problem Explanation
Find the maximum number of jumps to reach the last index, where you can jump from `i` to `j > i` if `|nums[j] - nums[i]| <= target`.

## How the Code Works
Uses **DP** where `dp[i]` = max jumps to reach index `i`. For each `i`, check all `j < i` where the jump is valid and update `dp[i] = max(dp[i], dp[j] + 1)`. Return `dp[n-1]` or -1 if unreachable.
