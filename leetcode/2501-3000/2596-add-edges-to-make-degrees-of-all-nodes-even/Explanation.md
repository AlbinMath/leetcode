# LeetCode 2508: Add Edges to Make Degrees of All Nodes Even

**LeetCode Problem #2508 — Add Edges to Make Degrees of All Nodes Even**
Solve LeetCode Add Edges to Make Degrees of All Nodes Even using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Add Edges to Make Degrees of All Nodes Even |
| LeetCode | #2508 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
There is an  undirected  graph consisting of  n  nodes numbered from  1  to  n . You are given the integer  n  and a  2D  array  edges  where  edges[i] = [a i , b i ]  indicates that there is an edge between nodes  a i   and  b i  . The graph can be disconnected.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
We iterate through the input using **Pointer Traversal & Node Manipulation**. By maintaining state efficiently in a **Linked List**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Two Pointer Convergence & Scanning**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Add Edges to Make Degrees of All Nodes Even**. Applying **Two Pointer Convergence & Scanning** yields the target result step by step.

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
- [921. Minimum Add to Make Parentheses Valid](../../0501-1000/0957-minimum-add-to-make-parentheses-valid/)
- [847. Shortest Path Visiting All Nodes](../../0501-1000/0877-shortest-path-visiting-all-nodes/)
- [863. All Nodes Distance K in Binary Tree](../../0501-1000/0893-all-nodes-distance-k-in-binary-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/add-edges-to-make-degrees-of-all-nodes-even/)
