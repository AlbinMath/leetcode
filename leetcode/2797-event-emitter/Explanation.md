# LeetCode 2694: Event Emitter

**LeetCode Problem #2694 — Event Emitter**
Solve LeetCode Event Emitter using TypeScript and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Event Emitter |
| LeetCode | #2694 |
| Difficulty | Medium |
| Language | TypeScript |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Design an  EventEmitter  class. This interface is similar (but with some differences) to the one found in Node.js or the Event Target interface of the DOM. The  EventEmitter  should allow for subscribing to events and emitting them.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
Uses a Map where keys are event names and values are arrays of callbacks. `subscribe` adds a callback and returns an object with `unsubscribe`. `emit` calls all registered callbacks for the event with the provided args and returns their results.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Event Emitter**. Applying **Depth-First Search (DFS) / Breadth-First Search (BFS)** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

## Pattern
**Tree & Graph**

## Topics
- Tree
- Graph
- DFS
- BFS

## Language
TypeScript

## Source Code
- [solution.ts](./solution.ts)

## Why This Works
By utilizing **Tree & Graph**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [675. Cut Off Trees for Golf Event](../0675-cut-off-trees-for-golf-event/)
- [3317. Find the Number of Possible Ways for an Event](../3604-find-the-number-of-possible-ways-for-an-event/)
- [3885. Design Event Manager](../4267-design-event-manager/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/event-emitter/)
