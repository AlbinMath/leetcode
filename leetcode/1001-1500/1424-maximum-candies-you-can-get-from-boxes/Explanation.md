# LeetCode 1298: Maximum Candies You Can Get from Boxes

**LeetCode Problem #1298 — Maximum Candies You Can Get from Boxes**
Solve LeetCode Maximum Candies You Can Get from Boxes using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Candies You Can Get from Boxes |
| LeetCode | #1298 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You have  n  boxes labeled from  0  to  n - 1 . You are given four arrays:  status ,  candies ,  keys , and  containedBoxes  where:

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Maximum Candies You Can Get from Boxes**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [1423. Maximum Points You Can Obtain from Cards](../../1501-2000/1538-maximum-points-you-can-obtain-from-cards/)
- [1561. Maximum Number of Coins You Can Get](../../1501-2000/1683-maximum-number-of-coins-you-can-get/)
- [1935. Maximum Number of Words You Can Type](../../1001-1500/1264-maximum-number-of-words-you-can-type/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes/)
