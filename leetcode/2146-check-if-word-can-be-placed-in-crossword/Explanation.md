# LeetCode 2018: Check if Word Can Be Placed In Crossword

**LeetCode Problem #2018 — Check if Word Can Be Placed In Crossword**
Solve LeetCode Check if Word Can Be Placed In Crossword using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Check if Word Can Be Placed In Crossword |
| LeetCode | #2018 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given an  m x n  matrix  board , representing the  current  state of a crossword puzzle. The crossword contains lowercase English letters (from solved words),  &#39; &#39;  to represent any  empty  cells, and  &#39;#&#39;  to represent any  blocked  cells.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Check if Word Can Be Placed In Crossword**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Array / General**

## Topics
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)

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
- [2116. Check if a Parentheses String Can Be Valid](../2221-check-if-a-parentheses-string-can-be-valid/)
- [2267.  Check if There Is a Valid Parentheses String Path](../2349-check-if-there-is-a-valid-parentheses-string-path/)
- [1003. Check If Word Is Valid After Substitutions](../1045-check-if-word-is-valid-after-substitutions/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/check-if-word-can-be-placed-in-crossword/)
