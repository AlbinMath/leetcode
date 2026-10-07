# LeetCode 1096: Brace Expansion II

**LeetCode Problem #1096 — Brace Expansion II**
Solve LeetCode Brace Expansion II using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Brace Expansion II |
| LeetCode | #1096 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
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
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Brace Expansion II**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [40. Combination Sum II](../0040-combination-sum-ii/)
- [45. Jump Game II](../0045-jump-game-ii/)
- [47. Permutations II](../0047-permutations-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/brace-expansion-ii/)
