# LeetCode 1446: Consecutive Characters

**LeetCode Problem #1446 — Consecutive Characters**
Solve LeetCode Consecutive Characters using Java and Math & Logic. This solution finds the optimal result using Mathematical Simulation / Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Consecutive Characters |
| LeetCode | #1446 |
| Difficulty | Easy |
| Language | Java |
| Algorithm | Mathematical Simulation / Modular Arithmetic |
| Data Structure | Primitive Data Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given two numbers,  hour  and  minutes , return  the smaller angle (in degrees) formed between the   hour   and the   minute   hand .

## Key Insight
Leverage **Math & Logic** with **Primitive Data Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
1. **Minute Hand Angle:** Each minute moves the minute hand by `6°` → `minuteAngle = minutes * 6.0`.
2. **Hour Hand Angle:** Each hour moves the hour hand by `30°`, and each minute moves it by `0.5°` → `hourAngle = (hour % 12) * 30.0 + minutes * 0.5`.
3. **Angle Between:** The absolute difference gives one angle. The other angle is `360 - difference`. Return the smaller of the two.

Time and space complexity are both $O(1)$.

## Algorithm
1. Initialize state variables / data structure (**Primitive Data Types**).
2. Process elements sequentially using **Mathematical Simulation / Modular Arithmetic**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Consecutive Characters**. Applying **Mathematical Simulation / Modular Arithmetic** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Math & Logic**

## Topics
- Math
- Simulation

## Language
Java

## Source Code
- [solution.java](./solution.java)

## Why This Works
By utilizing **Math & Logic**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1298. Maximum Candies You Can Get from Boxes](../1298-reverse-substrings-between-each-pair-of-parentheses/)
- [2182. Construct String With Repeat Limit](../2182-find-the-minimum-and-maximum-number-of-nodes-between-critical-points/)
- [2582. Pass the Pillow](../2582-minimum-score-of-a-path-between-two-cities/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/angle-between-hands-of-a-clock/)
