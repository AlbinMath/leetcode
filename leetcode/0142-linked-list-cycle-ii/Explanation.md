# LeetCode 142: Linked List Cycle II

**LeetCode Problem #142 — Linked List Cycle II**
Solve LeetCode Linked List Cycle II using Python and Fast & Slow Pointers. This solution finds the optimal result using Floyd Cycle Detection in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Linked List Cycle II |
| LeetCode | #142 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Floyd Cycle Detection |
| Data Structure | Linked List / Pointer |
| Pattern | Fast & Slow Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given the  head  of a linked list, return  the node where the cycle begins. If there is no cycle, return   null .

## Key Insight
Leverage **Fast & Slow Pointers** with **Linked List / Pointer** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Floyd Cycle Detection**. By maintaining state efficiently in a **Linked List / Pointer**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Linked List / Pointer**).
2. Process elements sequentially using **Floyd Cycle Detection**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Linked List Cycle II**. Applying **Floyd Cycle Detection** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Fast & Slow Pointers**

## Topics
- Two Pointers
- Cycle Detection

## Language
Python

## Source Code
- [solution.py](./solution.py)

## Why This Works
By utilizing **Fast & Slow Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [92. Reverse Linked List II](../0092-reverse-linked-list-ii/)
- [141. Linked List Cycle](../0141-linked-list-cycle/)
- [82. Remove Duplicates from Sorted List II](../0082-remove-duplicates-from-sorted-list-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/linked-list-cycle-ii/)
