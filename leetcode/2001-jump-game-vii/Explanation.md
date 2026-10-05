# LeetCode 1871: Jump Game VII

**LeetCode Problem #1871 — Jump Game VII**
Solve LeetCode Jump Game VII using C++ and Prefix Sum. This solution finds the optimal result using Prefix Sum Precomputation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Jump Game VII |
| LeetCode | #1871 |
| Difficulty | Medium |
| Language | C++ |
| Algorithm | Prefix Sum Precomputation |
| Data Structure | Prefix Array |
| Pattern | Prefix Sum |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given a  0-indexed  binary string  s  and two integers  minJump  and  maxJump . In the beginning, you are standing at index  0 , which is equal to  &#39;0&#39; . You can move from index  i  to index  j  if the following conditions are fulfilled:

## Key Insight
Leverage **Prefix Sum** with **Prefix Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code uses **BFS/DP with a sliding window** to avoid redundant checks. It maintains a window of reachable positions and uses a prefix sum or queue to efficiently determine which new positions can be reached within the `[minJump, maxJump]` range.

Time complexity is $O(N)$ and space complexity is $O(N)$.

## Algorithm
1. Initialize state variables / data structure (**Prefix Array**).
2. Process elements sequentially using **Prefix Sum Precomputation**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Jump Game VII**. Applying **Prefix Sum Precomputation** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

## Pattern
**Prefix Sum**

## Topics
- Prefix Sum
- Array

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)

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
- [1306. Jump Game III](../1428-jump-game-iii/)
- [1340. Jump Game V](../1466-jump-game-v/)
- [1345. Jump Game IV](../1447-jump-game-iv/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/jump-game-vii/)
