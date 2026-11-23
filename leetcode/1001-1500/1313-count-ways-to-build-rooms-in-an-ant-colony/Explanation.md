# LeetCode 1916: Count Ways to Build Rooms in an Ant Colony

**LeetCode Problem #1916 — Count Ways to Build Rooms in an Ant Colony**
Solve LeetCode Count Ways to Build Rooms in an Ant Colony using JavaScript and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Ways to Build Rooms in an Ant Colony |
| LeetCode | #1916 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are an ant tasked with adding  n  new rooms numbered  0  to  n-1  to your colony. You are given the expansion plan as a  0-indexed  integer array of length  n ,  prevRoom , where  prevRoom[i]  indicates that you must build room  prevRoom[i]  before building room  i , and these two rooms must be connected  directly . Room  0  is already built, so  prevRoom[0] = -1 . The expansion plan is given such that once all the rooms are built, every room will be reachable from room  0 .

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Stack**).
2. Process elements sequentially using **Stack Push / Pop Parsing**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Count Ways to Build Rooms in an Ant Colony**. Applying **Stack Push / Pop Parsing** yields the target result step by step.

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
- [1735. Count Ways to Make Array With Product](../../1501-2000/1836-count-ways-to-make-array-with-product/)
- [3725. Count Ways to Choose Coprime Integers from Rows](../../4001-4500/4069-count-ways-to-choose-coprime-integers-from-rows/)
- [3028. Ant on the Boundary](../../3001-3500/3311-ant-on-the-boundary/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-ways-to-build-rooms-in-an-ant-colony/)
