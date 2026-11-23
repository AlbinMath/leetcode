# LeetCode 1071: Greatest Common Divisor of Strings

**LeetCode Problem #1071 — Greatest Common Divisor of Strings**
Solve LeetCode Greatest Common Divisor of Strings using JavaScript, Python and Linked List. This solution finds the optimal result using Pointer Traversal & Node Manipulation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Greatest Common Divisor of Strings |
| LeetCode | #1071 |
| Difficulty | Easy |
| Language | JavaScript, Python |
| Algorithm | Pointer Traversal & Node Manipulation |
| Data Structure | Linked List |
| Pattern | Linked List |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
For two strings  s  and  t , we say " t  divides  s " if and only if  s = t + t + t + ... + t + t  (i.e.,  t  is concatenated with itself one or more times).

## Key Insight
Leverage **Linked List** with **Linked List** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Linked List**).
2. Process elements sequentially using **Pointer Traversal & Node Manipulation**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Greatest Common Divisor of Strings**. Applying **Pointer Traversal & Node Manipulation** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Linked List**

## Topics
- Linked List
- Two Pointers

## Language
JavaScript, Python

## Source Code
- [solution.js](./solution.js)
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
- [1979. Find Greatest Common Divisor of Array](../2106-find-greatest-common-divisor-of-array/)
- [2709. Greatest Common Divisor Traversal](../2827-greatest-common-divisor-traversal/)
- [2807. Insert Greatest Common Divisors in Linked List](../2903-insert-greatest-common-divisors-in-linked-list/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/greatest-common-divisor-of-strings/)
