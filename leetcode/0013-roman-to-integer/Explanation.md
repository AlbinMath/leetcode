# LeetCode 13: Roman to Integer

**LeetCode Problem #13 — Roman to Integer**
Solve LeetCode Roman to Integer using Python and Database / SQL. This solution finds the optimal result using SQL Query / Relational Join & Grouping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Roman to Integer |
| LeetCode | #13 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | SQL Query / Relational Join & Grouping |
| Data Structure | Relational Table |
| Pattern | Database / SQL |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Roman numerals are represented by seven different symbols:  I ,  V ,  X ,  L ,  C ,  D  and  M .

## Key Insight
Leverage **Database / SQL** with **Relational Table** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We define a dictionary `values` that maps each Roman numeral character to its corresponding integer value.
We initialize a `total` variable to `0`.
We iterate through the string `s`. For each character at index `i`:
- If there is a next character (`i + 1 < len(s)`) and its value is strictly greater than the current character's value, it represents a subtractive combination (like `IV` or `IX`). We subtract the current character's value from `total`.
- Otherwise, we add the current character's value to `total`.

## Algorithm
1. Initialize state variables / data structure (**Relational Table**).
2. Process elements sequentially using **SQL Query / Relational Join & Grouping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Roman to Integer**. Applying **SQL Query / Relational Join & Grouping** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

## Pattern
**Database / SQL**

## Topics
- Database
- SQL
- Data Aggregation

## Language
Python

## Source Code
- [solution.py](./solution.py)

## Why This Works
By utilizing **Database / SQL**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

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
- [3236. CEO Subordinate Hierarchy](../3236-smallest-missing-integer-greater-than-sequential-prefix-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/roman-to-integer/)
