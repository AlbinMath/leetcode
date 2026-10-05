# LeetCode 10: Regular Expression Matching

**LeetCode Problem #10 — Regular Expression Matching**
Solve LeetCode Regular Expression Matching using JavaScript and Database / SQL. This solution finds the optimal result using SQL Query / Relational Join & Grouping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Regular Expression Matching |
| LeetCode | #10 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | SQL Query / Relational Join & Grouping |
| Data Structure | Relational Table |
| Pattern | Database / SQL |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Given an input string  s  and a pattern  p , implement regular expression matching with support for  &#39;.&#39;  and  &#39;*&#39;  where:

## Key Insight
Leverage **Database / SQL** with **Relational Table** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
This solution uses **Top-Down Dynamic Programming (Memoization)** to check all possible valid matches efficiently.

1. **State:** The recursive function `dp(i, j)` determines if the substring `s[i:]` matches the pattern `p[j:]`.
2. **Memoization:** It uses a `Map` (`memo`) to store the results of `(i, j)` to avoid redundant calculations.
3. **Base Case:** If the pattern is fully consumed (`j === p.length`), the string must also be fully consumed (`i === s.length`) for a valid match.
4. **First Match:** It checks if the current characters match: `s[i] === p[j]` or if `p[j] === '.'` (which matches any character).
5. **Handling '*':**
   - If the *next* character in the pattern is `'*'`, there are two choices:
     1. **Ignore the '*' and the preceding element:** Advance the pattern by 2 characters (`dp(i, j + 2)`). This simulates the `'*'` matching *zero* occurrences.
     2. **Consume a character from `s`:** If `firstMatch` is true, we can consume one character from `s` and keep the pattern at `j` (`dp(i + 1, j)`). This simulates the `'*'` matching *one or more* occurrences.
6. **Handling Normal Characters:** If there's no `'*'`, it simply requires `firstMatch` to be true and recursively calls `dp(i + 1, j + 1)`.

By memoizing the states, the time complexity is reduced to $O(S \times P)$ where $S$ and $P$ are the lengths of the string and pattern respectively.

## Algorithm
1. Initialize state variables / data structure (**Relational Table**).
2. Process elements sequentially using **SQL Query / Relational Join & Grouping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Regular Expression Matching**. Applying **SQL Query / Relational Join & Grouping** yields the target result step by step.

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
JavaScript

## Source Code
- [solution.js](./solution.js)

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
- [13. Roman to Integer](../0013-roman-to-integer/)
- [17. Letter Combinations of a Phone Number](../0017-letter-combinations-of-a-phone-number/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/regular-expression-matching/)
