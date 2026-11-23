# LeetCode 2597: The Number of Beautiful Subsets

**LeetCode Problem #2597 — The Number of Beautiful Subsets**
Solve LeetCode The Number of Beautiful Subsets using JavaScript and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | The Number of Beautiful Subsets |
| LeetCode | #2597 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given an array  nums  of positive integers and a  positive  integer  k .

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Integer Bitmask**).
2. Process elements sequentially using **Bitwise Masking & Bit Shift**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **The Number of Beautiful Subsets**. Applying **Bitwise Masking & Bit Shift** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Bit Manipulation**

## Topics
- Bit Manipulation
- Bitwise Math

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)

## Why This Works
By utilizing **Bit Manipulation**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [2588. Count the Number of Beautiful Subarrays](../../2501-3000/2656-count-the-number-of-beautiful-subarrays/)
- [2748. Number of Beautiful Pairs](../../2501-3000/2831-number-of-beautiful-pairs/)
- [2914. Minimum Number of Changes to Make Binary String Beautiful](../../3001-3500/3174-minimum-number-of-changes-to-make-binary-string-beautiful/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/the-number-of-beautiful-subsets/)
