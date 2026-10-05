# LeetCode 1240: Tiling a Rectangle with the Fewest Squares

**LeetCode Problem #1240 — Tiling a Rectangle with the Fewest Squares**
Solve LeetCode Tiling a Rectangle with the Fewest Squares using C++ and Database / SQL. This solution finds the optimal result using SQL Query / Relational Join & Grouping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Tiling a Rectangle with the Fewest Squares |
| LeetCode | #1240 |
| Difficulty | Hard |
| Language | C++ |
| Algorithm | SQL Query / Relational Join & Grouping |
| Data Structure | Relational Table |
| Pattern | Database / SQL |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Alice and Bob continue their games with piles of stones. There are a number of piles  arranged in a row , and each pile has a positive integer number of stones  piles[i] . The objective of the game is to end with the most stones.

## Key Insight
Leverage **Database / SQL** with **Relational Table** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code uses **Bottom-Up DP** with a suffix sum optimization.

1. **Suffix Sum:** `suffix[i]` is the total stones from pile `i` to the end.
2. **DP Definition:** `dp[i][M]` = maximum stones the current player can take from pile `i` onward with the given `M`.
3. **Base Case:** If `i + 2*M >= n`, the player takes all remaining piles: `dp[i][M] = suffix[i]`.
4. **Transition:** Try each valid `X` from `1` to `2*M`:
   - The current player gets `suffix[i] - dp[i+X][max(M,X)]`. This works because `suffix[i]` is the total remaining and `dp[i+X][...]` is what the *opponent* will optimally take.
   - Maximize over all choices of `X`.
5. **Answer:** `dp[0][1]` — Alice starts at pile 0 with M = 1.

Time complexity is $O(N^3)$ and space complexity is $O(N^2)$.

## Algorithm
1. Initialize state variables / data structure (**Relational Table**).
2. Process elements sequentially using **SQL Query / Relational Join & Grouping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Tiling a Rectangle with the Fewest Squares**. Applying **SQL Query / Relational Join & Grouping** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

## Pattern
**Database / SQL**

## Topics
- Database
- SQL
- Data Aggregation

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)

## Why This Works
By utilizing **Database / SQL**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [909. Snakes and Ladders](../0909-stone-game/)
- [1522. Diameter of N-Ary Tree](../1522-stone-game-iii/)
- [1617. Count Subtrees With Max Distance Between Cities](../1617-stone-game-iv/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/stone-game-ii/)
