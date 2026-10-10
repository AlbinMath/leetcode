# LeetCode 1903: Largest Odd Number in String

**LeetCode Problem #1903 — Largest Odd Number in String**
Solve LeetCode Largest Odd Number in String using C++ and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Largest Odd Number in String |
| LeetCode | #1903 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given a string  num , representing a large integer. Return  the  largest-valued odd  integer (as a string) that is a  non-empty substring  of   num  , or an empty string   ""   if no odd integer exists .

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Largest Odd Number in String**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [434. Number of Segments in a String](../0434-number-of-segments-in-a-string/)
- [586. Customer Placing the Largest Number of Orders](../0586-customer-placing-the-largest-number-of-orders/)
- [747. Largest Number At Least Twice of Others](../0748-largest-number-at-least-twice-of-others/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/largest-odd-number-in-string/)
