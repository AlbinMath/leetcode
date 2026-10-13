# LeetCode 399: Evaluate Division

**LeetCode Problem #399 — Evaluate Division**
Solve LeetCode Evaluate Division using JavaScript and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Evaluate Division |
| LeetCode | #399 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given an array of variable pairs  equations  and an array of real numbers  values , where  equations[i] = [A i , B i ]  and  values[i]  represent the equation  A i  / B i  = values[i] . Each  A i   or  B i   is a string that represents a single variable.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Stack Push / Pop Parsing**. By maintaining state efficiently in a **Stack**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Stack**).
2. Process elements sequentially using **Stack Push / Pop Parsing**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Evaluate Division**. Applying **Stack Push / Pop Parsing** yields the target result step by step.

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
- [150. Evaluate Reverse Polish Notation](../0150-evaluate-reverse-polish-notation/)
- [1807. Evaluate the Bracket Pairs of a String](../1934-evaluate-the-bracket-pairs-of-a-string/)
- [20. Valid Parentheses](../0020-valid-parentheses/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/evaluate-division/)
