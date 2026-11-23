# LeetCode 424: Longest Repeating Character Replacement

**LeetCode Problem #424 — Longest Repeating Character Replacement**
Solve LeetCode Longest Repeating Character Replacement using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest Repeating Character Replacement |
| LeetCode | #424 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given a string  s  and an integer  k . You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most  k  times.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Longest Repeating Character Replacement**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [2213. Longest Substring of One Repeating Character](../2319-longest-substring-of-one-repeating-character/)
- [3. Longest Substring Without Repeating Characters](../0003-longest-substring-without-repeating-characters/)
- [395. Longest Substring with At Least K Repeating Characters](../0395-longest-substring-with-at-least-k-repeating-characters/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longest-repeating-character-replacement/)
