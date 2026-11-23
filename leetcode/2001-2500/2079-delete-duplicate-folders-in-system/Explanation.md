# LeetCode 1948: Delete Duplicate Folders in System

**LeetCode Problem #1948 — Delete Duplicate Folders in System**
Solve LeetCode Delete Duplicate Folders in System using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Delete Duplicate Folders in System |
| LeetCode | #1948 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Due to a bug, there are many duplicate folders in a file system. You are given a 2D array  paths , where  paths[i]  is an array representing an absolute path to the  i th   folder in the file system.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Two Pointer Convergence & Scanning**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Delete Duplicate Folders in System**. Applying **Two Pointer Convergence & Scanning** yields the target result step by step.

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
- [609. Find Duplicate File in System](../../0501-1000/0609-find-duplicate-file-in-system/)
- [196. Delete Duplicate Emails](../../0001-0500/0196-delete-duplicate-emails/)
- [1268. Search Suggestions System](../../1001-1500/1397-search-suggestions-system/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/delete-duplicate-folders-in-system/)
