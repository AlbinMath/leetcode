# LeetCode 1961: Check If String Is a Prefix of Array

**LeetCode Problem #1961 — Check If String Is a Prefix of Array**
Solve LeetCode Check If String Is a Prefix of Array using C++ and Prefix Sum. This solution finds the optimal result using Prefix Sum Precomputation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Check If String Is a Prefix of Array |
| LeetCode | #1961 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | Prefix Sum Precomputation |
| Data Structure | Prefix Array |
| Pattern | Prefix Sum |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Given a string  s  and an array of strings  words , determine whether  s  is a  prefix string  of  words .

## Key Insight
Leverage **Prefix Sum** with **Prefix Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Prefix Sum Precomputation**. By maintaining state efficiently in a **Prefix Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Prefix Array**).
2. Process elements sequentially using **Prefix Sum Precomputation**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Check If String Is a Prefix of Array**. Applying **Prefix Sum Precomputation** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

## Pattern
**Prefix Sum**

## Topics
- Prefix Sum
- Array

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)

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
- [1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence](../1566-check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/)
- [1662. Check If Two String Arrays are Equivalent](../1781-check-if-two-string-arrays-are-equivalent/)
- [1752. Check if Array Is Sorted and Rotated](../1878-check-if-array-is-sorted-and-rotated/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/check-if-string-is-a-prefix-of-array/)
