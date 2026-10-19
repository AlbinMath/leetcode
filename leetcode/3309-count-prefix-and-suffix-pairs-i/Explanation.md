# LeetCode 3042: Count Prefix and Suffix Pairs I

**LeetCode Problem #3042 — Count Prefix and Suffix Pairs I**
Solve LeetCode Count Prefix and Suffix Pairs I using Python and Prefix Sum. This solution finds the optimal result using Prefix Sum Precomputation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Prefix and Suffix Pairs I |
| LeetCode | #3042 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Prefix Sum Precomputation |
| Data Structure | Prefix Array |
| Pattern | Prefix Sum |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given a  0-indexed  string array  words .

## Key Insight
Leverage **Prefix Sum** with **Prefix Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Prefix Sum Precomputation**. By maintaining state efficiently in a **Prefix Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Prefix Array**).
2. Process elements sequentially using **Prefix Sum Precomputation**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Count Prefix and Suffix Pairs I**. Applying **Prefix Sum Precomputation** yields the target result step by step.

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
- [3045. Count Prefix and Suffix Pairs II](../3305-count-prefix-and-suffix-pairs-ii/)
- [2183. Count Array Pairs Divisible by K](../2301-count-array-pairs-divisible-by-k/)
- [3120. Count the Number of Special Characters I](../3408-count-the-number-of-special-characters-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-prefix-and-suffix-pairs-i/)
