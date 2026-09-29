# Distinct Subsequences

## Problem Explanation
Given two strings `s` and `t`, return the number of distinct subsequences of `s` which equal `t`. A subsequence is a string formed by deleting some (or no) characters from `s` without changing the order of the remaining characters.

For example, if `s = "rabbbit"` and `t = "rabbit"`:
- There are 3 distinct subsequences (choosing different `b`s to delete).

## How the Code Works
The code uses **1D Dynamic Programming** with space optimization.

1. **DP Definition:** `dp[j]` represents the number of distinct subsequences of `s[0..i-1]` that equal `t[0..j-1]`.
2. **Base Case:** `dp[0] = 1` because the empty string `""` is always a subsequence of any string (by deleting all characters).
3. **Iteration:** For each character `s[i-1]` (outer loop over `s`):
   - It iterates **backwards** over `j` (from `n` down to `1`) to avoid overwriting values that are still needed.
   - If `s[i-1] === t[j-1]`, then `dp[j] += dp[j-1]`. This means: the number of ways to form `t[0..j-1]` includes both (a) the ways without using `s[i-1]` (existing `dp[j]`) and (b) the ways that use `s[i-1]` to match `t[j-1]` (which is `dp[j-1]`).
4. The answer is `dp[n]` — the number of ways to form the entire string `t`.

Time complexity is $O(M \times N)$ where $M$ and $N$ are the lengths of `s` and `t`. Space complexity is $O(N)$.
