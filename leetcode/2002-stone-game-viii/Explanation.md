# LeetCode 2002: Maximum Product of the Length of Two Palindromic Subsequences

**LeetCode Problem #2002 — Maximum Product of the Length of Two Palindromic Subsequences**
Solve LeetCode Maximum Product of the Length of Two Palindromic Subsequences using Java and Prefix Sum. This solution finds the optimal result using Prefix Sum Precomputation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Product of the Length of Two Palindromic Subsequences |
| LeetCode | #2002 |
| Difficulty | Medium |
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
Consider the standard input for **Maximum Product of the Length of Two Palindromic Subsequences**. Applying **Prefix Sum Precomputation** yields the target result step by step.

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
- [909. Snakes and Ladders](../0909-stone-game/)
- [1240. Tiling a Rectangle with the Fewest Squares](../1240-stone-game-ii/)
- [1522. Diameter of N-Ary Tree](../1522-stone-game-iii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/stone-game-viii/)
