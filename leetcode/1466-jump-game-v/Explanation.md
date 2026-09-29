# Jump Game V

## Problem Explanation
Given an array `arr` and an integer `d`, you stand on index `i` and can jump to index `j` if: `j` is within `d` distance, `arr[i] > arr[j]`, and all indices between `i` and `j` also have values less than `arr[i]`. Return the maximum number of indices you can visit.

## How the Code Works
The code uses **DFS with Memoization**.

1. **DP Array:** `dp[i]` stores the maximum number of indices reachable from index `i`. Initialized to `1` (the index itself).
2. **DFS Function:** For each index `i`:
   - Try jumping right: iterate `j` from `i+1` up to `min(n-1, i+d)`. If `arr[j] >= arr[i]`, stop (blocked). Otherwise, `dp[i] = max(dp[i], 1 + dfs(j))`.
   - Try jumping left: iterate `j` from `i-1` down to `max(0, i-d)`. Same blocking rule.
3. **Answer:** The maximum of `dfs(i)` over all starting indices.

Time complexity is $O(N \times D)$ and space complexity is $O(N)$.
