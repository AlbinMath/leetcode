# LeetCode 2056: Number of Valid Move Combinations On Chessboard

**LeetCode Problem #2056 — Number of Valid Move Combinations On Chessboard**
Solve LeetCode Number of Valid Move Combinations On Chessboard using Python and Backtracking. This solution finds the optimal result using Backtracking Recursive Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Valid Move Combinations On Chessboard |
| LeetCode | #2056 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Backtracking Recursive Search |
| Data Structure | Recursion Tree |
| Pattern | Backtracking |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
There is an  8 x 8  chessboard containing  n  pieces (rooks, queens, or bishops). You are given a string array  pieces  of length  n , where  pieces[i]  describes the type (rook, queen, or bishop) of the  i th   piece. In addition, you are given a 2D integer array  positions  also of length  n , where  positions[i] = [r i , c i ]  indicates that the  i th   piece is currently at the  1-based  coordinate  (r i , c i )  on the chessboard.

## Key Insight
Leverage **Backtracking** with **Recursion Tree** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Backtracking Recursive Search**. By maintaining state efficiently in a **Recursion Tree**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Recursion Tree**).
2. Process elements sequentially using **Backtracking Recursive Search**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Number of Valid Move Combinations On Chessboard**. Applying **Backtracking Recursive Search** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Backtracking**

## Topics
- Backtracking
- Recursion

## Language
Python

## Source Code
- [solution.py](./solution.py)

## Why This Works
By utilizing **Backtracking**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1769. Minimum Number of Operations to Move All Balls to Each Box](../../1501-2000/1895-minimum-number-of-operations-to-move-all-balls-to-each-box/)
- [17. Letter Combinations of a Phone Number](../../0001-0500/0017-letter-combinations-of-a-phone-number/)
- [65. Valid Number](../../0001-0500/0065-valid-number/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-valid-move-combinations-on-chessboard/)
