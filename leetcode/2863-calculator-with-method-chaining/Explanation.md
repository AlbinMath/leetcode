# LeetCode 2863: Maximum Length of Semi-Decreasing Subarrays

**LeetCode Problem #2863 — Maximum Length of Semi-Decreasing Subarrays**
Solve LeetCode Maximum Length of Semi-Decreasing Subarrays using TypeScript and Math & Logic. This solution finds the optimal result using Mathematical Simulation / Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Length of Semi-Decreasing Subarrays |
| LeetCode | #2863 |
| Difficulty | Medium |
| Language | TypeScript |
| Algorithm | Mathematical Simulation / Modular Arithmetic |
| Data Structure | Primitive Data Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Design a  Calculator  class. The class should provide the mathematical operations of addition, subtraction, multiplication, division, and exponentiation. It should also allow consecutive operations to be performed using method chaining. The  Calculator  class constructor should accept a number which serves as the initial value of  result .

## Key Insight
Leverage **Math & Logic** with **Primitive Data Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
Each method (`add`, `subtract`, `multiply`, `divide`) modifies the internal `result` and returns `this` to enable chaining. `divide` throws an error if dividing by zero. `getResult` returns the current value.

## Algorithm
1. Initialize state variables / data structure (**Primitive Data Types**).
2. Process elements sequentially using **Mathematical Simulation / Modular Arithmetic**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Maximum Length of Semi-Decreasing Subarrays**. Applying **Mathematical Simulation / Modular Arithmetic** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Math & Logic**

## Topics
- Math
- Simulation

## Language
TypeScript

## Source Code
- [solution.ts](./solution.ts)

## Why This Works
By utilizing **Math & Logic**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [7. Reverse Integer](../0007-reverse-integer/)
- [48. Rotate Image](../0048-rotate-image/)
- [396. Rotate Function](../0396-rotate-function/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/calculator-with-method-chaining/)
