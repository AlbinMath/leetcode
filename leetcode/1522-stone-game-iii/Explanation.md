# LeetCode 1522: Diameter of N-Ary Tree

**LeetCode Problem #1522 — Diameter of N-Ary Tree**
Solve LeetCode Diameter of N-Ary Tree using PHP and Database / SQL. This solution finds the optimal result using SQL Query / Relational Join & Grouping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Diameter of N-Ary Tree |
| LeetCode | #1522 |
| Difficulty | Medium |
| Language | PHP |
| Algorithm | SQL Query / Relational Join & Grouping |
| Data Structure | Relational Table |
| Pattern | Database / SQL |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Alice and Bob continue their games with piles of stones. There are several stones  arranged in a row , and each stone has an associated value which is an integer given in the array  stoneValue .

## Key Insight
Leverage **Database / SQL** with **Relational Table** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code uses **Dynamic Programming** where `dp[i]` = max stones the current player can score from piles `i` onward.

1. Process from the last pile backwards.
2. For each position `i`, try taking 1, 2, or 3 piles. The current player gets `suffix[i] - dp[i + take]` (total remaining minus what the opponent gets).
3. Compare `dp[0]` (Alice's score) with `suffix[0] - dp[0]` (Bob's score).

Time complexity is $O(N)$ and space complexity is $O(N)$.

## Algorithm
1. Initialize state variables / data structure (**Relational Table**).
2. Process elements sequentially using **SQL Query / Relational Join & Grouping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Diameter of N-Ary Tree**. Applying **SQL Query / Relational Join & Grouping** yields the target result step by step.

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
PHP

## Source Code
- [solution.php](./solution.php)

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
- [1240. Tiling a Rectangle with the Fewest Squares](../1240-stone-game-ii/)
- [1428. Leftmost Column with at Least a One](../1428-jump-game-iii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/stone-game-iii/)
