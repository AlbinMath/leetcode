# LeetCode 632: Smallest Range Covering Elements from K Lists

**LeetCode Problem #632 — Smallest Range Covering Elements from K Lists**
Solve LeetCode Smallest Range Covering Elements from K Lists using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Smallest Range Covering Elements from K Lists |
| LeetCode | #632 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You have  k  lists of sorted integers in  non-decreasing order . Find the  smallest  range that includes at least one number from each of the  k  lists.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Smallest Range Covering Elements from K Lists**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [988. Smallest String Starting From Leaf](../1030-smallest-string-starting-from-leaf/)
- [2375. Construct Smallest Number From DI String](../2456-construct-smallest-number-from-di-string/)
- [2516. Take K of Each Character From Left and Right](../2599-take-k-of-each-character-from-left-and-right/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/)
