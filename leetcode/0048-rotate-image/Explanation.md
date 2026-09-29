# Rotate Image

## Problem Explanation
You are given an `n x n` 2D `matrix` representing an image. Rotate the image by **90 degrees clockwise** in-place. You must modify the input matrix directly without allocating another 2D matrix.

For example, rotating `[[1,2,3],[4,5,6],[7,8,9]]` gives `[[7,4,1],[8,5,2],[9,6,3]]`.

## How the Code Works
The code performs the rotation in two elegant steps:

1. **Transpose the Matrix:** Swap `matrix[i][j]` with `matrix[j][i]` for all elements above the main diagonal (`j > i`). This converts rows into columns. After transposing, `[[1,2,3],[4,5,6],[7,8,9]]` becomes `[[1,4,7],[2,5,8],[3,6,9]]`.
2. **Reverse Each Row:** Reverse every row of the transposed matrix. After reversing, `[[1,4,7],[2,5,8],[3,6,9]]` becomes `[[7,4,1],[8,5,2],[9,6,3]]`, which is the 90-degree clockwise rotation.

This is mathematically equivalent to a 90° clockwise rotation because: Rotate90°(M) = Reverse(Transpose(M)). Time complexity is $O(N^2)$ and space complexity is $O(1)$ since everything is done in-place.
