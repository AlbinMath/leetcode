# LeetCode 3562: Maximum Profit from Trading Stocks with Discounts

**LeetCode Problem #3562 — Maximum Profit from Trading Stocks with Discounts**
Solve LeetCode Maximum Profit from Trading Stocks with Discounts using JavaScript and Greedy. This solution finds the optimal result using Greedy Choice Property in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Profit from Trading Stocks with Discounts |
| LeetCode | #3562 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Greedy Choice Property |
| Data Structure | Array / Priority Queue |
| Pattern | Greedy |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given a 2D integer array  intervals , where  intervals[i] = [l i , r i , weight i ] . Interval  i  starts at position  l i   and ends at  r i  , and has a weight of  weight i  . You can choose  up to  4  non-overlapping  intervals. The  score  of the chosen intervals is defined as the total sum of their weights.

## Key Insight
Leverage **Greedy** with **Array / Priority Queue** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **SQL Query / Relational Join & Grouping**. By maintaining state efficiently in a **Relational Table**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array / Priority Queue**).
2. Process elements sequentially using **Greedy Choice Property**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Maximum Profit from Trading Stocks with Discounts**. Applying **Greedy Choice Property** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Greedy**

## Topics
- Greedy
- Sorting

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)

## Why This Works
By utilizing **Greedy**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1644. Lowest Common Ancestor of a Binary Tree II](../1644-maximum-number-of-non-overlapping-substrings/)
- [2559. Count Vowel Strings in Ranges](../2559-maximum-number-of-non-overlapping-palindrome-substrings/)
- [1573. Number of Ways to Split a String](../1573-find-two-non-overlapping-sub-arrays-each-with-target-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-score-of-non-overlapping-intervals/)
