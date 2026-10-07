# LeetCode 13: Roman to Integer

**LeetCode Problem #13 — Roman to Integer**
Solve LeetCode Roman to Integer using Python and Prefix Sum. This solution finds the optimal result using Prefix Sum Precomputation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Roman to Integer |
| LeetCode | #13 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Prefix Sum Precomputation |
| Data Structure | Prefix Array |
| Pattern | Prefix Sum |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Roman numerals are represented by seven different symbols:  I ,  V ,  X ,  L ,  C ,  D  and  M .

## Key Insight
Leverage **Prefix Sum** with **Prefix Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We define a dictionary `values` that maps each Roman numeral character to its corresponding integer value.
We initialize a `total` variable to `0`.
We iterate through the string `s`. For each character at index `i`:
- If there is a next character (`i + 1 < len(s)`) and its value is strictly greater than the current character's value, it represents a subtractive combination (like `IV` or `IX`). We subtract the current character's value from `total`.
- Otherwise, we add the current character's value to `total`.

## Algorithm
1. Initialize state variables / data structure (**Prefix Array**).
2. Process elements sequentially using **Prefix Sum Precomputation**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Roman to Integer**. Applying **Prefix Sum Precomputation** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

## Pattern
**Prefix Sum**

## Topics
- Prefix Sum
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)

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
- [12. Integer to Roman](../0012-integer-to-roman/)
- [7. Reverse Integer](../0007-reverse-integer/)
- [8. String to Integer (atoi)](../0008-string-to-integer-atoi/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/roman-to-integer/)
