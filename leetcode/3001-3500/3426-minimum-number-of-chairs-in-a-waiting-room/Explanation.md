# LeetCode 3168: Minimum Number of Chairs in a Waiting Room

**LeetCode Problem #3168 — Minimum Number of Chairs in a Waiting Room**
Solve LeetCode Minimum Number of Chairs in a Waiting Room using JavaScript and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Number of Chairs in a Waiting Room |
| LeetCode | #3168 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given a string  s . Simulate events at each second  i :

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Integer Bitmask**).
2. Process elements sequentially using **Bitwise Masking & Bit Shift**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Minimum Number of Chairs in a Waiting Room**. Applying **Bitwise Masking & Bit Shift** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Bit Manipulation**

## Topics
- Bit Manipulation
- Bitwise Math

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)

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
- [4009. Minimum Possible Maximum Waiting Time](../../4001-4500/4244-minimum-possible-maximum-waiting-time/)
- [452. Minimum Number of Arrows to Burst Balloons](../../0001-0500/0452-minimum-number-of-arrows-to-burst-balloons/)
- [995. Minimum Number of K Consecutive Bit Flips](../../1001-1500/1037-minimum-number-of-k-consecutive-bit-flips/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-number-of-chairs-in-a-waiting-room/)
