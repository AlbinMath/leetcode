# LeetCode 668: Kth Smallest Number in Multiplication Table

**LeetCode Problem #668 — Kth Smallest Number in Multiplication Table**
Solve LeetCode Kth Smallest Number in Multiplication Table using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Kth Smallest Number in Multiplication Table |
| LeetCode | #668 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Nearly everyone has used the  Multiplication Table . The multiplication table of size  m x n  is an integer matrix  mat  where  mat[i][j] == i * j  ( 1-indexed ).

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Kth Smallest Number in Multiplication Table**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Array / General**

## Topics
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)

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
- [230. Kth Smallest Element in a BST](../0230-kth-smallest-element-in-a-bst/)
- [1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance](../1456-find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/)
- [1539. Kth Missing Positive Number](../1646-kth-missing-positive-number/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/)
