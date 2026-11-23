# LeetCode 1823: Find the Winner of the Circular Game

**LeetCode Problem #1823 — Find the Winner of the Circular Game**
Solve LeetCode Find the Winner of the Circular Game using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find the Winner of the Circular Game |
| LeetCode | #1823 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
There are  n  friends that are playing a game. The friends are sitting in a circle and are numbered from  1  to  n  in  clockwise order . More formally, moving clockwise from the  i th   friend brings you to the  (i+1) th   friend for  1 <= i < n , and moving clockwise from the  n th   friend brings you to the  1 st   friend.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Find the Winner of the Circular Game**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
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
- [2682. Find the Losers of the Circular Game](../../2501-3000/2791-find-the-losers-of-the-circular-game/)
- [1275. Find Winner on a Tic Tac Toe Game](../../1001-1500/1400-find-winner-on-a-tic-tac-toe-game/)
- [1535. Find the Winner of an Array Game](../../1501-2000/1657-find-the-winner-of-an-array-game/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-the-winner-of-the-circular-game/)
