# LeetCode 2071: Maximum Number of Tasks You Can Assign

**LeetCode Problem #2071 — Maximum Number of Tasks You Can Assign**
Solve LeetCode Maximum Number of Tasks You Can Assign using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Number of Tasks You Can Assign |
| LeetCode | #2071 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You have  n  tasks and  m  workers. Each task has a strength requirement stored in a  0-indexed  integer array  tasks , with the  i th   task requiring  tasks[i]  strength to complete. The strength of each worker is stored in a  0-indexed  integer array  workers , with the  j th   worker having  workers[j]  strength. Each worker can only be assigned to a  single  task and must have a strength  greater than or equal  to the task&#39;s strength requirement (i.e.,  workers[j] >= tasks[i] ).

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Maximum Number of Tasks You Can Assign**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [1561. Maximum Number of Coins You Can Get](../1683-maximum-number-of-coins-you-can-get/)
- [1935. Maximum Number of Words You Can Type](../1264-maximum-number-of-words-you-can-type/)
- [1298. Maximum Candies You Can Get from Boxes](../1424-maximum-candies-you-can-get-from-boxes/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-number-of-tasks-you-can-assign/)
