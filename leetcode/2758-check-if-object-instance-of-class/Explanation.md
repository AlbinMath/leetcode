# LeetCode 2618: Check if Object Instance of Class

**LeetCode Problem #2618 — Check if Object Instance of Class**
Solve LeetCode Check if Object Instance of Class using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Check if Object Instance of Class |
| LeetCode | #2618 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Write a function that checks if a given value is an instance of a given class or superclass. For this problem, an object is considered an instance of a given class if that object has access to that class&#39;s methods.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
Walk up the prototype chain of `obj` using `Object.getPrototypeOf()`. At each step, check if the prototype matches `classFunction.prototype`. Return true if found, false if the chain ends (null).

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Check if Object Instance of Class**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [1232. Check If It Is a Straight Line](../1349-check-if-it-is-a-straight-line/)
- [1346. Check If N and Its Double Exist](../1468-check-if-n-and-its-double-exist/)
- [1437. Check If All 1's Are at Least Length K Places Away](../1548-check-if-all-1s-are-at-least-length-k-places-away/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/check-if-object-instance-of-class/)
