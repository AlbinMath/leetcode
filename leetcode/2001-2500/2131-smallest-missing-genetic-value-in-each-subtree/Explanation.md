# LeetCode 2003: Smallest Missing Genetic Value in Each Subtree

**LeetCode Problem #2003 — Smallest Missing Genetic Value in Each Subtree**
Solve LeetCode Smallest Missing Genetic Value in Each Subtree using Python and Prefix Sum. This solution finds the optimal result using Prefix Sum Precomputation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Smallest Missing Genetic Value in Each Subtree |
| LeetCode | #2003 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Prefix Sum Precomputation |
| Data Structure | Prefix Array |
| Pattern | Prefix Sum |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
There is a  family tree  rooted at  0  consisting of  n  nodes numbered  0  to  n - 1 . You are given a  0-indexed  integer array  parents , where  parents[i]  is the parent for node  i . Since node  0  is the  root ,  parents[0] == -1 .

## Key Insight
Leverage **Prefix Sum** with **Prefix Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Depth-First Search (DFS) / Breadth-First Search (BFS)**. By maintaining state efficiently in a **Tree / Graph / Grid**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Prefix Array**).
2. Process elements sequentially using **Prefix Sum Precomputation**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Smallest Missing Genetic Value in Each Subtree**. Applying **Prefix Sum Precomputation** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

## Pattern
**Prefix Sum**

## Topics
- Prefix Sum
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)

## Why This Works
By utilizing **Prefix Sum**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [865. Smallest Subtree with all the Deepest Nodes](../../0501-1000/0896-smallest-subtree-with-all-the-deepest-nodes/)
- [1663. Smallest String With A Given Numeric Value](../../1501-2000/1782-smallest-string-with-a-given-numeric-value/)
- [2507. Smallest Value After Replacing With Sum of Prime Factors](../../2501-3000/2595-smallest-value-after-replacing-with-sum-of-prime-factors/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/smallest-missing-genetic-value-in-each-subtree/)
