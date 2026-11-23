# LeetCode 2063: Vowels of All Substrings

**LeetCode Problem #2063 — Vowels of All Substrings**
Solve LeetCode Vowels of All Substrings using JavaScript and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Vowels of All Substrings |
| LeetCode | #2063 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given a string  word , return  the  sum of the number of vowels  (  &#39;a&#39; ,  &#39;e&#39;  ,   &#39;i&#39;  ,   &#39;o&#39;  , and   &#39;u&#39;  )   in every substring of   word .

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Bitwise Masking & Bit Shift**. By maintaining state efficiently in a **Integer Bitmask**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Integer Bitmask**).
2. Process elements sequentially using **Bitwise Masking & Bit Shift**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Vowels of All Substrings**. Applying **Bitwise Masking & Bit Shift** yields the target result step by step.

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
- [1839. Longest Substring Of All Vowels in Order](../../1501-2000/1967-longest-substring-of-all-vowels-in-order/)
- [828. Count Unique Characters of All Substrings of a Given String](../../0501-1000/0855-count-unique-characters-of-all-substrings-of-a-given-string/)
- [1358. Number of Substrings Containing All Three Characters](../../1001-1500/1460-number-of-substrings-containing-all-three-characters/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/vowels-of-all-substrings/)
