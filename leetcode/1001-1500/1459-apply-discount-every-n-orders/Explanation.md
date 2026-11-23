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
- [1475. Final Prices With a Special Discount in a Shop](../../1501-2000/1570-final-prices-with-a-special-discount-in-a-shop/)
- [2144. Minimum Cost of Buying Candies With Discount](../../2001-2500/2248-minimum-cost-of-buying-candies-with-discount/)
- [50. Pow(x, n)](../../0001-0500/0050-powx-n/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/apply-discount-every-n-orders/)
