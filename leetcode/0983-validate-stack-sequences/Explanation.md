# LeetCode 946: Validate Stack Sequences

**LeetCode Problem #946 — Validate Stack Sequences**
Solve LeetCode Validate Stack Sequences using JavaScript and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Validate Stack Sequences |
| LeetCode | #946 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Given two integer arrays  pushed  and  popped  each with distinct values, return  true   if this could have been the result of a sequence of push and pop operations on an initially empty stack, or   false   otherwise.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Stack Push / Pop Parsing**. By maintaining state efficiently in a **Stack**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Stack**).
2. Process elements sequentially using **Stack Push / Pop Parsing**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Validate Stack Sequences**. Applying **Stack Push / Pop Parsing** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)

## Why This Works
By utilizing **Stack & Queue**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [187. Repeated DNA Sequences](../0187-repeated-dna-sequences/)
- [2318. Number of Distinct Roll Sequences](../2404-number-of-distinct-roll-sequences/)
- [2954. Count the Number of Infection Sequences](../3224-count-the-number-of-infection-sequences/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/validate-stack-sequences/)
