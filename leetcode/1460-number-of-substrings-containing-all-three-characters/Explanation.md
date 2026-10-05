# LeetCode 1460: Make Two Arrays Equal by Reversing Subarrays

**LeetCode Problem #1460 — Make Two Arrays Equal by Reversing Subarrays**
Solve LeetCode Make Two Arrays Equal by Reversing Subarrays using Java and Database / SQL. This solution finds the optimal result using SQL Query / Relational Join & Grouping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Make Two Arrays Equal by Reversing Subarrays |
| LeetCode | #1460 |
| Difficulty | Easy |
| Language | Java |
| Algorithm | SQL Query / Relational Join & Grouping |
| Data Structure | Relational Table |
| Pattern | Database / SQL |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Given a string  s  consisting only of characters  a ,  b  and  c .

## Key Insight
Leverage **Database / SQL** with **Relational Table** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code uses a clever **counting approach** based on tracking the last occurrence of each character.

1. **Last Array:** `last[0]`, `last[1]`, `last[2]` store the most recent index where `a`, `b`, `c` appeared, initialized to `-1`.
2. For each index `right`, update `last[s[right] - 'a'] = right`.
3. If all three characters have appeared (`last[0] != -1 && last[1] != -1 && last[2] != -1`):
   - Find `minLast` = the earliest of the three last positions. Any substring starting from index `0` through `minLast` (inclusive) and ending at `right` will contain all three characters.
   - Add `minLast + 1` to the answer.

Time complexity is $O(N)$ and space complexity is $O(1)$.

## Algorithm
1. Initialize state variables / data structure (**Relational Table**).
2. Process elements sequentially using **SQL Query / Relational Join & Grouping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Make Two Arrays Equal by Reversing Subarrays**. Applying **SQL Query / Relational Join & Grouping** yields the target result step by step.

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
Java

## Source Code
- [solution.java](./solution.java)

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
- [1644. Lowest Common Ancestor of a Binary Tree II](../1644-maximum-number-of-non-overlapping-substrings/)
- [2099. Find Subsequence of Length K With the Largest Sum](../2099-number-of-strings-that-appear-as-substrings-in-word/)
- [2559. Count Vowel Strings in Ranges](../2559-maximum-number-of-non-overlapping-palindrome-substrings/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/)
