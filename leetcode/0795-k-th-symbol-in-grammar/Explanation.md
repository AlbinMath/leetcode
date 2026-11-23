# LeetCode 779: K-th Symbol in Grammar

**LeetCode Problem #779 — K-th Symbol in Grammar**
Solve LeetCode K-th Symbol in Grammar using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | K-th Symbol in Grammar |
| LeetCode | #779 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
We build a table of  n  rows ( 1-indexed ). We start by writing  0  in the  1 st   row. Now in every subsequent row, we look at the previous row and replace each occurrence of  0  with  01 , and each occurrence of  1  with  10 .

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **K-th Symbol in Grammar**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Array / General**

## Topics
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)

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
- [440. K-th Smallest in Lexicographical Order](../0440-k-th-smallest-in-lexicographical-order/)
- [1415. The k-th Lexicographical String of All Happy Strings of Length n](../1516-the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/)
- [3154. Find Number of Ways to Reach the K-th Stair](../3414-find-number-of-ways-to-reach-the-k-th-stair/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/k-th-symbol-in-grammar/)
