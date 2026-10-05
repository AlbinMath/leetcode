# LeetCode 1570: Dot Product of Two Sparse Vectors

**LeetCode Problem #1570 — Dot Product of Two Sparse Vectors**
Solve LeetCode Dot Product of Two Sparse Vectors using TypeScript and Database / SQL. This solution finds the optimal result using SQL Query / Relational Join & Grouping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Dot Product of Two Sparse Vectors |
| LeetCode | #1570 |
| Difficulty | Medium |
| Language | TypeScript |
| Algorithm | SQL Query / Relational Join & Grouping |
| Data Structure | Relational Table |
| Pattern | Database / SQL |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given an integer array  prices  where  prices[i]  is the price of the  i th   item in a shop.

## Key Insight
Leverage **Database / SQL** with **Relational Table** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code uses a **Monotonic Stack** to efficiently find the next smaller or equal element for each index. It processes prices left to right, maintaining a stack of indices with unresolved discounts. When a price that qualifies as a discount is found, all applicable items on the stack get their discount applied.

Time complexity is $O(N)$ and space complexity is $O(N)$.

## Algorithm
1. Initialize state variables / data structure (**Relational Table**).
2. Process elements sequentially using **SQL Query / Relational Join & Grouping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Dot Product of Two Sparse Vectors**. Applying **SQL Query / Relational Join & Grouping** yields the target result step by step.

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
TypeScript

## Source Code
- [solution.ts](./solution.ts)

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
- [2248. Intersection of Multiple Arrays](../2248-minimum-cost-of-buying-candies-with-discount/)
- [3408. Design Task Manager](../3408-count-the-number-of-special-characters-i/)
- [3931. Check Adjacent Digit Differences](../3931-process-string-with-special-operations-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/)
