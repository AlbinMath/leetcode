# LeetCode 2245: Maximum Trailing Zeros in a Cornered Path

**LeetCode Problem #2245 — Maximum Trailing Zeros in a Cornered Path**
Solve LeetCode Maximum Trailing Zeros in a Cornered Path using Java and Array / General. This solution finds the optimal result using Iterative Traversal in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Trailing Zeros in a Cornered Path |
| LeetCode | #2245 |
| Difficulty | Medium |
| Language | Java |
| Algorithm | Iterative Traversal |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given an integer  mass , which represents the original mass of a planet. You are further given an integer array  asteroids , where  asteroids[i]  is the mass of the  i th   asteroid.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
Sort asteroids in ascending order. Greedily absorb from smallest to largest. If at any point the planet's mass is less than the current asteroid, return `false`.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Iterative Traversal**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Maximum Trailing Zeros in a Cornered Path**. Applying **Iterative Traversal** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Array / General**

## Topics
- Array

## Language
Java

## Source Code
- [solution.java](./solution.java)

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
- [5. Longest Palindromic Substring](../0005-longest-palindromic-substring/)
- [6. Zigzag Conversion](../0006-zigzag-conversion/)
- [193. Valid Phone Numbers](../0193-valid-phone-numbers/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/destroying-asteroids/)
