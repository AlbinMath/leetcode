# LeetCode 1216: Valid Palindrome III

**LeetCode Problem #1216 — Valid Palindrome III**
Solve LeetCode Valid Palindrome III using Java and Database / SQL. This solution finds the optimal result using SQL Query / Relational Join & Grouping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Valid Palindrome III |
| LeetCode | #1216 |
| Difficulty | Hard |
| Language | Java |
| Algorithm | SQL Query / Relational Join & Grouping |
| Data Structure | Relational Table |
| Pattern | Database / SQL |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You have a function  printNumber  that can be called with an integer parameter and prints it to the console.

## Key Insight
Leverage **Database / SQL** with **Relational Table** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code uses three **Semaphores** for synchronization.

1. **Semaphore State:** `zero` starts at `1` (goes first), `even` and `odd` start at `0`.
2. **zero thread:** For each number `i` from `1` to `n`, acquires the `zero` semaphore, prints `0`, then releases either `odd` (if `i` is odd) or `even` (if `i` is even).
3. **odd thread:** For each odd number, acquires the `odd` semaphore, prints the odd number, then releases `zero`.
4. **even thread:** For each even number, acquires the `even` semaphore, prints the even number, then releases `zero`.

This creates the pattern: zero→odd→zero→even→zero→odd→... producing `"010203..."`.

## Algorithm
1. Initialize state variables / data structure (**Relational Table**).
2. Process elements sequentially using **SQL Query / Relational Join & Grouping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Valid Palindrome III**. Applying **SQL Query / Relational Join & Grouping** yields the target result step by step.

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
Java

## Source Code
- [solution.java](./solution.java)

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
- [3995. Minimum Cost to Convert String III](../3995-gcd-of-odd-and-even-sums/)
- [1187. Make Array Strictly Increasing](../1187-print-foobar-alternately/)
- [1203. Sort Items by Groups Respecting Dependencies](../1203-print-in-order/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/print-zero-even-odd/)
