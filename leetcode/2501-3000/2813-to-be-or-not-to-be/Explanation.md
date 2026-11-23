# LeetCode 2704: To Be Or Not To Be

**LeetCode Problem #2704 — To Be Or Not To Be**
Solve LeetCode To Be Or Not To Be using TypeScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | To Be Or Not To Be |
| LeetCode | #2704 |
| Difficulty | Easy |
| Language | TypeScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Write a function  expect  that helps developers test their code. It should take in any value  val  and return an object with the following two functions.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
`toBe` compares with `===` and throws "Not Equal" if they differ. `notToBe` throws "Equal" if they match. Otherwise both return `true`.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **To Be Or Not To Be**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [1160. Find Words That Can Be Formed by Characters](../../1001-1500/1112-find-words-that-can-be-formed-by-characters/)
- [1574. Shortest Subarray to be Removed to Make Array Sorted](../../1501-2000/1679-shortest-subarray-to-be-removed-to-make-array-sorted/)
- [1886. Determine Whether Matrix Can Be Obtained By Rotation](../../2001-2500/2015-determine-whether-matrix-can-be-obtained-by-rotation/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/to-be-or-not-to-be/)
