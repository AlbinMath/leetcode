# LeetCode 14: Longest Common Prefix

**LeetCode Problem #14 — Longest Common Prefix**
Solve LeetCode Longest Common Prefix using Python and Array / General. This solution finds the optimal result using Iterative Traversal in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest Common Prefix |
| LeetCode | #14 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Iterative Traversal |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Write a function to find the longest common prefix string amongst an array of strings.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We assume the first string `strs[0]` is the longest common prefix.
Then, we iterate through the rest of the strings.
For each string, we check if it starts with the current `prefix`.
If it doesn't, we shorten the `prefix` by removing the last character (`prefix[:-1]`) until the string starts with the prefix.
If at any point the `prefix` becomes empty, it means there is no common prefix among the strings, and we can immediately return `""`.
If the loop finishes, we return the remaining `prefix`.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Iterative Traversal**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Longest Common Prefix**. Applying **Iterative Traversal** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Array / General**

## Topics
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)

## Why This Works
By utilizing **Array / General**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [3329. Count Substrings With K-Frequency Characters II](../3329-find-the-length-of-the-longest-common-prefix/)
- [2766. Relocate Marbles](../2766-find-the-prefix-common-array-of-two-arrays/)
- [3376. Minimum Time to Break Locks I](../3376-longest-common-suffix-queries/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longest-common-prefix/)
