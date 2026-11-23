# LeetCode 41: First Missing Positive

**LeetCode Problem #41 — First Missing Positive**
Solve LeetCode First Missing Positive using JavaScript, Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | First Missing Positive |
| LeetCode | #41 |
| Difficulty | Hard |
| Language | JavaScript, Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given an unsorted integer array  nums . Return the  smallest positive integer  that is  not present  in  nums .

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **First Missing Positive**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Array / General**

## Topics
- Array

## Language
JavaScript, Python

## Source Code
- [solution.js](./solution.js)
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
- [1539. Kth Missing Positive Number](../../1501-2000/1646-kth-missing-positive-number/)
- [1237. Find Positive Integer Solution for a Given Equation](../../1001-1500/1358-find-positive-integer-solution-for-a-given-equation/)
- [1413. Minimum Value to Get Positive Step by Step Sum](../../1501-2000/1514-minimum-value-to-get-positive-step-by-step-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/first-missing-positive/)
