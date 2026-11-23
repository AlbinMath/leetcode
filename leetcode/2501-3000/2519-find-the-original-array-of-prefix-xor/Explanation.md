# LeetCode 2433: Find The Original Array of Prefix Xor

**LeetCode Problem #2433 — Find The Original Array of Prefix Xor**
Solve LeetCode Find The Original Array of Prefix Xor using Python and Prefix Sum. This solution finds the optimal result using Prefix Sum Precomputation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find The Original Array of Prefix Xor |
| LeetCode | #2433 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Prefix Sum Precomputation |
| Data Structure | Prefix Array |
| Pattern | Prefix Sum |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given an  integer  array  pref  of size  n . Find and return  the array   arr   of size   n   that satisfies :

## Key Insight
Leverage **Prefix Sum** with **Prefix Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Prefix Sum Precomputation**. By maintaining state efficiently in a **Prefix Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Prefix Array**).
2. Process elements sequentially using **Prefix Sum Precomputation**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Find The Original Array of Prefix Xor**. Applying **Prefix Sum Precomputation** yields the target result step by step.

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
- [2657. Find the Prefix Common Array of Two Arrays](../../2501-3000/2766-find-the-prefix-common-array-of-two-arrays/)
- [2527. Find Xor-Beauty of Array](../../2501-3000/2621-find-xor-beauty-of-array/)
- [1961. Check If String Is a Prefix of Array](../../2001-2500/2093-check-if-string-is-a-prefix-of-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-the-original-array-of-prefix-xor/)
