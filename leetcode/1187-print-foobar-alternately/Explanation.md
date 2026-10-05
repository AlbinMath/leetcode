# LeetCode 1115: Print FooBar Alternately

**LeetCode Problem #1115 — Print FooBar Alternately**
Solve LeetCode Print FooBar Alternately using Java and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Print FooBar Alternately |
| LeetCode | #1115 |
| Difficulty | Medium |
| Language | Java |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Suppose you are given the following code:

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
The code uses **Semaphores** for synchronization.

1. `fooSem` starts at `1` (foo can go first) and `barSem` starts at `0` (bar must wait).
2. **foo thread:** Acquires `fooSem`, prints "foo", then releases `barSem` (allowing bar to proceed).
3. **bar thread:** Acquires `barSem`, prints "bar", then releases `fooSem` (allowing foo to proceed again).

This ping-pong of semaphores ensures strict alternation for `n` iterations.

## Algorithm
1. Initialize state variables / data structure (**Dictionary / Hash Map**).
2. Process elements sequentially using **Complement Lookup / Hash Table Frequency**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Print FooBar Alternately**. Applying **Complement Lookup / Hash Table Frequency** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

## Pattern
**Hash Map**

## Topics
- Hash Table
- Array
- Complement Lookup

## Language
Java

## Source Code
- [solution.java](./solution.java)

## Why This Works
By utilizing **Hash Map**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Using the same element twice.
2. Checking the map before inserting elements in the correct order.
3. Inefficient hash functions or unnecessary duplicate key updates.

## Interview Notes
- **Tests:** Hash map usage, complement/frequency lookup, and $O(n)$ time optimization.
- **Follow-up:** Can you solve the problem in $O(1)$ extra space if the input array is sorted?

## Related Problems
- [1114. Print in Order](../1203-print-in-order/)
- [1116. Print Zero Even Odd](../1216-print-zero-even-odd/)
- [1. Two Sum](../0001-two-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/print-foobar-alternately/)
