# LeetCode 2306: Naming a Company

**LeetCode Problem #2306 — Naming a Company**
Solve LeetCode Naming a Company using Java and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Naming a Company |
| LeetCode | #2306 |
| Difficulty | Hard |
| Language | Java |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given a 2D integer array  descriptions  where  descriptions[i] = [parent i , child i , isLeft i ]  indicates that  parent i   is the  parent  of  child i   in a  binary  tree of  unique  values. Furthermore,

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
1. Create all nodes in a hash map (value → TreeNode).
2. Process each description: link parent to child as left or right child. Track which nodes are children.
3. The root is the only node that never appears as a child.

## Algorithm
1. Initialize state variables / data structure (**Dictionary / Hash Map**).
2. Process elements sequentially using **Complement Lookup / Hash Table Frequency**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Naming a Company**. Applying **Complement Lookup / Hash Table Frequency** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

## Pattern
**Hash Map**

## Topics
- Hash Table
- Array
- Complement Lookup

## Language
Java

## Source Code
- [solution.java](./solution.java)

## Why This Works
By utilizing **Hash Map**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Using the same element twice.
2. Checking the map before inserting elements in the correct order.
3. Inefficient hash functions or unnecessary duplicate key updates.

## Interview Notes
- **Tests:** Hash map usage, complement/frequency lookup, and $O(n)$ time optimization.
- **Follow-up:** Can you solve the problem in $O(1)$ extra space if the input array is sorted?

## Related Problems
- [19. Remove Nth Node From End of List](../0019-remove-nth-node-from-end-of-list/)
- [608. Tree Node](../0608-tree-node/)
- [2212. Maximum Points in an Archery Competition](../2212-removing-minimum-and-maximum-from-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/create-binary-tree-from-descriptions/)
