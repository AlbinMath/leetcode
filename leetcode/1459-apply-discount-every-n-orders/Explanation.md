# LeetCode 1357: Apply Discount Every n Orders

**LeetCode Problem #1357 — Apply Discount Every n Orders**
Solve LeetCode Apply Discount Every n Orders using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Apply Discount Every n Orders |
| LeetCode | #1357 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
There is a supermarket that is frequented by many customers. The products sold at the supermarket are represented as two parallel integer arrays  products  and  prices , where the  i th   product has an ID of  products[i]  and a price of  prices[i] .

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Apply Discount Every n Orders**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [586. Customer Placing the Largest Number of Orders](../0586-customer-placing-the-largest-number-of-orders/)
- [1418. Display Table of Food Orders in a Restaurant](../1533-display-table-of-food-orders-in-a-restaurant/)
- [1801. Number of Orders in the Backlog](../1928-number-of-orders-in-the-backlog/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/apply-discount-every-n-orders/)
