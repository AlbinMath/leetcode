# LeetCode 1018: Binary Prefix Divisible By 5

**LeetCode Problem #1018 — Binary Prefix Divisible By 5**
Solve LeetCode Binary Prefix Divisible By 5 using Python and Trie. This solution finds the optimal result using Prefix Tree Lookup in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Binary Prefix Divisible By 5 |
| LeetCode | #1018 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Prefix Tree Lookup |
| Data Structure | Trie Node |
| Pattern | Trie |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given a binary array  nums  ( 0-indexed ).

## Key Insight
Leverage **Trie** with **Trie Node** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Prefix Sum Precomputation**. By maintaining state efficiently in a **Prefix Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Trie Node**).
2. Process elements sequentially using **Prefix Tree Lookup**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Binary Prefix Divisible By 5**. Applying **Prefix Tree Lookup** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

## Pattern
**Trie**

## Topics
- Trie
- String
- Prefix Search

## Language
Python

## Source Code
- [solution.py](./solution.py)

## Why This Works
By utilizing **Trie**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [570. Managers with at Least 5 Direct Reports](../../0501-1000/0570-managers-with-at-least-5-direct-reports/)
- [596. Classes With at Least 5 Students](../../0501-1000/0596-classes-with-at-least-5-students/)
- [14. Longest Common Prefix](../../0001-0500/0014-longest-common-prefix/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/binary-prefix-divisible-by-5/)
