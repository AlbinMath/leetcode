# LeetCode 1316: Distinct Echo Substrings

**LeetCode Problem #1316 — Distinct Echo Substrings**
Solve LeetCode Distinct Echo Substrings using C++ and Database / SQL. This solution finds the optimal result using SQL Query / Relational Join & Grouping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Distinct Echo Substrings |
| LeetCode | #1316 |
| Difficulty | Hard |
| Language | C++ |
| Algorithm | SQL Query / Relational Join & Grouping |
| Data Structure | Relational Table |
| Pattern | Database / SQL |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You have the four functions:

## Key Insight
Leverage **Database / SQL** with **Relational Table** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code uses synchronization primitives (mutex + condition variable or semaphores) so that:
1. All four threads run in a loop from `1` to `n`.
2. At each step, only the thread whose condition matches the current number is allowed to proceed and print.
3. After printing, the current number is incremented and all threads are notified to check again.

## Algorithm
1. Initialize state variables / data structure (**Relational Table**).
2. Process elements sequentially using **SQL Query / Relational Join & Grouping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Distinct Echo Substrings**. Applying **SQL Query / Relational Join & Grouping** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

## Pattern
**Database / SQL**

## Topics
- Database
- SQL
- Data Aggregation

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)

## Why This Works
By utilizing **Database / SQL**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [10. Regular Expression Matching](../0010-regular-expression-matching/)
- [12. Integer to Roman](../0012-integer-to-roman/)
- [13. Roman to Integer](../0013-roman-to-integer/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/fizz-buzz-multithreaded/)
