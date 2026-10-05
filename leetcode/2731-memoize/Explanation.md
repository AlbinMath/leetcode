# LeetCode 2731: Movement of Robots

**LeetCode Problem #2731 — Movement of Robots**
Solve LeetCode Movement of Robots using TypeScript and Database / SQL. This solution finds the optimal result using SQL Query / Relational Join & Grouping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Movement of Robots |
| LeetCode | #2731 |
| Difficulty | Medium |
| Language | TypeScript |
| Algorithm | SQL Query / Relational Join & Grouping |
| Data Structure | Relational Table |
| Pattern | Database / SQL |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Given a function  fn , return a  memoized  version of that function.

## Key Insight
Leverage **Database / SQL** with **Relational Table** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The memoize function wraps the input function with a closure that maintains a cache (Map/Object). Before calling the original function, it checks if the arguments have been seen before (using a key derived from the arguments). If cached, return the stored result; otherwise, call the function, store the result, and return it.

## Algorithm
1. Initialize state variables / data structure (**Relational Table**).
2. Process elements sequentially using **SQL Query / Relational Join & Grouping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Movement of Robots**. Applying **SQL Query / Relational Join & Grouping** yields the target result step by step.

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
TypeScript

## Source Code
- [solution.ts](./solution.ts)

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
- [2744. Find Maximum Number of String Pairs](../2744-memoize-ii/)
- [10. Regular Expression Matching](../0010-regular-expression-matching/)
- [12. Integer to Roman](../0012-integer-to-roman/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/memoize/)
