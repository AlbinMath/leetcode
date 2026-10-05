# LeetCode 1563: Stone Game V

**LeetCode Problem #1563 — Stone Game V**
Solve LeetCode Stone Game V using Java and Prefix Sum. This solution finds the optimal result using Prefix Sum Precomputation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Stone Game V |
| LeetCode | #1563 |
| Difficulty | Hard |
| Language | Java |
| Algorithm | Prefix Sum Precomputation |
| Data Structure | Prefix Array |
| Pattern | Prefix Sum |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
There are several stones  arranged in a row , and each stone has an associated value which is an integer given in the array  stoneValue .

## Key Insight
Leverage **Prefix Sum** with **Prefix Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code uses **Interval DP** where `dp[left][right]` = maximum score from the subarray `[left, right]`.

1. **Prefix Sums:** Compute prefix sums for fast range sum queries.
2. **DP Transition:** For every split point `mid` in `[left, right-1]`:
   - Compute `leftSum` and `rightSum`.
   - If `leftSum < rightSum`: discard right, score `leftSum`, recurse on `[left, mid]`.
   - If `leftSum > rightSum`: discard left, score `rightSum`, recurse on `[mid+1, right]`.
   - If equal: try both options and take the maximum.
3. Return `dp[0][n-1]`.

Time complexity is $O(N^3)$ and space complexity is $O(N^2)$.

## Algorithm
1. Initialize state variables / data structure (**Prefix Array**).
2. Process elements sequentially using **Prefix Sum Precomputation**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Stone Game V**. Applying **Prefix Sum Precomputation** yields the target result step by step.

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
- [1340. Jump Game V](../1466-jump-game-v/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/stone-game-v/)
