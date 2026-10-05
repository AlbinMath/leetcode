# LeetCode 2126: Destroying Asteroids

**LeetCode Problem #2126 — Destroying Asteroids**
Solve LeetCode Destroying Asteroids using Java and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Destroying Asteroids |
| LeetCode | #2126 |
| Difficulty | Medium |
| Language | Java |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given an integer  mass , which represents the original mass of a planet. You are further given an integer array  asteroids , where  asteroids[i]  is the mass of the  i th   asteroid.

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
Sort asteroids in ascending order. Greedily absorb from smallest to largest. If at any point the planet's mass is less than the current asteroid, return `false`.

## Algorithm
1. Initialize state variables / data structure (**Integer Bitmask**).
2. Process elements sequentially using **Bitwise Masking & Bit Shift**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Destroying Asteroids**. Applying **Bitwise Masking & Bit Shift** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Bit Manipulation**

## Topics
- Bit Manipulation
- Bitwise Math

## Language
Java

## Source Code
- [solution.java](./solution.java)

## Why This Works
By utilizing **Bit Manipulation**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [7. Reverse Integer](../0007-reverse-integer/)
- [396. Rotate Function](../0396-rotate-function/)
- [835. Image Overlap](../0864-image-overlap/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/destroying-asteroids/)
