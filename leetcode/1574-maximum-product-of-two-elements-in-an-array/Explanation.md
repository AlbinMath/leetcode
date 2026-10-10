# LeetCode 1464: Maximum Product of Two Elements in an Array

**LeetCode Problem #1464 — Maximum Product of Two Elements in an Array**
Solve LeetCode Maximum Product of Two Elements in an Array using Scala and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Product of Two Elements in an Array |
| LeetCode | #1464 |
| Difficulty | Easy |
| Language | Scala |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given an array of integers  nums .

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
The code finds the two largest elements in the array (either by sorting or a single-pass scan). The maximum product is `(largest - 1) * (secondLargest - 1)` since subtracting 1 from the two biggest numbers gives the best result.

Time complexity is $O(N)$ with a single pass (or $O(N \log N)$ with sorting) and space complexity is $O(1)$.

## Algorithm
1. Initialize state variables / data structure (**Sorted Array**).
2. Process elements sequentially using **Modified Binary Search**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Maximum Product of Two Elements in an Array**. Applying **Modified Binary Search** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Binary Search**

## Topics
- Binary Search
- Divide and Conquer
- Search Space

## Language
Scala

## Source Code
- [solution.scala](./solution.scala)

## Why This Works
By utilizing **Binary Search**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Applying standard binary search without accounting for array rotation or duplicates.
2. Off-by-one errors when updating boundary pointers (`left = mid + 1` vs `right = mid - 1`).
3. Integer overflow during midpoint calculation (use `mid = left + (right - left) // 2`).

## Interview Notes
- **Tests:** Logarithmic search space reduction, boundary handling, and invariant preservation.
- **Follow-up:** How does performance change if the array contains duplicate elements?

## Related Problems
- [1913. Maximum Product Difference Between Two Pairs](../2042-maximum-product-difference-between-two-pairs/)
- [3536. Maximum Product of Two Digits](../3859-maximum-product-of-two-digits/)
- [628. Maximum Product of Three Numbers](../0628-maximum-product-of-three-numbers/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/)
