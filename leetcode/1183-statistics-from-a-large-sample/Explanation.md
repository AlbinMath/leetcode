# LeetCode 1093: Statistics from a Large Sample

**LeetCode Problem #1093 — Statistics from a Large Sample**
Solve LeetCode Statistics from a Large Sample using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Statistics from a Large Sample |
| LeetCode | #1093 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given a large sample of integers in the range  [0, 255] . Since the sample is so large, it is represented by an array  count  where  count[k]  is the  number of times  that  k  appears in the sample.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Statistics from a Large Sample**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [19. Remove Nth Node From End of List](../0019-remove-nth-node-from-end-of-list/)
- [26. Remove Duplicates from Sorted Array](../0026-remove-duplicates-from-sorted-array/)
- [80. Remove Duplicates from Sorted Array II](../0080-remove-duplicates-from-sorted-array-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/statistics-from-a-large-sample/)
