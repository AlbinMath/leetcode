# LeetCode 900: RLE Iterator

**LeetCode Problem #900 — RLE Iterator**
Solve LeetCode RLE Iterator using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | RLE Iterator |
| LeetCode | #900 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
We can use run-length encoding (i.e.,  RLE ) to encode a sequence of integers. In a run-length encoded array of even length  encoding  ( 0-indexed ), for all even  i ,  encoding[i]  tells us the number of times that the non-negative integer value  encoding[i + 1]  is repeated in the sequence.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **RLE Iterator**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [173. Binary Search Tree Iterator](../0173-binary-search-tree-iterator/)
- [284. Peeking Iterator](../0284-peeking-iterator/)
- [341. Flatten Nested List Iterator](../0341-flatten-nested-list-iterator/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/rle-iterator/)
