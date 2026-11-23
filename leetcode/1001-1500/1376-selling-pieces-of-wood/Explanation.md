# LeetCode 2312: Selling Pieces of Wood

**LeetCode Problem #2312 — Selling Pieces of Wood**
Solve LeetCode Selling Pieces of Wood using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Selling Pieces of Wood |
| LeetCode | #2312 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given two integers  m  and  n  that represent the height and width of a rectangular piece of wood. You are also given a 2D integer array  prices , where  prices[i] = [h i , w i , price i ]  indicates you can sell a rectangular piece of wood of height  h i   and width  w i   for  price i   dollars.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Selling Pieces of Wood**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [2038. Remove Colored Pieces if Both Neighbors are the Same Color](../../2001-2500/2149-remove-colored-pieces-if-both-neighbors-are-the-same-color/)
- [3426. Manhattan Distances of All Arrangements of Pieces](../../3501-4000/3739-manhattan-distances-of-all-arrangements-of-pieces/)
- [1251. Average Selling Price](../../1001-1500/1390-average-selling-price/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/selling-pieces-of-wood/)
