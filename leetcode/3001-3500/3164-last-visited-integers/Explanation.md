# LeetCode 2899: Last Visited Integers

**LeetCode Problem #2899 — Last Visited Integers**
Solve LeetCode Last Visited Integers using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Last Visited Integers |
| LeetCode | #2899 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given an integer array  nums  where  nums[i]  is either a positive integer or  -1 . We need to find for each  -1  the respective positive integer, which we call the last visited integer.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Last Visited Integers**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Array / General**

## Topics
- Array

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)

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
- [1560. Most Visited Sector in  a Circular Track](../../1501-2000/1682-most-visited-sector-in--a-circular-track/)
- [1581. Customer Who Visited but Did Not Make Any Transactions](../../1501-2000/1724-customer-who-visited-but-did-not-make-any-transactions/)
- [2617. Minimum Number of Visited Cells in a Grid](../../2501-3000/2697-minimum-number-of-visited-cells-in-a-grid/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/last-visited-integers/)
