# LeetCode 1291: Sequential Digits

**LeetCode Problem #1291 — Sequential Digits**
Solve LeetCode Sequential Digits using C++ and Prefix Sum. This solution finds the optimal result using Prefix Sum Precomputation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Sequential Digits |
| LeetCode | #1291 |
| Difficulty | Medium |
| Language | C++ |
| Algorithm | Prefix Sum Precomputation |
| Data Structure | Prefix Array |
| Pattern | Prefix Sum |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
An integer has  sequential digits  if and only if each digit in the number is one more than the previous digit.

## Key Insight
Leverage **Prefix Sum** with **Prefix Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code generates all possible sequential digit numbers and filters those within the range.

1. It starts from each digit `1` through `9` as the first digit.
2. For each starting digit, it builds numbers by appending the next consecutive digit (e.g., starting from `1`: `1 → 12 → 123 → 1234 → ...`).
3. If a generated number falls within `[low, high]`, it's added to the result.
4. The generation stops when the next digit exceeds `9` or the number exceeds `high`.
5. The result is sorted before returning.

Since there are at most 36 sequential-digit numbers (9 possible lengths × varying starts), this runs in $O(1)$ time.

## Algorithm
1. Initialize state variables / data structure (**Prefix Array**).
2. Process elements sequentially using **Prefix Sum Precomputation**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Sequential Digits**. Applying **Prefix Sum Precomputation** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

## Pattern
**Prefix Sum**

## Topics
- Prefix Sum
- Array

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)

## Why This Works
By utilizing **Prefix Sum**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [258. Add Digits](../0258-add-digits/)
- [788. Rotated Digits](../0804-rotated-digits/)
- [1281. Subtract the Product and Sum of Digits of an Integer](../1406-subtract-the-product-and-sum-of-digits-of-an-integer/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/sequential-digits/)
