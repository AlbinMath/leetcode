# LeetCode 2265: Count Nodes Equal to Average of Subtree

**LeetCode Problem #2265 — Count Nodes Equal to Average of Subtree**
Solve LeetCode Count Nodes Equal to Average of Subtree using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Nodes Equal to Average of Subtree |
| LeetCode | #2265 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given the  root  of a binary tree, return  the number of nodes where the value of the node is equal to the  average  of the values in its  subtree  .

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
Use **DFS** (post-order traversal). Each recursive call returns the `(sum, count)` of the subtree. At each node, compute `average = sum / count` and check if it equals the node's value.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Two Pointer Convergence & Scanning**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Count Nodes Equal to Average of Subtree**. Applying **Two Pointer Convergence & Scanning** yields the target result step by step.

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
JavaScript

## Source Code
- [solution.js](./solution.js)

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
- [1251. Average Selling Price](../1390-average-selling-price/)
- [1661. Average Time of Process per Machine](../1801-average-time-of-process-per-machine/)
- [1729. Find Followers Count](../1877-find-followers-count/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/)
