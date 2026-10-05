# LeetCode 1644: Lowest Common Ancestor of a Binary Tree II

**LeetCode Problem #1644 — Lowest Common Ancestor of a Binary Tree II**
Solve LeetCode Lowest Common Ancestor of a Binary Tree II using JavaScript and Heap. This solution finds the optimal result using Priority Queue Selection in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Lowest Common Ancestor of a Binary Tree II |
| LeetCode | #1644 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Priority Queue Selection |
| Data Structure | Min/Max Heap |
| Pattern | Heap |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Given a string  s  of lowercase letters, you need to find the maximum number of  non-empty  substrings of  s  that meet the following conditions:

## Key Insight
Leverage **Heap** with **Min/Max Heap** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code uses a **Greedy** approach. It first finds the leftmost and rightmost occurrence of each character. Then for each potential starting character, it expands the substring to include all occurrences of all characters within it. Finally, it greedily selects non-overlapping substrings by preferring shorter ones that end earliest.

Time complexity is $O(N \times |\Sigma|)$ and space complexity is $O(|\Sigma|)$ where $|\Sigma|$ is the alphabet size.

## Algorithm
1. Initialize state variables / data structure (**Min/Max Heap**).
2. Process elements sequentially using **Priority Queue Selection**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Lowest Common Ancestor of a Binary Tree II**. Applying **Priority Queue Selection** yields the target result step by step.

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
- [2559. Count Vowel Strings in Ranges](../2559-maximum-number-of-non-overlapping-palindrome-substrings/)
- [1725. Number Of Rectangles That Can Form The Largest Square](../1725-number-of-sets-of-k-non-overlapping-line-segments/)
- [3562. Maximum Profit from Trading Stocks with Discounts](../3562-maximum-score-of-non-overlapping-intervals/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/)
