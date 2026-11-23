# LeetCode 2888: Reshape Data: Concatenate

**LeetCode Problem #2888 — Reshape Data: Concatenate**
Solve LeetCode Reshape Data: Concatenate using Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Reshape Data: Concatenate |
| LeetCode | #2888 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Write a solution to concatenate these two DataFrames  vertically  into one DataFrame.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Stack Push / Pop Parsing**. By maintaining state efficiently in a **Stack**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Stack**).
2. Process elements sequentially using **Stack Push / Pop Parsing**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Reshape Data: Concatenate**. Applying **Stack Push / Pop Parsing** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
Python

## Source Code
- [solution.py](./solution.py)

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
- [2889. Reshape Data: Pivot](../3072-reshape-data-pivot/)
- [2890. Reshape Data: Melt](../3073-reshape-data-melt/)
- [566. Reshape the Matrix](../0566-reshape-the-matrix/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/reshape-data-concatenate/)
