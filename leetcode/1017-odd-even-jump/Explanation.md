# LeetCode 975: Odd Even Jump

**LeetCode Problem #975 — Odd Even Jump**
Solve LeetCode Odd Even Jump using Python and Linked List. This solution finds the optimal result using Pointer Traversal & Node Manipulation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Odd Even Jump |
| LeetCode | #975 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Pointer Traversal & Node Manipulation |
| Data Structure | Linked List |
| Pattern | Linked List |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given an integer array  arr . From some starting index, you can make a series of jumps. The (1 st , 3 rd , 5 th , ...) jumps in the series are called  odd-numbered jumps , and the (2 nd , 4 th , 6 th , ...) jumps in the series are called  even-numbered jumps . Note that the  jumps  are numbered, not the indices.

## Key Insight
Leverage **Linked List** with **Linked List** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Linked List**).
2. Process elements sequentially using **Pointer Traversal & Node Manipulation**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Odd Even Jump**. Applying **Pointer Traversal & Node Manipulation** yields the target result step by step.

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
- [328. Odd Even Linked List](../0328-odd-even-linked-list/)
- [1116. Print Zero Even Odd](../1216-print-zero-even-odd/)
- [1609. Even Odd Tree](../1731-even-odd-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/odd-even-jump/)
