# LeetCode 1872: Stone Game VIII

**LeetCode Problem #1872 — Stone Game VIII**
Solve LeetCode Stone Game VIII using Java and Prefix Sum. This solution finds the optimal result using Prefix Sum Precomputation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Stone Game VIII |
| LeetCode | #1872 |
| Difficulty | Hard |
| Language | Java |
| Algorithm | Prefix Sum Precomputation |
| Data Structure | Prefix Array |
| Pattern | Prefix Sum |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Alice and Bob take turns playing a game, with  Alice starting first .

## Key Insight
Leverage **Prefix Sum** with **Prefix Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code uses **DP with prefix sums**. After computing prefix sums, the problem reduces to choosing optimal split points. Working backwards, `dp[i]` = max difference the current player can achieve starting from index `i`. The recurrence is `dp[i] = max(dp[i+1], prefix[i] - dp[i+1])`.

Time complexity is $O(N)$ and space complexity is $O(1)$.

## Algorithm
1. Initialize state variables / data structure (**Prefix Array**).
2. Process elements sequentially using **Prefix Sum Precomputation**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Stone Game VIII**. Applying **Prefix Sum Precomputation** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

## Pattern
**Prefix Sum**

## Topics
- Prefix Sum
- Array

## Language
Java

## Source Code
- [solution.java](./solution.java)

## Why This Works
By utilizing **Prefix Sum**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [877. Stone Game](../0909-stone-game/)
- [1140. Stone Game II](../1240-stone-game-ii/)
- [1406. Stone Game III](../1522-stone-game-iii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/stone-game-viii/)
