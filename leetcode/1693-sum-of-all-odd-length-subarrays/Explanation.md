# LeetCode 1588: Sum of All Odd Length Subarrays

**LeetCode Problem #1588 — Sum of All Odd Length Subarrays**
Solve LeetCode Sum of All Odd Length Subarrays using C++ and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Sum of All Odd Length Subarrays |
| LeetCode | #1588 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given an array of positive integers  arr , return  the sum of all possible  odd-length subarrays  of   arr .

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Sum of All Odd Length Subarrays**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Array / General**

## Topics
- Array

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)

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
- [2461. Maximum Sum of Distinct Subarrays With Length K](../2552-maximum-sum-of-distinct-subarrays-with-length-k/)
- [2763. Sum of Imbalance Numbers of All Subarrays](../2849-sum-of-imbalance-numbers-of-all-subarrays/)
- [3318. Find X-Sum of All K-Long Subarrays I](../3610-find-x-sum-of-all-k-long-subarrays-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/sum-of-all-odd-length-subarrays/)
