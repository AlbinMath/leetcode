# LeetCode 1140: Stone Game II

**LeetCode Problem #1140 — Stone Game II**
Solve LeetCode Stone Game II using C++ and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Stone Game II |
| LeetCode | #1140 |
| Difficulty | Medium |
| Language | C++ |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Alice and Bob continue their games with piles of stones. There are a number of piles  arranged in a row , and each pile has a positive integer number of stones  piles[i] . The objective of the game is to end with the most stones.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

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
1. Initialize state variables / data structure (**DP Table / Array**).
2. Process elements sequentially using **Memoization & State Transition**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Stone Game II**. Applying **Memoization & State Transition** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

## Pattern
**Dynamic Programming**

## Topics
- Dynamic Programming
- Memoization
- State Transition

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)

## Why This Works
By utilizing **Dynamic Programming**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Incorrect base case initialization.
2. Flawed state transition equation.
3. Storing unnecessary state leading to Memory Limit Exceeded (MLE).

## Interview Notes
- **Tests:** Subproblem decomposition, state transition logic, and space optimization.
- **Follow-up:** Can space complexity be reduced from $O(n^2)$ to $O(n)$ or $O(1)$?

## Related Problems
- [877. Stone Game](../0909-stone-game/)
- [1406. Stone Game III](../1522-stone-game-iii/)
- [1510. Stone Game IV](../1617-stone-game-iv/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/stone-game-ii/)
