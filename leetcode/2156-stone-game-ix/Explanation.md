# LeetCode 2156: Find Substring With Given Hash Value

**LeetCode Problem #2156 — Find Substring With Given Hash Value**
Solve LeetCode Find Substring With Given Hash Value using C++ and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Substring With Given Hash Value |
| LeetCode | #2156 |
| Difficulty | Hard |
| Language | C++ |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Alice and Bob continue their games with stones. There is a row of n stones, and each stone has an associated value. You are given an integer array  stones , where  stones[i]  is the  value  of the  i th   stone.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code counts stones by their value mod 3 (groups 0, 1, 2). The key insights are:
- Mod-0 stones flip the game state (like a "pass" that changes who benefits).
- Alice needs to choose a starting stone (mod 1 or mod 2) that forces Bob into a losing position.
- The solution analyzes both possible starting moves and checks if either leads to a win for Alice based on the counts.

Time complexity is $O(N)$ and space complexity is $O(1)$.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Find Substring With Given Hash Value**. Applying **Depth-First Search (DFS) / Breadth-First Search (BFS)** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

## Pattern
**Tree & Graph**

## Topics
- Tree
- Graph
- DFS
- BFS

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)

## Why This Works
By utilizing **Tree & Graph**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

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
[View problem on LeetCode](https://leetcode.com/problems/stone-game-ix/)
