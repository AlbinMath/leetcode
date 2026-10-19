# LeetCode 3327: Check if DFS Strings Are Palindromes

**LeetCode Problem #3327 — Check if DFS Strings Are Palindromes**
Solve LeetCode Check if DFS Strings Are Palindromes using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Check if DFS Strings Are Palindromes |
| LeetCode | #3327 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given a tree rooted at node 0, consisting of  n  nodes numbered from  0  to  n - 1 . The tree is represented by an array  parent  of size  n , where  parent[i]  is the parent of node  i . Since node 0 is the root,  parent[0] == -1 .

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
We iterate through the input using **Two Pointer Convergence & Scanning**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Two Pointer Convergence & Scanning**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Check if DFS Strings Are Palindromes**. Applying **Two Pointer Convergence & Scanning** yields the target result step by step.

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
Python

## Source Code
- [solution.py](./solution.py)

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
- [1437. Check If All 1's Are at Least Length K Places Away](../1548-check-if-all-1s-are-at-least-length-k-places-away/)
- [1657. Determine if Two Strings Are Close](../1777-determine-if-two-strings-are-close/)
- [1662. Check If Two String Arrays are Equivalent](../1781-check-if-two-string-arrays-are-equivalent/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/check-if-dfs-strings-are-palindromes/)
