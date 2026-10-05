# LeetCode 1725: Number Of Rectangles That Can Form The Largest Square

**LeetCode Problem #1725 — Number Of Rectangles That Can Form The Largest Square**
Solve LeetCode Number Of Rectangles That Can Form The Largest Square using JavaScript and Prefix Sum. This solution finds the optimal result using Prefix Sum Precomputation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number Of Rectangles That Can Form The Largest Square |
| LeetCode | #1725 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | Prefix Sum Precomputation |
| Data Structure | Prefix Array |
| Pattern | Prefix Sum |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Given  n  points on a 1-D plane, where the  i th   point (from  0  to  n-1 ) is at  x = i , find the number of ways we can draw  exactly   k   non-overlapping  line segments such that each segment covers two or more points. The endpoints of each segment must have  integral coordinates . The  k  line segments  do not  have to cover all  n  points, and they are  allowed  to share endpoints.

## Key Insight
Leverage **Prefix Sum** with **Prefix Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code uses an optimized **DP with prefix sums**.

1. `dp[j]` = number of ways to choose `j` segments using points processed so far.
2. `prefix[j]` accumulates the sum of `dp[j-1]` values, enabling efficient transitions.
3. For each new point `i` (from 1 to n-1), update the prefix sums and then use them to update `dp[j]`.

Time complexity is $O(N \times K)$ and space complexity is $O(K)$.

## Algorithm
1. Initialize state variables / data structure (**Prefix Array**).
2. Process elements sequentially using **Prefix Sum Precomputation**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Number Of Rectangles That Can Form The Largest Square**. Applying **Prefix Sum Precomputation** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

## Pattern
**Prefix Sum**

## Topics
- Prefix Sum
- Array

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)

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
- [1644. Lowest Common Ancestor of a Binary Tree II](../1644-maximum-number-of-non-overlapping-substrings/)
- [2559. Count Vowel Strings in Ranges](../2559-maximum-number-of-non-overlapping-palindrome-substrings/)
- [1573. Number of Ways to Split a String](../1573-find-two-non-overlapping-sub-arrays-each-with-target-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-sets-of-k-non-overlapping-line-segments/)
