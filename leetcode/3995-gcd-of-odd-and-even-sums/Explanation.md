# LeetCode 3658: GCD of Odd and Even Sums

**LeetCode Problem #3658 — GCD of Odd and Even Sums**
Solve LeetCode GCD of Odd and Even Sums using Kotlin and Linked List. This solution finds the optimal result using Pointer Traversal & Node Manipulation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | GCD of Odd and Even Sums |
| LeetCode | #3658 |
| Difficulty | Easy |
| Language | Kotlin |
| Algorithm | Pointer Traversal & Node Manipulation |
| Data Structure | Linked List |
| Pattern | Linked List |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given an integer  n . Your task is to compute the  GCD  (greatest common divisor) of two values:

## Key Insight
Leverage **Linked List** with **Linked List** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Iterative Traversal**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Linked List**).
2. Process elements sequentially using **Pointer Traversal & Node Manipulation**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **GCD of Odd and Even Sums**. Applying **Pointer Traversal & Node Manipulation** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Linked List**

## Topics
- Linked List
- Two Pointers

## Language
Kotlin

## Source Code
- [solution.kt](./solution.kt)

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
- [3220. Odd and Even Transactions](../3530-odd-and-even-transactions/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/gcd-of-odd-and-even-sums/)
