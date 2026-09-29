# Rotating The Box

## Problem Explanation
Given a 2D grid representing a box with stones (`#`), obstacles (`*`), and empty cells (`.`), rotate the box 90° clockwise. Gravity should cause stones to fall to the bottom after rotation.

## How the Code Works
1. **Apply Gravity (rightward):** Before rotating, simulate gravity in each row by moving stones as far right as possible, stopping at obstacles or the edge.
2. **Rotate 90° Clockwise:** Create a new matrix where `result[j][m-1-i] = box[i][j]`.

Time complexity is $O(M \times N)$ and space complexity is $O(M \times N)$.
