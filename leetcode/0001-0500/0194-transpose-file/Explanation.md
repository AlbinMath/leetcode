# LeetCode 194: Transpose File

**LeetCode Problem #194 — Transpose File**
Solve LeetCode Transpose File using Shell and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Transpose File |
| LeetCode | #194 |
| Difficulty | Medium |
| Language | Shell |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a text file `file.txt`, transpose its content.

You may assume that each row has the same number of columns, and each field is separated by the `' '` character.

## Examples
Consider the standard input for **Transpose File**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The solution uses a single `awk` command:
1. `for(i=1;i<=NF;i++) a[i]=a[i]" "$i`: For each line, it iterates through all fields (words). It appends the `i`th field of the current line to an accumulator string `a[i]`. This effectively groups all values from column `i` together.
2. `END{for(i=1;i<=NF;i++) print substr(a[i],2)}`: After processing all lines, it prints each accumulated string. `substr(a[i], 2)` removes the leading space that was prepended during concatenation.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
Applying **In-Place Array Traversal & Index Mapping** step by step to the input yields the expected result.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
Shell

## Source Code
- [solution.sh](./solution.sh)


```bash
# Read from the file file.txt and print its transposed content to stdout.
awk '{for(i=1;i<=NF;i++)a[i]=a[i]" "$i}END{for(i=1;i<=NF;i++)print substr(a[i],2)}' file.txt
```

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
- [867. Transpose Matrix](../../0501-1000/0898-transpose-matrix/)
- [388. Longest Absolute File Path](../../0001-0500/0388-longest-absolute-file-path/)
- [609. Find Duplicate File in System](../../0501-1000/0609-find-duplicate-file-in-system/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/transpose-file/)
