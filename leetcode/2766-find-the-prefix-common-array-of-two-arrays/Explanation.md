# LeetCode 2657: Find the Prefix Common Array of Two Arrays

**LeetCode Problem #2657 — Find the Prefix Common Array of Two Arrays**
Solve LeetCode Find the Prefix Common Array of Two Arrays using C++ and Prefix Sum. This solution finds the optimal result using Prefix Sum Precomputation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find the Prefix Common Array of Two Arrays |
| LeetCode | #2657 |
| Difficulty | Medium |
| Language | C++ |
| Algorithm | Prefix Sum Precomputation |
| Data Structure | Prefix Array |
| Pattern | Prefix Sum |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given two  0-indexed  integer   permutations  A  and  B  of length  n .

## Key Insight
Leverage **Prefix Sum** with **Prefix Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
Maintain a frequency counter. For each index i, increment counts for A[i] and B[i]. If a count reaches 2, that number has appeared in both arrays up to this point. Track the running count of such numbers.

## Algorithm
1. Initialize state variables / data structure (**Prefix Array**).
2. Process elements sequentially using **Prefix Sum Precomputation**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Find the Prefix Common Array of Two Arrays**. Applying **Prefix Sum Precomputation** yields the target result step by step.

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
- [1477. Find Two Non-overlapping Sub-arrays Each With Target Sum](../1573-find-two-non-overlapping-sub-arrays-each-with-target-sum/)
- [1979. Find Greatest Common Divisor of Array](../2106-find-greatest-common-divisor-of-array/)
- [3043. Find the Length of the Longest Common Prefix](../3329-find-the-length-of-the-longest-common-prefix/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/)
