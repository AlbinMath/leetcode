# LeetCode 2693: Call Function with Custom Context

**LeetCode Problem #2693 — Call Function with Custom Context**
Solve LeetCode Call Function with Custom Context using TypeScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Call Function with Custom Context |
| LeetCode | #2693 |
| Difficulty | Medium |
| Language | TypeScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Enhance all functions to have the  callPolyfill  method. The method accepts an object  obj  as its first parameter and any number of additional arguments. The  obj  becomes the  this  context for the function. The additional arguments are passed to the function (that the  callPolyfill  method belongs on).

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
Temporarily assigns the function as a property of the `context` object, calls it with the provided arguments, then deletes the temporary property. Uses a Symbol to avoid property name collisions.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Call Function with Custom Context**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Array / General**

## Topics
- Array

## Language
TypeScript

## Source Code
- [solution.ts](./solution.ts)

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
- [2666. Allow One Function Call](../2796-allow-one-function-call/)
- [396. Rotate Function](../0396-rotate-function/)
- [2629. Function Composition](../2741-function-composition/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/call-function-with-custom-context/)
