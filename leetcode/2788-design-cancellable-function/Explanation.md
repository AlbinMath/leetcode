# LeetCode 2650: Design Cancellable Function

**LeetCode Problem #2650 — Design Cancellable Function**
Solve LeetCode Design Cancellable Function using TypeScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Design Cancellable Function |
| LeetCode | #2650 |
| Difficulty | Hard |
| Language | TypeScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Sometimes you have a long running task, and you may wish to cancel it before it completes. To help with this goal, write a function  cancellable  that accepts a generator object and returns an array of two values: a  cancel function  and a  promise .

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
Wraps the generator execution in a promise. Maintains a reference to allow cancellation. When `cancel()` is called, it throws an error into the generator via `generator.throw()`, causing the generator to reject.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Design Cancellable Function**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [396. Rotate Function](../0396-rotate-function/)
- [705. Design HashSet](../0816-design-hashset/)
- [706. Design HashMap](../0817-design-hashmap/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/design-cancellable-function/)
