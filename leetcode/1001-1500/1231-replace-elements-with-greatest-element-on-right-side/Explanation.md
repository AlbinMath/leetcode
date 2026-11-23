# LeetCode 1299: Replace Elements with Greatest Element on Right Side

**LeetCode Problem #1299 — Replace Elements with Greatest Element on Right Side**
Solve LeetCode Replace Elements with Greatest Element on Right Side using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Replace Elements with Greatest Element on Right Side |
| LeetCode | #1299 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given an array  arr , replace every element in that array with the greatest element among the elements to its right, and replace the last element with  -1 .

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Two Pointer Convergence & Scanning**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Replace Elements with Greatest Element on Right Side**. Applying **Two Pointer Convergence & Scanning** yields the target result step by step.

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
- [199. Binary Tree Right Side View](../../0001-0500/0199-binary-tree-right-side-view/)
- [2295. Replace Elements in an Array](../../2001-2500/2388-replace-elements-in-an-array/)
- [116. Populating Next Right Pointers in Each Node](../../0001-0500/0116-populating-next-right-pointers-in-each-node/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/)
