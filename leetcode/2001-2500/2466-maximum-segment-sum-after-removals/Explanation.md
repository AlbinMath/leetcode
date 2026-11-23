# LeetCode 2382: Maximum Segment Sum After Removals

**LeetCode Problem #2382 — Maximum Segment Sum After Removals**
Solve LeetCode Maximum Segment Sum After Removals using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Segment Sum After Removals |
| LeetCode | #2382 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given two  0-indexed  integer arrays  nums  and  removeQueries , both of length  n . For the  i th   query, the element in  nums  at the index  removeQueries[i]  is removed, splitting  nums  into different segments.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Maximum Segment Sum After Removals**. Applying **Depth-First Search (DFS) / Breadth-First Search (BFS)** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

## Pattern
**Tree & Graph**

## Topics
- Tree
- Graph
- DFS
- BFS

## Language
Python

## Source Code
- [solution.py](./solution.py)

## Why This Works
By utilizing **Tree & Graph**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [3962. Maximum Subarray Sum After at Most K Swaps](../../4001-4500/4246-maximum-subarray-sum-after-at-most-k-swaps/)
- [2322. Minimum Score After Removals on a Tree](../../2001-2500/2400-minimum-score-after-removals-on-a-tree/)
- [3561. Resulting String After Adjacent Removals](../../3501-4000/3860-resulting-string-after-adjacent-removals/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-segment-sum-after-removals/)
