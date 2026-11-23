# LeetCode 966: Vowel Spellchecker

**LeetCode Problem #966 — Vowel Spellchecker**
Solve LeetCode Vowel Spellchecker using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Vowel Spellchecker |
| LeetCode | #966 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given a  wordlist , we want to implement a spellchecker that converts a query word into a correct word.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Vowel Spellchecker**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Array / General**

## Topics
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)

## Why This Works
By utilizing **Array / General**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1641. Count Sorted Vowel Strings](../../1501-2000/1761-count-sorted-vowel-strings/)
- [2062. Count Vowel Substrings of a String](../../2001-2500/2186-count-vowel-substrings-of-a-string/)
- [3305. Count of Substrings Containing Every Vowel and K Consonants I](../../3501-4000/3570-count-of-substrings-containing-every-vowel-and-k-consonants-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/vowel-spellchecker/)
