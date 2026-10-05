# LeetCode 2039: The Time When the Network Becomes Idle

**LeetCode Problem #2039 — The Time When the Network Becomes Idle**
Solve LeetCode The Time When the Network Becomes Idle using C++ and Array / General. This solution finds the optimal result using Iterative Traversal in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | The Time When the Network Becomes Idle |
| LeetCode | #2039 |
| Difficulty | Medium |
| Language | C++ |
| Algorithm | Iterative Traversal |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Alice and Bob take turns playing a game, with  Alice   starting first .

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code counts the number of `?` marks and digit sums in each half. If the total `?` count is odd, Alice always wins (she has the last move). If even, Bob wins only if he can balance the sums, which requires the sum difference to be exactly `9 * (question marks difference / 2)`.

Time complexity is $O(N)$ and space complexity is $O(1)$.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Iterative Traversal**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **The Time When the Network Becomes Idle**. Applying **Iterative Traversal** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Array / General**

## Topics
- Array

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)

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
- [1. Two Sum](../0001-two-sum/)
- [909. Snakes and Ladders](../0909-stone-game/)
- [1179. Reformat Department Table](../1179-game-play-analysis-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/sum-game/)
