# LeetCode 2797: Partial Function with Placeholders

**LeetCode Problem #2797 — Partial Function with Placeholders**
Solve LeetCode Partial Function with Placeholders using TypeScript and Array / General. This solution finds the optimal result using Iterative Traversal in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Partial Function with Placeholders |
| LeetCode | #2797 |
| Difficulty | Easy |
| Language | TypeScript |
| Algorithm | Iterative Traversal |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Design an  EventEmitter  class. This interface is similar (but with some differences) to the one found in Node.js or the Event Target interface of the DOM. The  EventEmitter  should allow for subscribing to events and emitting them.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
Uses a Map where keys are event names and values are arrays of callbacks. `subscribe` adds a callback and returns an object with `unsubscribe`. `emit` calls all registered callbacks for the event with the provided args and returns their results.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Iterative Traversal**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Partial Function with Placeholders**. Applying **Iterative Traversal** yields the target result step by step.

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
- [5. Longest Palindromic Substring](../0005-longest-palindromic-substring/)
- [6. Zigzag Conversion](../0006-zigzag-conversion/)
- [193. Valid Phone Numbers](../0193-valid-phone-numbers/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/event-emitter/)
