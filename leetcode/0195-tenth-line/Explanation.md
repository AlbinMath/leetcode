# LeetCode 195: Tenth Line

**LeetCode Problem #195 — Tenth Line**
Solve LeetCode Tenth Line using Shell and Array / General. This solution finds the optimal result using Iterative Traversal in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Tenth Line |
| LeetCode | #195 |
| Difficulty | Easy |
| Language | Shell |
| Algorithm | Iterative Traversal |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given a text file  file.txt , print just the 10th line of the file.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The solution uses `sed -n '10p'`:
- `sed` is a stream editor that processes text line by line.
- `-n` suppresses the default output (which would print every line).
- `'10p'` tells `sed` to **p**rint only line number 10.

This is a concise and efficient one-liner.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Iterative Traversal**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Tenth Line**. Applying **Iterative Traversal** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Array / General**

## Topics
- Array

## Language
Shell

## Source Code
- [solution.sh](./solution.sh)

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
- [1725. Number Of Rectangles That Can Form The Largest Square](../1725-number-of-sets-of-k-non-overlapping-line-segments/)
- [5. Longest Palindromic Substring](../0005-longest-palindromic-substring/)
- [6. Zigzag Conversion](../0006-zigzag-conversion/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/tenth-line/)
