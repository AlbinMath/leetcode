# LeetCode 864: Shortest Path to Get All Keys

**LeetCode Problem #864 — Shortest Path to Get All Keys**
Solve LeetCode Shortest Path to Get All Keys using JavaScript and Array / General. This solution finds the optimal result using Iterative Traversal in O(n²) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Shortest Path to Get All Keys |
| LeetCode | #864 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Iterative Traversal |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n²) |
| Space Complexity | O(1) |

## Problem
You are given two images,  img1  and  img2 , represented as binary, square matrices of size  n x n . A binary matrix has only  0 s and  1 s as values.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code uses a **brute force** approach, trying every possible translation.

1. It iterates over all possible row shifts `dr` from `-(n-1)` to `(n-1)` and column shifts `dc` from `-(n-1)` to `(n-1)`.
2. For each translation `(dr, dc)`, it counts how many positions `(i, j)` in `img1` have `img1[i][j] == 1` and `img2[i+dr][j+dc] == 1` (only when the translated position is within bounds).
3. It tracks the maximum overlap across all translations.

Time complexity is $O(N^4)$ (trying $O(N^2)$ translations, each requiring an $O(N^2)$ comparison) and space complexity is $O(1)$.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Iterative Traversal**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Shortest Path to Get All Keys**. Applying **Iterative Traversal** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n²)
- **Space Complexity:** O(1)

## Pattern
**Array / General**

## Topics
- Array

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)

## Why This Works
By utilizing **Array / General**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [48. Rotate Image](../0048-rotate-image/)
- [866. Prime Palindrome](../0866-rectangle-overlap/)
- [5. Longest Palindromic Substring](../0005-longest-palindromic-substring/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/image-overlap/)
