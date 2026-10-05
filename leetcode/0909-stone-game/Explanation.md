# LeetCode 909: Snakes and Ladders

**LeetCode Problem #909 — Snakes and Ladders**
Solve LeetCode Snakes and Ladders using C++ and Math & Logic. This solution finds the optimal result using Mathematical Simulation / Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Snakes and Ladders |
| LeetCode | #909 |
| Difficulty | Medium |
| Language | C++ |
| Algorithm | Mathematical Simulation / Modular Arithmetic |
| Data Structure | Primitive Data Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Alice and Bob play a game with piles of stones. There are an  even  number of piles arranged in a row, and each pile has a  positive  integer number of stones  piles[i] .

## Key Insight
Leverage **Math & Logic** with **Primitive Data Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code simply returns `true`.

This is a **mathematical insight**: With an even number of piles, Alice can always win. She can always choose to take either all even-indexed piles or all odd-indexed piles (by choosing left or right strategically). Since the total number of stones is odd (all piles are positive), one group must have more stones than the other. Alice, going first, can always pick the more favorable group. Therefore, Alice always wins.

## Algorithm
1. Initialize state variables / data structure (**Primitive Data Types**).
2. Process elements sequentially using **Mathematical Simulation / Modular Arithmetic**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Snakes and Ladders**. Applying **Mathematical Simulation / Modular Arithmetic** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
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
- [1240. Tiling a Rectangle with the Fewest Squares](../1240-stone-game-ii/)
- [1522. Diameter of N-Ary Tree](../1522-stone-game-iii/)
- [1617. Count Subtrees With Max Distance Between Cities](../1617-stone-game-iv/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/stone-game/)
