# Maximum Number Of Non Overlapping Palindrome Substrings

## Problem Explanation
Find the maximum number of non-overlapping palindromic substrings, each of length ≥ `k`.

## How the Code Works
Uses **DP** combined with palindrome detection (expand-around-center or Manacher's). For each position, compute `dp[i]` = max non-overlapping palindromes in `s[0..i-1]`. When a palindrome of length ≥ k ending at position i is found, update dp accordingly.
