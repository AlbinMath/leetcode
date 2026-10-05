# LeetCode 1212: Team Scores in Football Tournament

**LeetCode Problem #1212 — Team Scores in Football Tournament**
Solve LeetCode Team Scores in Football Tournament using C++ and Math & Logic. This solution finds the optimal result using Mathematical Simulation / Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Team Scores in Football Tournament |
| LeetCode | #1212 |
| Difficulty | Medium |
| Language | C++ |
| Algorithm | Mathematical Simulation / Modular Arithmetic |
| Data Structure | Primitive Data Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
An integer has  sequential digits  if and only if each digit in the number is one more than the previous digit.

## Key Insight
Leverage **Math & Logic** with **Primitive Data Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code generates all possible sequential digit numbers and filters those within the range.

1. It starts from each digit `1` through `9` as the first digit.
2. For each starting digit, it builds numbers by appending the next consecutive digit (e.g., starting from `1`: `1 → 12 → 123 → 1234 → ...`).
3. If a generated number falls within `[low, high]`, it's added to the result.
4. The generation stops when the next digit exceeds `9` or the number exceeds `high`.
5. The result is sorted before returning.

Since there are at most 36 sequential-digit numbers (9 possible lengths × varying starts), this runs in $O(1)$ time.

## Algorithm
1. Initialize state variables / data structure (**Primitive Data Types**).
2. Process elements sequentially using **Mathematical Simulation / Modular Arithmetic**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Team Scores in Football Tournament**. Applying **Mathematical Simulation / Modular Arithmetic** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Math & Logic**

## Topics
- Math
- Simulation

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)

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
- [804. Unique Morse Code Words](../0804-rotated-digits/)
- [2639. Find the Width of Columns of a Grid](../2639-separate-the-digits-in-an-array/)
- [3236. CEO Subordinate Hierarchy](../3236-smallest-missing-integer-greater-than-sequential-prefix-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/sequential-digits/)
