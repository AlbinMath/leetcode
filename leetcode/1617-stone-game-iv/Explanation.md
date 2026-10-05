# LeetCode 1617: Count Subtrees With Max Distance Between Cities

**LeetCode Problem #1617 — Count Subtrees With Max Distance Between Cities**
Solve LeetCode Count Subtrees With Max Distance Between Cities using TypeScript and Database / SQL. This solution finds the optimal result using SQL Query / Relational Join & Grouping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Subtrees With Max Distance Between Cities |
| LeetCode | #1617 |
| Difficulty | Hard |
| Language | TypeScript |
| Algorithm | SQL Query / Relational Join & Grouping |
| Data Structure | Relational Table |
| Pattern | Database / SQL |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Alice and Bob take turns playing a game, with Alice starting first.

## Key Insight
Leverage **Database / SQL** with **Relational Table** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code uses **Dynamic Programming** where `dp[i]` = whether the current player wins with `i` stones.

1. `dp[0] = false` (no stones = current player loses).
2. For each `i` from 1 to n: try removing every perfect square `k*k <= i`. If any `dp[i - k*k]` is `false` (meaning the opponent would lose), then `dp[i] = true`.
3. Return `dp[n]`.

Time complexity is $O(N\sqrt{N})$ and space complexity is $O(N)$.

## Algorithm
1. Initialize state variables / data structure (**Relational Table**).
2. Process elements sequentially using **SQL Query / Relational Join & Grouping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Count Subtrees With Max Distance Between Cities**. Applying **SQL Query / Relational Join & Grouping** yields the target result step by step.

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
TypeScript

## Source Code
- [solution.ts](./solution.ts)

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
- [1182. Shortest Distance to Target Color](../1182-game-play-analysis-iv/)
- [1240. Tiling a Rectangle with the Fewest Squares](../1240-stone-game-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/stone-game-iv/)
