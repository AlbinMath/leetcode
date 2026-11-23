# LeetCode 1202: Smallest String With Swaps

**LeetCode Problem #1202 — Smallest String With Swaps**
Solve LeetCode Smallest String With Swaps using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Smallest String With Swaps |
| LeetCode | #1202 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given a string  s , and an array of pairs of indices in the string  pairs  where  pairs[i] = [a, b]  indicates 2 indices(0-indexed) of the string.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Smallest String With Swaps**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [988. Smallest String Starting From Leaf](../../1001-1500/1030-smallest-string-starting-from-leaf/)
- [1061. Lexicographically Smallest Equivalent String](../../1001-1500/1058-lexicographically-smallest-equivalent-string/)
- [1625. Lexicographically Smallest String After Applying Operations](../../1501-2000/1747-lexicographically-smallest-string-after-applying-operations/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/smallest-string-with-swaps/)
