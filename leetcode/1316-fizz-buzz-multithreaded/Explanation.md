# LeetCode 1316: Distinct Echo Substrings

**LeetCode Problem #1316 — Distinct Echo Substrings**
Solve LeetCode Distinct Echo Substrings using C++ and Array / General. This solution finds the optimal result using Iterative Traversal in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Distinct Echo Substrings |
| LeetCode | #1316 |
| Difficulty | Hard |
| Language | C++ |
| Algorithm | Iterative Traversal |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You have the four functions:

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code uses synchronization primitives (mutex + condition variable or semaphores) so that:
1. All four threads run in a loop from `1` to `n`.
2. At each step, only the thread whose condition matches the current number is allowed to proceed and print.
3. After printing, the current number is incremented and all threads are notified to check again.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Iterative Traversal**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Distinct Echo Substrings**. Applying **Iterative Traversal** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Array / General**

## Topics
- Array

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)

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
- [5. Longest Palindromic Substring](../0005-longest-palindromic-substring/)
- [6. Zigzag Conversion](../0006-zigzag-conversion/)
- [193. Valid Phone Numbers](../0193-valid-phone-numbers/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/fizz-buzz-multithreaded/)
