# LeetCode 1340: Jump Game V

**LeetCode Problem #1340 — Jump Game V**
Solve LeetCode Jump Game V using C++ and Array / General. This solution finds the optimal result using Iterative Traversal in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Jump Game V |
| LeetCode | #1340 |
| Difficulty | Hard |
| Language | C++ |
| Algorithm | Iterative Traversal |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Five silent philosophers sit at a round table with bowls of spaghetti. Forks are placed between each pair of adjacent philosophers.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code uses `std::lock` with `defer_lock` to acquire both forks atomically.

1. Each fork is represented by a `mutex`. Philosopher `i` needs forks `i` and `(i+1) % 5`.
2. `unique_lock` with `defer_lock` creates lock guards without immediately locking.
3. `std::lock(leftLock, rightLock)` acquires both locks simultaneously using a deadlock-avoidance algorithm.
4. The philosopher picks up forks, eats, puts them down, and the locks are automatically released when the `unique_lock` objects go out of scope.

This eliminates deadlocks because `std::lock` uses an internal ordering to prevent circular wait.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Iterative Traversal**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Jump Game V**. Applying **Iterative Traversal** yields the target result step by step.

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
- [14. Longest Common Prefix](../0014-longest-common-prefix/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/the-dining-philosophers/)
