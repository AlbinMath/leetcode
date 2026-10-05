# LeetCode 3562: Maximum Profit from Trading Stocks with Discounts

**LeetCode Problem #3562 — Maximum Profit from Trading Stocks with Discounts**
Solve LeetCode Maximum Profit from Trading Stocks with Discounts using JavaScript and Heap. This solution finds the optimal result using Priority Queue Selection in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Profit from Trading Stocks with Discounts |
| LeetCode | #3562 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Priority Queue Selection |
| Data Structure | Min/Max Heap |
| Pattern | Heap |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given a 2D integer array  intervals , where  intervals[i] = [l i , r i , weight i ] . Interval  i  starts at position  l i   and ends at  r i  , and has a weight of  weight i  . You can choose  up to  4  non-overlapping  intervals. The  score  of the chosen intervals is defined as the total sum of their weights.

## Key Insight
Leverage **Heap** with **Min/Max Heap** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **SQL Query / Relational Join & Grouping**. By maintaining state efficiently in a **Relational Table**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Min/Max Heap**).
2. Process elements sequentially using **Priority Queue Selection**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Maximum Profit from Trading Stocks with Discounts**. Applying **Priority Queue Selection** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

## Pattern
**Heap**

## Topics
- Heap
- Priority Queue
- Sorting

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)

## Why This Works
By utilizing **Heap**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

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
