# LeetCode 194: Transpose File

**LeetCode Problem #194 — Transpose File**
Solve LeetCode Transpose File using Shell and Array / General. This solution finds the optimal result using Iterative Traversal in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Transpose File |
| LeetCode | #194 |
| Difficulty | Medium |
| Language | Shell |
| Algorithm | Iterative Traversal |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given a text file  file.txt , transpose its content.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The solution uses a single `awk` command:
1. `for(i=1;i<=NF;i++) a[i]=a[i]" "$i`: For each line, it iterates through all fields (words). It appends the `i`th field of the current line to an accumulator string `a[i]`. This effectively groups all values from column `i` together.
2. `END{for(i=1;i<=NF;i++) print substr(a[i],2)}`: After processing all lines, it prints each accumulated string. `substr(a[i], 2)` removes the leading space that was prepended during concatenation.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Iterative Traversal**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Transpose File**. Applying **Iterative Traversal** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Array / General**

## Topics
- Array

## Language
Shell

## Source Code
- [solution.sh](./solution.sh)

## Why This Works
By utilizing **Array / General**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [5. Longest Palindromic Substring](../0005-longest-palindromic-substring/)
- [6. Zigzag Conversion](../0006-zigzag-conversion/)
- [14. Longest Common Prefix](../0014-longest-common-prefix/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/transpose-file/)
