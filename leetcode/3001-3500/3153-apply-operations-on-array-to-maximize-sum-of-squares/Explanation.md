# LeetCode 2897: Apply Operations on Array to Maximize Sum of Squares

**LeetCode Problem #2897 — Apply Operations on Array to Maximize Sum of Squares**
Solve LeetCode Apply Operations on Array to Maximize Sum of Squares using JavaScript and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Apply Operations on Array to Maximize Sum of Squares |
| LeetCode | #2897 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given a  0-indexed  integer array  nums  and a  positive  integer  k .

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Bitwise Masking & Bit Shift**. By maintaining state efficiently in a **Integer Bitmask**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Stack**).
2. Process elements sequentially using **Stack Push / Pop Parsing**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Apply Operations on Array to Maximize Sum of Squares**. Applying **Stack Push / Pop Parsing** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)

## Why This Works
By utilizing **Stack & Queue**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [3091. Apply Operations to Make Sum of Array Greater Than or Equal to k](../../3001-3500/3328-apply-operations-to-make-sum-of-array-greater-than-or-equal-to-k/)
- [1005. Maximize Sum Of Array After K Negations](../../1001-1500/1047-maximize-sum-of-array-after-k-negations/)
- [2460. Apply Operations to an Array](../../2501-3000/2551-apply-operations-to-an-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/apply-operations-on-array-to-maximize-sum-of-squares/)
