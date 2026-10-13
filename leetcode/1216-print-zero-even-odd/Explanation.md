# LeetCode 1116: Print Zero Even Odd

**LeetCode Problem #1116 — Print Zero Even Odd**
Solve LeetCode Print Zero Even Odd using Java and Linked List. This solution finds the optimal result using Pointer Traversal & Node Manipulation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Print Zero Even Odd |
| LeetCode | #1116 |
| Difficulty | Medium |
| Language | Java |
| Algorithm | Pointer Traversal & Node Manipulation |
| Data Structure | Linked List |
| Pattern | Linked List |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You have a function  printNumber  that can be called with an integer parameter and prints it to the console.

## Key Insight
Leverage **Linked List** with **Linked List** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code uses three **Semaphores** for synchronization.

1. **Semaphore State:** `zero` starts at `1` (goes first), `even` and `odd` start at `0`.
2. **zero thread:** For each number `i` from `1` to `n`, acquires the `zero` semaphore, prints `0`, then releases either `odd` (if `i` is odd) or `even` (if `i` is even).
3. **odd thread:** For each odd number, acquires the `odd` semaphore, prints the odd number, then releases `zero`.
4. **even thread:** For each even number, acquires the `even` semaphore, prints the even number, then releases `zero`.

This creates the pattern: zero→odd→zero→even→zero→odd→... producing `"010203..."`.

## Algorithm
1. Initialize state variables / data structure (**Linked List**).
2. Process elements sequentially using **Pointer Traversal & Node Manipulation**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Print Zero Even Odd**. Applying **Pointer Traversal & Node Manipulation** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Linked List**

## Topics
- Linked List
- Two Pointers

## Language
Java

## Source Code
- [solution.java](./solution.java)

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
- [3220. Odd and Even Transactions](../3530-odd-and-even-transactions/)
- [3658. GCD of Odd and Even Sums](../3995-gcd-of-odd-and-even-sums/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/print-zero-even-odd/)
