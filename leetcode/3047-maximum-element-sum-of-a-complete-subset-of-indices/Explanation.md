# LeetCode 2862: Maximum Element-Sum of a Complete Subset of Indices

**LeetCode Problem #2862 — Maximum Element-Sum of a Complete Subset of Indices**
Solve LeetCode Maximum Element-Sum of a Complete Subset of Indices using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Element-Sum of a Complete Subset of Indices |
| LeetCode | #2862 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given a  1  -indexed  array  nums . Your task is to select a  complete subset  from  nums  where every pair of selected indices multiplied is a  perfect square, . i. e. if you select  a i   and  a j  ,  i * j  must be a perfect square.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Maximum Element-Sum of a Complete Subset of Indices**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Array / General**

## Topics
- Array

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)

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
- [124. Binary Tree Maximum Path Sum](../0124-binary-tree-maximum-path-sum/)
- [689. Maximum Sum of 3 Non-Overlapping Subarrays](../0689-maximum-sum-of-3-non-overlapping-subarrays/)
- [918. Maximum Sum Circular Subarray](../0954-maximum-sum-circular-subarray/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-element-sum-of-a-complete-subset-of-indices/)
