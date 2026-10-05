# LeetCode 628: Maximum Product of Three Numbers

**LeetCode Problem #628 — Maximum Product of Three Numbers**
Solve LeetCode Maximum Product of Three Numbers using Elixir and Database / SQL. This solution finds the optimal result using SQL Query / Relational Join & Grouping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Product of Three Numbers |
| LeetCode | #628 |
| Difficulty | Easy |
| Language | Elixir |
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
The code uses **sorting** and considers two possible candidates for the maximum product:

1. **Sort the Array:** Sort `nums` in ascending order.
2. **Two Candidates:**
   - `a * b * c` — the product of the three largest numbers (last three elements in the sorted array).
   - `a * x * y` — the product of the largest number and the two smallest numbers (first two elements). This handles the case where two large negative numbers multiply to give a large positive result.
3. Return the maximum of these two candidates.

Time complexity is $O(N \log N)$ for sorting and space complexity is $O(\log N)$.

## Algorithm
1. Initialize state variables / data structure (**Relational Table**).
2. Process elements sequentially using **SQL Query / Relational Join & Grouping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Maximum Product of Three Numbers**. Applying **SQL Query / Relational Join & Grouping** yields the target result step by step.

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
Elixir

## Source Code
- [solution.ex](./solution.ex)

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
- [1574. Shortest Subarray to be Removed to Make Array Sorted](../1574-maximum-product-of-two-elements-in-an-array/)
- [3859. Count Subarrays With K Distinct Integers](../3859-maximum-product-of-two-digits/)
- [2. Add Two Numbers](../0002-add-two-numbers/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-product-of-three-numbers/)
