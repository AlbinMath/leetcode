# LeetCode 688: Knight Probability in Chessboard

**LeetCode Problem #688 — Knight Probability in Chessboard**
Solve LeetCode Knight Probability in Chessboard using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Knight Probability in Chessboard |
| LeetCode | #688 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
On an  n x n  chessboard, a knight starts at the cell  (row, column)  and attempts to make exactly  k  moves. The rows and columns are  0-indexed , so the top-left cell is  (0, 0) , and the bottom-right cell is  (n - 1, n - 1) .

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Knight Probability in Chessboard**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [1227. Airplane Seat Assignment Probability](../1362-airplane-seat-assignment-probability/)
- [1514. Path with Maximum Probability](../1325-path-with-maximum-probability/)
- [1812. Determine Color of a Chessboard Square](../1920-determine-color-of-a-chessboard-square/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/knight-probability-in-chessboard/)
