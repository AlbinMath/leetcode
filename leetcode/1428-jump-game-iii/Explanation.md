# LeetCode 1306: Jump Game III

**LeetCode Problem #1306 — Jump Game III**
Solve LeetCode Jump Game III using C++ and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Jump Game III |
| LeetCode | #1306 |
| Difficulty | Medium |
| Language | C++ |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Given an array of non-negative integers  arr , you are initially positioned at  start  index of the array. When you are at index  i , you can jump to  i + arr[i]  or  i - arr[i] , check if you can reach  any  index with value 0.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code uses **BFS** (Breadth-First Search).

1. Start from the given index, mark it as visited, and add it to a queue.
2. For each index `i` dequeued: if `arr[i] == 0`, return `true`.
3. Otherwise, calculate the two possible jump destinations (`i + arr[i]` and `i - arr[i]`). If a destination is within bounds and unvisited, mark it visited and enqueue it.
4. If the queue empties without finding a `0`, return `false`.

Time complexity is $O(N)$ and space complexity is $O(N)$.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Jump Game III**. Applying **Depth-First Search (DFS) / Breadth-First Search (BFS)** yields the target result step by step.

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
- [45. Jump Game II](../0045-jump-game-ii/)
- [55. Jump Game](../0055-jump-game/)
- [1340. Jump Game V](../1466-jump-game-v/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/jump-game-iii/)
