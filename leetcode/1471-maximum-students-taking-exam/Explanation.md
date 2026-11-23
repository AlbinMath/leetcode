# LeetCode 1349: Maximum Students Taking Exam

**LeetCode Problem #1349 — Maximum Students Taking Exam**
Solve LeetCode Maximum Students Taking Exam using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Students Taking Exam |
| LeetCode | #1349 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given a  m * n  matrix  seats   that represent seats distributions in a classroom. If a seat is broken, it is denoted by  &#39;#&#39;  character otherwise it is denoted by a  &#39;.&#39;  character.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Maximum Students Taking Exam**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [53. Maximum Subarray](../0053-maximum-subarray/)
- [104. Maximum Depth of Binary Tree](../0104-maximum-depth-of-binary-tree/)
- [124. Binary Tree Maximum Path Sum](../0124-binary-tree-maximum-path-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-students-taking-exam/)
