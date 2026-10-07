# LeetCode 2267:  Check if There Is a Valid Parentheses String Path

**LeetCode Problem #2267 —  Check if There Is a Valid Parentheses String Path**
Solve LeetCode  Check if There Is a Valid Parentheses String Path using C++ and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem |  Check if There Is a Valid Parentheses String Path |
| LeetCode | #2267 |
| Difficulty | Hard |
| Language | C++ |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
A parentheses string is a  non-empty  string consisting only of  &#39;(&#39;  and  &#39;)&#39; . It is  valid  if  any  of the following conditions is  true :

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
Uses **DP with state tracking**. At each cell, track the set of possible open-parenthesis counts. Moving right or down, increment count for `(` and decrement for `)`. A path is valid if we reach the bottom-right with count exactly 0. Prune states where count goes negative.

## Algorithm
1. Initialize state variables / data structure (**Stack**).
2. Process elements sequentially using **Stack Push / Pop Parsing**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for ** Check if There Is a Valid Parentheses String Path**. Applying **Stack Push / Pop Parsing** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)

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
- [20. Valid Parentheses](../0020-valid-parentheses/)
- [32. Longest Valid Parentheses](../0032-longest-valid-parentheses/)
- [678. Valid Parenthesis String](../0678-valid-parenthesis-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/check-if-there-is-a-valid-parentheses-string-path/)
