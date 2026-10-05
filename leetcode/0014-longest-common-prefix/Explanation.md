# LeetCode 14: Longest Common Prefix

**LeetCode Problem #14 — Longest Common Prefix**
Solve LeetCode Longest Common Prefix using Python and Prefix Sum. This solution finds the optimal result using Prefix Sum Precomputation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest Common Prefix |
| LeetCode | #14 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Prefix Sum Precomputation |
| Data Structure | Prefix Array |
| Pattern | Prefix Sum |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Write a function to find the longest common prefix string amongst an array of strings.

## Key Insight
Leverage **Prefix Sum** with **Prefix Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We assume the first string `strs[0]` is the longest common prefix.
Then, we iterate through the rest of the strings.
For each string, we check if it starts with the current `prefix`.
If it doesn't, we shorten the `prefix` by removing the last character (`prefix[:-1]`) until the string starts with the prefix.
If at any point the `prefix` becomes empty, it means there is no common prefix among the strings, and we can immediately return `""`.
If the loop finishes, we return the remaining `prefix`.

## Algorithm
1. Initialize state variables / data structure (**Prefix Array**).
2. Process elements sequentially using **Prefix Sum Precomputation**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Longest Common Prefix**. Applying **Prefix Sum Precomputation** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

## Pattern
**Prefix Sum**

## Topics
- Prefix Sum
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)

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
- [3043. Find the Length of the Longest Common Prefix](../3329-find-the-length-of-the-longest-common-prefix/)
- [2657. Find the Prefix Common Array of Two Arrays](../2766-find-the-prefix-common-array-of-two-arrays/)
- [3093. Longest Common Suffix Queries](../3376-longest-common-suffix-queries/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longest-common-prefix/)
