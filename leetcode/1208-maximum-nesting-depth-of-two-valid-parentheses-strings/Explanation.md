# LeetCode 1208: Get Equal Substrings Within Budget

**LeetCode Problem #1208 — Get Equal Substrings Within Budget**
Solve LeetCode Get Equal Substrings Within Budget using C++ and Database / SQL. This solution finds the optimal result using SQL Query / Relational Join & Grouping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Get Equal Substrings Within Budget |
| LeetCode | #1208 |
| Difficulty | Medium |
| Language | C++ |
| Algorithm | SQL Query / Relational Join & Grouping |
| Data Structure | Relational Table |
| Pattern | Database / SQL |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
A string is a  valid parentheses string  (denoted VPS) if and only if it consists of  "("  and  ")"  characters only, and:

## Key Insight
Leverage **Database / SQL** with **Relational Table** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Stack Push / Pop Traversal**. By maintaining state efficiently in a **Stack**, we eliminate redundant operations.

## Algorithm
1. Initialize state variables / data structure (**Relational Table**).
2. Process elements sequentially using **SQL Query / Relational Join & Grouping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Get Equal Substrings Within Budget**. Applying **SQL Query / Relational Join & Grouping** yields the target result step by step.

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
- [1737. Change Minimum Characters to Satisfy One of Three Conditions](../1737-maximum-nesting-depth-of-the-parentheses/)
- [20. Valid Parentheses](../0020-valid-parentheses/)
- [1574. Shortest Subarray to be Removed to Make Array Sorted](../1574-maximum-product-of-two-elements-in-an-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/)
