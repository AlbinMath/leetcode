# LeetCode 806: Number of Lines To Write String

**LeetCode Problem #806 — Number of Lines To Write String**
Solve LeetCode Number of Lines To Write String using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Lines To Write String |
| LeetCode | #806 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given a string  s  of lowercase English letters and an array  widths  denoting  how many pixels wide  each lowercase English letter is. Specifically,  widths[0]  is the width of  &#39;a&#39; ,  widths[1]  is the width of  &#39;b&#39; , and so on.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Number of Lines To Write String**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [434. Number of Segments in a String](../0434-number-of-segments-in-a-string/)
- [1805. Number of Different Integers in a String](../1933-number-of-different-integers-in-a-string/)
- [1903. Largest Odd Number in String](../2032-largest-odd-number-in-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-lines-to-write-string/)
