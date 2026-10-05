# LeetCode 1685: Sum of Absolute Differences in a Sorted Array

**LeetCode Problem #1685 — Sum of Absolute Differences in a Sorted Array**
Solve LeetCode Sum of Absolute Differences in a Sorted Array using Java and Database / SQL. This solution finds the optimal result using SQL Query / Relational Join & Grouping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Sum of Absolute Differences in a Sorted Array |
| LeetCode | #1685 |
| Difficulty | Medium |
| Language | Java |
| Algorithm | SQL Query / Relational Join & Grouping |
| Data Structure | Relational Table |
| Pattern | Database / SQL |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
There are several stones  arranged in a row , and each stone has an associated value which is an integer given in the array  stoneValue .

## Key Insight
Leverage **Database / SQL** with **Relational Table** to process inputs efficiently and achieve optimal time and space complexity.

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
1. Initialize state variables / data structure (**Relational Table**).
2. Process elements sequentially using **SQL Query / Relational Join & Grouping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Sum of Absolute Differences in a Sorted Array**. Applying **SQL Query / Relational Join & Grouping** yields the target result step by step.

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
Java

## Source Code
- [solution.java](./solution.java)

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
- [1466. Reorder Routes to Make All Paths Lead to the City Zero](../1466-jump-game-v/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/stone-game-v/)
