# LeetCode 14: Longest Common Prefix

**LeetCode Problem #14 — Longest Common Prefix**
Solve LeetCode Longest Common Prefix using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest Common Prefix |
| LeetCode | #14 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Write a function to find the longest common prefix string amongst an array of strings.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
We assume the first string `strs[0]` is the longest common prefix.
Then, we iterate through the rest of the strings.
For each string, we check if it starts with the current `prefix`.
If it doesn't, we shorten the `prefix` by removing the last character (`prefix[:-1]`) until the string starts with the prefix.
If at any point the `prefix` becomes empty, it means there is no common prefix among the strings, and we can immediately return `""`.
If the loop finishes, we return the remaining `prefix`.

## Algorithm
1. Initialize state variables / data structure (**Dictionary / Hash Map**).
2. Process elements sequentially using **Complement Lookup / Hash Table Frequency**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Longest Common Prefix**. Applying **Complement Lookup / Hash Table Frequency** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

## Pattern
**Hash Map**

## Topics
- Hash Table
- Array
- Complement Lookup

## Language
Python

## Source Code
- [solution.py](./solution.py)

## Why This Works
By utilizing **Hash Map**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Using the same element twice.
2. Checking the map before inserting elements in the correct order.
3. Inefficient hash functions or unnecessary duplicate key updates.

## Interview Notes
- **Tests:** Hash map usage, complement/frequency lookup, and $O(n)$ time optimization.
- **Follow-up:** Can you solve the problem in $O(1)$ extra space if the input array is sorted?

## Related Problems
- [3329. Count Substrings With K-Frequency Characters II](../3329-find-the-length-of-the-longest-common-prefix/)
- [2766. Relocate Marbles](../2766-find-the-prefix-common-array-of-two-arrays/)
- [3376. Minimum Time to Break Locks I](../3376-longest-common-suffix-queries/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longest-common-prefix/)
