# LeetCode 3831: Median of a Binary Search Tree Level

**LeetCode Problem #3831 — Median of a Binary Search Tree Level**
Solve LeetCode Median of a Binary Search Tree Level using JavaScript and Database / SQL. This solution finds the optimal result using SQL Query / Relational Join & Grouping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Median of a Binary Search Tree Level |
| LeetCode | #3831 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | SQL Query / Relational Join & Grouping |
| Data Structure | Relational Table |
| Pattern | Database / SQL |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given an array of  positive  integers  nums , and a  positive  integer  k .

## Key Insight
Leverage **Database / SQL** with **Relational Table** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code uses **Dynamic Programming** to count the products of all possible contiguous subarrays efficiently.
1. It initializes an array `result` of size `k` to store the final counts for each remainder.
2. It uses a `dp` array (size `k`), where `dp[r]` keeps track of how many subarrays ending at the *previous* element have a product whose remainder modulo `k` is `r`.
3. It iterates through each `num` in `nums`:
   - It calculates the remainder `x` of the current number itself (`num % k`).
   - It creates a `next` array to represent subarrays ending at the *current* position.
   - It counts the subarray that consists *only* of the current element: `next[x]++`.
   - It extends all previous subarrays: for every remainder `r` in `dp`, the new remainder if the current number is appended is `(r * x) % k`. It adds the count `dp[r]` to `next[newRemainder]`.
   - After computing all subarrays ending at the current position (`next`), it adds these counts to the overall `result` array.
   - Finally, it updates `dp = next` for the next iteration.
4. It returns the `result` array containing the aggregated counts.

## Algorithm
1. Initialize state variables / data structure (**Relational Table**).
2. Process elements sequentially using **SQL Query / Relational Join & Grouping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Median of a Binary Search Tree Level**. Applying **SQL Query / Relational Join & Grouping** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

## Pattern
**Database / SQL**

## Topics
- Database
- SQL
- Data Aggregation

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)

## Why This Works
By utilizing **Database / SQL**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [3840. House Robber V](../3840-find-x-value-of-array-ii/)
- [153. Find Minimum in Rotated Sorted Array](../0153-find-minimum-in-rotated-sorted-array/)
- [154. Find Minimum in Rotated Sorted Array II](../0154-find-minimum-in-rotated-sorted-array-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-x-value-of-array-i/)
