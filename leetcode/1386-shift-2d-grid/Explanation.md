# Shift 2D Grid

## Problem Explanation
Given a 2D grid, shift all elements `k` times. Each shift moves every element one position to the right; the last element of each row wraps to the first position of the next row, and the last element of the last row wraps to position `(0, 0)`.

## How the Code Works
The code (in Racket) uses a **flatten-shift-reshape** approach:
1. **Flatten:** Convert the 2D grid into a 1D list.
2. **Shift:** Compute `shift = k % total` to avoid redundant full rotations. Split the flat list at `total - shift` and swap the two halves (move the last `shift` elements to the front).
3. **Reshape:** Convert the shifted 1D list back into a 2D grid with `m` rows and `n` columns.

Time complexity is $O(M \times N)$ and space complexity is $O(M \times N)$.
