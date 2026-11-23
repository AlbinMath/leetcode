# LeetCode 1967: Number of Strings That Appear as Substrings in Word

**LeetCode Problem #1967 — Number of Strings That Appear as Substrings in Word**
Solve LeetCode Number of Strings That Appear as Substrings in Word using Kotlin and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Strings That Appear as Substrings in Word |
| LeetCode | #1967 |
| Difficulty | Easy |
| Language | Kotlin |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given an array of strings  patterns  and a string  word , return  the  number  of strings in   patterns   that exist as a  substring  in   word .

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
The code iterates through each pattern and checks if it exists as a substring of `word` using the built-in `contains`/`indexOf` method. Count and return the matches.

Time complexity is $O(P \times W)$ where $P$ is total pattern length and $W$ is word length, and space complexity is $O(1)$.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Two Pointer Convergence & Scanning**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Number of Strings That Appear as Substrings in Word**. Applying **Two Pointer Convergence & Scanning** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

## Language
Kotlin

## Source Code
- [solution.kt](./solution.kt)

## Why This Works
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [1074. Number of Submatrices That Sum to Target](../../1001-1500/1145-number-of-submatrices-that-sum-to-target/)
- [1498. Number of Subsequences That Satisfy the Given Sum Condition](../../1501-2000/1621-number-of-subsequences-that-satisfy-the-given-sum-condition/)
- [1606. Find Servers That Handled Most Number of Requests](../../1501-2000/1710-find-servers-that-handled-most-number-of-requests/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/)
