# LeetCode 1672: Richest Customer Wealth

**LeetCode Problem #1672 — Richest Customer Wealth**
Solve LeetCode Richest Customer Wealth using C++ and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Richest Customer Wealth |
| LeetCode | #1672 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given an  m x n  integer grid  accounts  where  accounts[i][j]  is the amount of money the  i​​​​​ ​​​​​​th ​​​​  customer has in the  j​​​​​ ​​​​​​th  ​​​​ bank. Return  the  wealth  that the richest customer has.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Richest Customer Wealth**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [584. Find Customer Referee](../0584-find-customer-referee/)
- [586. Customer Placing the Largest Number of Orders](../0586-customer-placing-the-largest-number-of-orders/)
- [1581. Customer Who Visited but Did Not Make Any Transactions](../1724-customer-who-visited-but-did-not-make-any-transactions/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/richest-customer-wealth/)
