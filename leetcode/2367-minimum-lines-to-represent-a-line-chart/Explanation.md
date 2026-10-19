# LeetCode 2280: Minimum Lines to Represent a Line Chart

**LeetCode Problem #2280 — Minimum Lines to Represent a Line Chart**
Solve LeetCode Minimum Lines to Represent a Line Chart using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Lines to Represent a Line Chart |
| LeetCode | #2280 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given a 2D integer array  stockPrices  where  stockPrices[i] = [day i , price i ]  indicates the price of the stock on day  day i   is  price i  . A  line chart  is created from the array by plotting the points on an XY plane with the X-axis representing the day and the Y-axis representing the price and connecting adjacent points. One such example is shown below:

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Minimum Lines to Represent a Line Chart**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Array / General**

## Topics
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)

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
- [64. Minimum Path Sum](../0064-minimum-path-sum/)
- [76. Minimum Window Substring](../0076-minimum-window-substring/)
- [111. Minimum Depth of Binary Tree](../0111-minimum-depth-of-binary-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-lines-to-represent-a-line-chart/)
