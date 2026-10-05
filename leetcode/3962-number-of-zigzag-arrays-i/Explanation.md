# LeetCode 3962: Maximum Subarray Sum After at Most K Swaps

**LeetCode Problem #3962 — Maximum Subarray Sum After at Most K Swaps**
Solve LeetCode Maximum Subarray Sum After at Most K Swaps using PHP and Array / General. This solution finds the optimal result using Iterative Traversal in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Subarray Sum After at Most K Swaps |
| LeetCode | #3962 |
| Difficulty | Hard |
| Language | PHP |
| Algorithm | Iterative Traversal |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given three integers  n ,  l , and  r .

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Iterative Traversal**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Iterative Traversal**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Maximum Subarray Sum After at Most K Swaps**. Applying **Iterative Traversal** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Array / General**

## Topics
- Array

## Language
PHP

## Source Code
- [solution.php](./solution.php)

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
- [3964. Minimum Lights to Illuminate a Road](../3964-number-of-zigzag-arrays-ii/)
- [3275. K-th Nearest Obstacle Queries](../3275-minimum-number-of-pushes-to-type-word-i/)
- [3347. Maximum Frequency of an Element After Performing Operations II](../3347-distribute-elements-into-two-arrays-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-zigzag-arrays-i/)
