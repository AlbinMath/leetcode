# LeetCode 406: Queue Reconstruction by Height

**LeetCode Problem #406 — Queue Reconstruction by Height**
Solve LeetCode Queue Reconstruction by Height using JavaScript and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Queue Reconstruction by Height |
| LeetCode | #406 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given an array of people,  people , which are the attributes of some people in a queue (not necessarily in order). Each  people[i] = [h i , k i ]  represents the  i th   person of height  h i   with  exactly   k i   other people in front who have a height greater than or equal to  h i  .

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Stack**).
2. Process elements sequentially using **Stack Push / Pop Parsing**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Queue Reconstruction by Height**. Applying **Stack Push / Pop Parsing** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)

## Why This Works
By utilizing **Stack & Queue**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [232. Implement Queue using Stacks](../0232-implement-queue-using-stacks/)
- [1051. Height Checker](../1137-height-checker/)
- [1840. Maximum Building Height](../1968-maximum-building-height/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/queue-reconstruction-by-height/)
