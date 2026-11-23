# LeetCode 22: Generate Parentheses

**LeetCode Problem #22 — Generate Parentheses**
Solve LeetCode Generate Parentheses using C++, JavaScript, Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Generate Parentheses |
| LeetCode | #22 |
| Difficulty | Medium |
| Language | C++, JavaScript, Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Given  n  pairs of parentheses, write a function to  generate all combinations of well-formed parentheses .

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Stack Push / Pop Parsing**. By maintaining state efficiently in a **Stack**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Stack**).
2. Process elements sequentially using **Stack Push / Pop Parsing**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Generate Parentheses**. Applying **Stack Push / Pop Parsing** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
C++, JavaScript, Python

## Source Code
- [solution.cpp](./solution.cpp)
- [solution.js](./solution.js)
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
- [2267.  Check if There Is a Valid Parentheses String Path](../2349-check-if-there-is-a-valid-parentheses-string-path/)
- [478. Generate Random Point in a Circle](../0915-generate-random-point-in-a-circle/)
- [1374. Generate a String With Characters That Have Odd Counts](../1490-generate-a-string-with-characters-that-have-odd-counts/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/generate-parentheses/)
