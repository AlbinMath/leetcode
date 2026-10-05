# LeetCode 48: Rotate Image

**LeetCode Problem #48 — Rotate Image**
Solve LeetCode Rotate Image using C++ and Math & Logic. This solution finds the optimal result using Mathematical Simulation / Modular Arithmetic in O(n²) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Rotate Image |
| LeetCode | #48 |
| Difficulty | Medium |
| Language | C++ |
| Algorithm | Mathematical Simulation / Modular Arithmetic |
| Data Structure | Primitive Data Types |
| Pattern | Math & Logic |
| Time Complexity | O(n²) |
| Space Complexity | O(1) |

## Problem
You are given an  n x n  2D  matrix  representing an image, rotate the image by  90  degrees (clockwise).

## Key Insight
Leverage **Math & Logic** with **Primitive Data Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code performs the rotation in two elegant steps:

1. **Transpose the Matrix:** Swap `matrix[i][j]` with `matrix[j][i]` for all elements above the main diagonal (`j > i`). This converts rows into columns. After transposing, `[[1,2,3],[4,5,6],[7,8,9]]` becomes `[[1,4,7],[2,5,8],[3,6,9]]`.
2. **Reverse Each Row:** Reverse every row of the transposed matrix. After reversing, `[[1,4,7],[2,5,8],[3,6,9]]` becomes `[[7,4,1],[8,5,2],[9,6,3]]`, which is the 90-degree clockwise rotation.

This is mathematically equivalent to a 90° clockwise rotation because: Rotate90°(M) = Reverse(Transpose(M)). Time complexity is $O(N^2)$ and space complexity is $O(1)$ since everything is done in-place.

## Algorithm
1. Initialize state variables / data structure (**Primitive Data Types**).
2. Process elements sequentially using **Mathematical Simulation / Modular Arithmetic**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Rotate Image**. Applying **Mathematical Simulation / Modular Arithmetic** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n²)
- **Space Complexity:** O(1)

## Pattern
**Math & Logic**

## Topics
- Math
- Simulation

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)

## Why This Works
By utilizing **Math & Logic**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [61. Rotate List](../0061-rotate-list/)
- [396. Rotate Function](../0396-rotate-function/)
- [812. Largest Triangle Area](../0812-rotate-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/rotate-image/)
