# LeetCode 2223: Sum of Scores of Built Strings

**LeetCode Problem #2223 — Sum of Scores of Built Strings**
Solve LeetCode Sum of Scores of Built Strings using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Sum of Scores of Built Strings |
| LeetCode | #2223 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are  building  a string  s  of length  n   one  character at a time,  prepending  each new character to the  front  of the string. The strings are labeled from  1  to  n , where the string with length  i  is labeled  s i  .

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Sum of Scores of Built Strings**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [2416. Sum of Prefix Scores of Strings](../2494-sum-of-prefix-scores-of-strings/)
- [1. Two Sum](../0001-two-sum/)
- [39. Combination Sum](../0039-combination-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/sum-of-scores-of-built-strings/)
