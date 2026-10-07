# LeetCode 141: Linked List Cycle

**LeetCode Problem #141 — Linked List Cycle**
Solve LeetCode Linked List Cycle using PHP and Fast & Slow Pointers. This solution finds the optimal result using Floyd Cycle Detection in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Linked List Cycle |
| LeetCode | #141 |
| Difficulty | Easy |
| Language | PHP |
| Algorithm | Floyd Cycle Detection |
| Data Structure | Linked List / Pointer |
| Pattern | Fast & Slow Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given  head , the head of a linked list, determine if the linked list has a cycle in it.

## Key Insight
Leverage **Fast & Slow Pointers** with **Linked List / Pointer** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Floyd Cycle Detection**. By maintaining state efficiently in a **Linked List / Pointer**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Linked List / Pointer**).
2. Process elements sequentially using **Floyd Cycle Detection**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Linked List Cycle**. Applying **Floyd Cycle Detection** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Fast & Slow Pointers**

## Topics
- Two Pointers
- Cycle Detection

## Language
PHP

## Source Code
- [solution.php](./solution.php)

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
- [203. Remove Linked List Elements](../0203-remove-linked-list-elements/)
- [206. Reverse Linked List](../0206-reverse-linked-list/)
- [234. Palindrome Linked List](../0234-palindrome-linked-list/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/linked-list-cycle/)
