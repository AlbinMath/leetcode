# LeetCode 2001: Number of Pairs of Interchangeable Rectangles

**LeetCode Problem #2001 — Number of Pairs of Interchangeable Rectangles**
Solve LeetCode Number of Pairs of Interchangeable Rectangles using C++ and Sliding Window. This solution finds the optimal result using Dynamic Sliding Window Traversal in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Pairs of Interchangeable Rectangles |
| LeetCode | #2001 |
| Difficulty | Medium |
| Language | C++ |
| Algorithm | Dynamic Sliding Window Traversal |
| Data Structure | Array / Hash Set |
| Pattern | Sliding Window |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given a  0-indexed  binary string  s  and two integers  minJump  and  maxJump . In the beginning, you are standing at index  0 , which is equal to  &#39;0&#39; . You can move from index  i  to index  j  if the following conditions are fulfilled:

## Key Insight
Maintain a dynamic contiguous window with two pointers (`left` and `right`), expanding to include new elements and shrinking when window invariants are violated.

## Approach
The code uses **BFS/DP with a sliding window** to avoid redundant checks. It maintains a window of reachable positions and uses a prefix sum or queue to efficiently determine which new positions can be reached within the `[minJump, maxJump]` range.

Time complexity is $O(N)$ and space complexity is $O(N)$.

## Algorithm
1. Initialize state variables / data structure (**Array / Hash Set**).
2. Process elements sequentially using **Dynamic Sliding Window Traversal**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Number of Pairs of Interchangeable Rectangles**. Applying **Dynamic Sliding Window Traversal** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Sliding Window**

## Topics
- Sliding Window
- Two Pointers
- Subarrays

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)

## Why This Works
By utilizing **Sliding Window**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Shrinking the window too late or missing invalid state checks.
2. Forgetting to update window metrics (e.g. char counts) during contraction.
3. Misinterpreting fixed vs variable window requirements.

## Interview Notes
- **Tests:** Two-pointer window management, state tracking, and contiguous subarray analysis.
- **Follow-up:** How do you handle non-positive integer values in subarray sum windows?

## Related Problems
- [1428. Leftmost Column with at Least a One](../1428-jump-game-iii/)
- [1447. Simplified Fractions](../1447-jump-game-iv/)
- [1466. Reorder Routes to Make All Paths Lead to the City Zero](../1466-jump-game-v/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/jump-game-vii/)
