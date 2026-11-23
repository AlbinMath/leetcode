# LeetCode 2709: Greatest Common Divisor Traversal

**LeetCode Problem #2709 — Greatest Common Divisor Traversal**
Solve LeetCode Greatest Common Divisor Traversal using Python and Linked List. This solution finds the optimal result using Pointer Traversal & Node Manipulation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Greatest Common Divisor Traversal |
| LeetCode | #2709 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Pointer Traversal & Node Manipulation |
| Data Structure | Linked List |
| Pattern | Linked List |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given a  0-indexed  integer array  nums , and you are allowed to  traverse  between its indices. You can traverse between index  i  and index  j ,  i != j , if and only if  gcd(nums[i], nums[j]) > 1 , where  gcd  is the  greatest common divisor .

## Key Insight
Leverage **Linked List** with **Linked List** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Linked List**).
2. Process elements sequentially using **Pointer Traversal & Node Manipulation**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Greatest Common Divisor Traversal**. Applying **Pointer Traversal & Node Manipulation** yields the target result step by step.

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
- [1071. Greatest Common Divisor of Strings](../1146-greatest-common-divisor-of-strings/)
- [1979. Find Greatest Common Divisor of Array](../2106-find-greatest-common-divisor-of-array/)
- [2807. Insert Greatest Common Divisors in Linked List](../2903-insert-greatest-common-divisors-in-linked-list/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/greatest-common-divisor-traversal/)
