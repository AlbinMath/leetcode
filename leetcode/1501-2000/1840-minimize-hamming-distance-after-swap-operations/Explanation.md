# LeetCode 1722: Minimize Hamming Distance After Swap Operations

**LeetCode Problem #1722 — Minimize Hamming Distance After Swap Operations**
Solve LeetCode Minimize Hamming Distance After Swap Operations using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimize Hamming Distance After Swap Operations |
| LeetCode | #1722 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given two integer arrays,  source  and  target , both of length  n . You are also given an array  allowedSwaps  where each  allowedSwaps[i] = [a i , b i ]  indicates that you are allowed to swap the elements at index  a i   and index  b i    (0-indexed)  of array  source . Note that you can swap elements at a specific pair of indices  multiple  times and in  any  order.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Minimize Hamming Distance After Swap Operations**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [3012. Minimize Length of Array Using Operations](../../3001-3500/3244-minimize-length-of-array-using-operations/)
- [3022. Minimize OR of Remaining Elements Using Operations](../../3001-3500/3261-minimize-or-of-remaining-elements-using-operations/)
- [461. Hamming Distance](../../0001-0500/0461-hamming-distance/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations/)
