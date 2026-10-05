# LeetCode 2714: Find Shortest Path with K Hops

**LeetCode Problem #2714 — Find Shortest Path with K Hops**
Solve LeetCode Find Shortest Path with K Hops using Kotlin and Prefix Sum. This solution finds the optimal result using Prefix Sum Precomputation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Shortest Path with K Hops |
| LeetCode | #2714 |
| Difficulty | Hard |
| Language | Kotlin |
| Algorithm | Prefix Sum Precomputation |
| Data Structure | Prefix Array |
| Pattern | Prefix Sum |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given a  0-indexed  integer array  nums  of size  n .

## Key Insight
Leverage **Prefix Sum** with **Prefix Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
Compute prefix sums for left sums and suffix sums for right sums, then calculate the absolute difference at each index.

## Algorithm
1. Initialize state variables / data structure (**Prefix Array**).
2. Process elements sequentially using **Prefix Sum Precomputation**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Find Shortest Path with K Hops**. Applying **Prefix Sum Precomputation** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

## Pattern
**Prefix Sum**

## Topics
- Prefix Sum
- Array

## Language
Kotlin

## Source Code
- [solution.kt](./solution.kt)

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
- [1. Two Sum](../0001-two-sum/)
- [1573. Number of Ways to Split a String](../1573-find-two-non-overlapping-sub-arrays-each-with-target-sum/)
- [2039. The Time When the Network Becomes Idle](../2039-sum-game/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/left-and-right-sum-differences/)
