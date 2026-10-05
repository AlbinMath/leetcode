# LeetCode 3116: Kth Smallest Amount With Single Denomination Combination

**LeetCode Problem #3116 — Kth Smallest Amount With Single Denomination Combination**
Solve LeetCode Kth Smallest Amount With Single Denomination Combination using Java and Backtracking. This solution finds the optimal result using Backtracking Recursive Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Kth Smallest Amount With Single Denomination Combination |
| LeetCode | #3116 |
| Difficulty | Hard |
| Language | Java |
| Algorithm | Backtracking Recursive Search |
| Data Structure | Recursion Tree |
| Pattern | Backtracking |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given an integer array  coins  representing coins of different denominations and an integer  k .

## Key Insight
Leverage **Backtracking** with **Recursion Tree** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Iterative Traversal**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Recursion Tree**).
2. Process elements sequentially using **Backtracking Recursive Search**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Kth Smallest Amount With Single Denomination Combination**. Applying **Backtracking Recursive Search** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Backtracking**

## Topics
- Backtracking
- Recursion

## Language
Java

## Source Code
- [solution.java](./solution.java)

## Why This Works
By utilizing **Backtracking**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [619. Biggest Single Number](../0619-biggest-single-number/)
- [1081. Smallest Subsequence of Distinct Characters](../1159-smallest-subsequence-of-distinct-characters/)
- [2904. Shortest and Lexicographically Smallest Beautiful String](../3150-shortest-and-lexicographically-smallest-beautiful-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/kth-smallest-amount-with-single-denomination-combination/)
