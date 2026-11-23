# LeetCode 2526: Find Consecutive Integers from a Data Stream

**LeetCode Problem #2526 — Find Consecutive Integers from a Data Stream**
Solve LeetCode Find Consecutive Integers from a Data Stream using Python and Linked List. This solution finds the optimal result using Pointer Traversal & Node Manipulation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Consecutive Integers from a Data Stream |
| LeetCode | #2526 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Pointer Traversal & Node Manipulation |
| Data Structure | Linked List |
| Pattern | Linked List |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
For a stream of integers, implement a data structure that checks if the last  k  integers parsed in the stream are  equal  to  value .

## Key Insight
Leverage **Linked List** with **Linked List** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Linked List**).
2. Process elements sequentially using **Pointer Traversal & Node Manipulation**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Find Consecutive Integers from a Data Stream**. Applying **Pointer Traversal & Node Manipulation** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Linked List**

## Topics
- Linked List
- Two Pointers

## Language
Python

## Source Code
- [solution.py](./solution.py)

## Why This Works
By utilizing **Linked List**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [295. Find Median from Data Stream](../../0001-0500/0295-find-median-from-data-stream/)
- [2177. Find Three Consecutive Integers That Sum to a Given Number](../../2001-2500/2278-find-three-consecutive-integers-that-sum-to-a-given-number/)
- [2115. Find All Possible Recipes from Given Supplies](../../2001-2500/2220-find-all-possible-recipes-from-given-supplies/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/)
