# LeetCode 195: Tenth Line

**LeetCode Problem #195 — Tenth Line**
Solve LeetCode Tenth Line using Shell and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Tenth Line |
| LeetCode | #195 |
| Difficulty | Easy |
| Language | Shell |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a text file `file.txt`, print just the 10th line of the file.

## Examples
Consider the standard input for **Tenth Line**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The solution uses `sed -n '10p'`:
- `sed` is a stream editor that processes text line by line.
- `-n` suppresses the default output (which would print every line).
- `'10p'` tells `sed` to **p**rint only line number 10.

This is a concise and efficient one-liner.

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
# Read from the file file.txt and output the tenth line to stdout.
sed -n '10p' file.txt
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
- [149. Max Points on a Line](../../0001-0500/0149-max-points-on-a-line/)
- [1232. Check If It Is a Straight Line](../../1001-1500/1232-check-if-it-is-a-straight-line/)
- [1621. Number of Sets of K Non-Overlapping Line Segments](../../1501-2000/1621-number-of-sets-of-k-non-overlapping-line-segments/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/tenth-line/)
