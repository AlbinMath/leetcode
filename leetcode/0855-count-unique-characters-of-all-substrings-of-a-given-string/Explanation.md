# LeetCode 828: Count Unique Characters of All Substrings of a Given String

**LeetCode Problem #828 — Count Unique Characters of All Substrings of a Given String**
Solve LeetCode Count Unique Characters of All Substrings of a Given String using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Unique Characters of All Substrings of a Given String |
| LeetCode | #828 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Let&#39;s define a function  countUniqueChars(s)  that returns the number of unique characters in  s .

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Bitwise Masking & Bit Shift**. By maintaining state efficiently in a **Integer Bitmask**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Integer Bitmask**).
2. Process elements sequentially using **Bitwise Masking & Bit Shift**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Count Unique Characters of All Substrings of a Given String**. Applying **Bitwise Masking & Bit Shift** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Bit Manipulation**

## Topics
- Bit Manipulation
- Bitwise Math

## Language
Python

## Source Code
- [solution.py](./solution.py)

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
- [2062. Count Vowel Substrings of a String](../2186-count-vowel-substrings-of-a-string/)
- [3297. Count Substrings That Can Be Rearranged to Contain a String I](../3573-count-substrings-that-can-be-rearranged-to-contain-a-string-i/)
- [3298. Count Substrings That Can Be Rearranged to Contain a String II](../3572-count-substrings-that-can-be-rearranged-to-contain-a-string-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/)
