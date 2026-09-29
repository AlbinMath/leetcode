# Image Overlap

## Problem Explanation
You are given two `n x n` binary matrices `img1` and `img2`. You can translate (shift) `img1` in any direction. Return the largest number of `1`s that overlap between `img1` and `img2` after any translation.

## How the Code Works
The code uses a **brute force** approach, trying every possible translation.

1. It iterates over all possible row shifts `dr` from `-(n-1)` to `(n-1)` and column shifts `dc` from `-(n-1)` to `(n-1)`.
2. For each translation `(dr, dc)`, it counts how many positions `(i, j)` in `img1` have `img1[i][j] == 1` and `img2[i+dr][j+dc] == 1` (only when the translated position is within bounds).
3. It tracks the maximum overlap across all translations.

Time complexity is $O(N^4)$ (trying $O(N^2)$ translations, each requiring an $O(N^2)$ comparison) and space complexity is $O(1)$.
