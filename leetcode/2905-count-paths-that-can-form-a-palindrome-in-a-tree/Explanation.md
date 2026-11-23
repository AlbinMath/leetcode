# LeetCode 2791: Count Paths That Can Form a Palindrome in a Tree

**LeetCode Problem #2791 — Count Paths That Can Form a Palindrome in a Tree**
Solve LeetCode Count Paths That Can Form a Palindrome in a Tree using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Paths That Can Form a Palindrome in a Tree |
| LeetCode | #2791 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given a  tree  (i.e. a connected, undirected graph that has no cycles)  rooted  at node  0  consisting of  n  nodes numbered from  0  to  n - 1 . The tree is represented by a  0-indexed  array  parent  of size  n , where  parent[i]  is the parent of node  i . Since node  0  is the root,  parent[0] == -1 .

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
We iterate through the input using **Two Pointer Convergence & Scanning**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Two Pointer Convergence & Scanning**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Count Paths That Can Form a Palindrome in a Tree**. Applying **Two Pointer Convergence & Scanning** yields the target result step by step.

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
- [1442. Count Triplets That Can Form Two Arrays of Equal XOR](../1553-count-triplets-that-can-form-two-arrays-of-equal-xor/)
- [2201. Count Artifacts That Can Be Extracted](../1312-count-artifacts-that-can-be-extracted/)
- [2867. Count Valid Paths in a Tree](../3112-count-valid-paths-in-a-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-paths-that-can-form-a-palindrome-in-a-tree/)
