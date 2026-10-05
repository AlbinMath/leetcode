# LeetCode 1188: Design Bounded Blocking Queue

**LeetCode Problem #1188 — Design Bounded Blocking Queue**
Solve LeetCode Design Bounded Blocking Queue using JavaScript and Array / General. This solution finds the optimal result using Iterative Traversal in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Design Bounded Blocking Queue |
| LeetCode | #1188 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Iterative Traversal |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Under the grammar given below, strings can represent a set of lowercase words. Let  R(expr)  denote the set of words the expression represents.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The solution implements a **Recursive Descent Parser** with three main functions to process the expression string according to the grammar.
1. `parseExpression()`: This function handles unions (comma-separated terms). It calls `parseTerm()` to get the first set of words. Then, as long as it encounters commas `,`, it skips them, calls `parseTerm()` again, and adds all resulting words into a single Set (which automatically removes duplicates).
2. `parseTerm()`: This function handles concatenation (adjacent factors). It starts with a base Set containing an empty string `[""]`. As long as it doesn't hit a `}` or `,`, it calls `parseFactor()` to get the next set of words. It then takes the Cartesian product of the current `result` Set and the new `factor` Set (combining every prefix with every new suffix) and updates the `result`.
3. `parseFactor()`: This function handles the smallest building blocks.
   - If the current character is a letter, it simply returns a Set containing that single letter and advances the index.
   - If it encounters a `{`, it skips it, calls `parseExpression()` recursively to evaluate the entire expression inside the braces, and then skips the closing `}`.
4. The main function starts by calling `parseExpression()`, converts the resulting Set to an Array, sorts it lexicographically as required, and returns it.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Iterative Traversal**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Design Bounded Blocking Queue**. Applying **Iterative Traversal** yields the target result step by step.

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
- [154. Find Minimum in Rotated Sorted Array II](../0154-find-minimum-in-rotated-sorted-array-ii/)
- [602. Friend Requests II: Who Has the Most Friends](../0602-friend-requests-ii-who-has-the-most-friends/)
- [977. Squares of a Sorted Array](../0977-distinct-subsequences-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/brace-expansion-ii/)
