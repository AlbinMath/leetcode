# LeetCode 2039: The Time When the Network Becomes Idle

**LeetCode Problem #2039 — The Time When the Network Becomes Idle**
Solve LeetCode The Time When the Network Becomes Idle using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | The Time When the Network Becomes Idle |
| LeetCode | #2039 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
There is a network of  n  servers, labeled from  0  to  n - 1 . You are given a 2D integer array  edges , where  edges[i] = [u i , v i ]  indicates there is a message channel between servers  u i   and  v i  , and they can pass  any  number of messages to  each other  directly in  one  second. You are also given a  0-indexed  integer array  patience  of length  n .

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **The Time When the Network Becomes Idle**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [743. Network Delay Time](../0744-network-delay-time/)
- [803. Bricks Falling When Hit](../0821-bricks-falling-when-hit/)
- [121. Best Time to Buy and Sell Stock](../0121-best-time-to-buy-and-sell-stock/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/the-time-when-the-network-becomes-idle/)
