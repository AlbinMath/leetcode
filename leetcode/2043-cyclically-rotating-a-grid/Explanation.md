# Cyclically Rotating A Grid

## Problem Explanation
Given an `m x n` grid, rotate each concentric layer of the grid counter-clockwise by `k` positions.

## How the Code Works
1. **Extract Layers:** For each concentric ring of the grid, extract the elements into a 1D array by traversing the ring clockwise.
2. **Rotate:** Rotate the 1D array by `k % length` positions.
3. **Place Back:** Write the rotated elements back into the corresponding positions in the grid.

Time complexity is $O(M \times N)$ and space complexity is $O(M \times N)$.
