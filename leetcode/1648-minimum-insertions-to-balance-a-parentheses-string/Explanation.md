# LeetCode 1541: Minimum Insertions to Balance a Parentheses String

**LeetCode Problem #1541 — Minimum Insertions to Balance a Parentheses String**
Solve LeetCode Minimum Insertions to Balance a Parentheses String using Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Insertions to Balance a Parentheses String |
| LeetCode | #1541 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Given a parentheses string  s  containing only the characters  &#39;(&#39;  and  &#39;)&#39; . A parentheses string is  balanced  if:

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Stack Push / Pop Parsing**. By maintaining state efficiently in a **Stack**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Stack**).
2. Process elements sequentially using **Stack Push / Pop Parsing**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Minimum Insertions to Balance a Parentheses String**. Applying **Stack Push / Pop Parsing** yields the target result step by step.

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
- [921. Minimum Add to Make Parentheses Valid](../0957-minimum-add-to-make-parentheses-valid/)
- [1758. Minimum Changes To Make Alternating Binary String](../1884-minimum-changes-to-make-alternating-binary-string/)
- [2267.  Check if There Is a Valid Parentheses String Path](../2349--check-if-there-is-a-valid-parentheses-string-path/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/)
