# LeetCode 1455: Check If a Word Occurs As a Prefix of Any Word in a Sentence

**LeetCode Problem #1455 — Check If a Word Occurs As a Prefix of Any Word in a Sentence**
Solve LeetCode Check If a Word Occurs As a Prefix of Any Word in a Sentence using Python and Prefix Sum. This solution finds the optimal result using Prefix Sum Precomputation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Check If a Word Occurs As a Prefix of Any Word in a Sentence |
| LeetCode | #1455 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Prefix Sum Precomputation |
| Data Structure | Prefix Array |
| Pattern | Prefix Sum |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Given a  sentence  that consists of some words separated by a  single space , and a  searchWord , check if  searchWord  is a prefix of any word in  sentence .

## Key Insight
Leverage **Prefix Sum** with **Prefix Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Prefix Sum Precomputation**. By maintaining state efficiently in a **Prefix Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Prefix Array**).
2. Process elements sequentially using **Prefix Sum Precomputation**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Check If a Word Occurs As a Prefix of Any Word in a Sentence**. Applying **Prefix Sum Precomputation** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

## Pattern
**Prefix Sum**

## Topics
- Prefix Sum
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)

## Why This Works
By utilizing **Prefix Sum**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [2267.  Check if There Is a Valid Parentheses String Path](../../2001-2500/2349-check-if-there-is-a-valid-parentheses-string-path/)
- [1003. Check If Word Is Valid After Substitutions](../../1001-1500/1045-check-if-word-is-valid-after-substitutions/)
- [1832. Check if the Sentence Is Pangram](../../1501-2000/1960-check-if-the-sentence-is-pangram/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/)
