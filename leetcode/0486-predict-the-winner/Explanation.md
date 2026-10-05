# LeetCode 486: Predict the Winner

**LeetCode Problem #486 — Predict the Winner**
Solve LeetCode Predict the Winner using C++ and Database / SQL. This solution finds the optimal result using SQL Query / Relational Join & Grouping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Predict the Winner |
| LeetCode | #486 |
| Difficulty | Medium |
| Language | C++ |
| Algorithm | SQL Query / Relational Join & Grouping |
| Data Structure | Relational Table |
| Pattern | Database / SQL |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given an integer array  nums .

## Key Insight
Leverage **Database / SQL** with **Relational Table** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code uses **Interval DP** where `dp[i][j]` represents the maximum score advantage the current player can achieve from the subarray `nums[i..j]`.

1. **Base Case:** `dp[i][i] = nums[i]` — if only one number is left, the current player takes it.
2. **Transition:** For each subarray of length `len` from `2` to `n`:
   - `dp[i][j] = max(nums[i] - dp[i+1][j], nums[j] - dp[i][j-1])`
   - The current player picks either the left (`nums[i]`) or right (`nums[j]`) element. After picking, the opponent becomes the "current player" for the remaining subarray, so we subtract `dp` of the remaining range (since that represents the opponent's advantage).
3. **Result:** `dp[0][n-1] >= 0` means Player 1's advantage over the entire array is non-negative, so Player 1 wins or ties.

Time complexity is $O(N^2)$ and space complexity is $O(N^2)$.

## Algorithm
1. Initialize state variables / data structure (**Relational Table**).
2. Process elements sequentially using **SQL Query / Relational Join & Grouping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Predict the Winner**. Applying **SQL Query / Relational Join & Grouping** yields the target result step by step.

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
C++

## Source Code
- [solution.cpp](./solution.cpp)

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
- [10. Regular Expression Matching](../0010-regular-expression-matching/)
- [12. Integer to Roman](../0012-integer-to-roman/)
- [13. Roman to Integer](../0013-roman-to-integer/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/predict-the-winner/)
