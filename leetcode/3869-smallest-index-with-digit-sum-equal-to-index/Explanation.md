# LeetCode 3550: Smallest Index With Digit Sum Equal to Index

**LeetCode Problem #3550 — Smallest Index With Digit Sum Equal to Index**
Solve LeetCode Smallest Index With Digit Sum Equal to Index using JavaScript and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Smallest Index With Digit Sum Equal to Index |
| LeetCode | #3550 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given an integer array  nums .

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code uses a straightforward iterative approach.
1. It uses a `for` loop to iterate through the array from the first element (index `0`) to the last. This naturally ensures we find the smallest index first.
2. For each index `i`, it takes the number `nums[i]`.
3. It calculates the sum of the digits of the number using a `while` loop:
   - `num % 10` extracts the last digit of the number, which is added to `sum`.
   - `Math.floor(num / 10)` removes the last digit from the number.
   - This repeats until all digits have been processed and `num` becomes 0.
4. It compares the calculated `sum` with the current index `i`.
   - If `sum === i`, it immediately returns `i`, fulfilling the condition of finding the smallest index.
5. If the loop finishes checking all elements without returning, it means no such index exists, so it returns `-1`.

## Algorithm
1. Initialize state variables / data structure (**Primitive Types**).
2. Process elements sequentially using **Mathematical Simulation & Modular Arithmetic**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Smallest Index With Digit Sum Equal to Index**. Applying **Mathematical Simulation & Modular Arithmetic** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Math & Logic**

## Topics
- Math
- Simulation

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)

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
- [2996. Smallest Missing Integer Greater Than Sequential Prefix Sum](../3236-smallest-missing-integer-greater-than-sequential-prefix-sum/)
- [3300. Minimum Element After Replacement With Digit Sum](../3606-minimum-element-after-replacement-with-digit-sum/)
- [3345. Smallest Divisible Digit Product I](../3626-smallest-divisible-digit-product-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/)
