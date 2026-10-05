# LeetCode 3813: Vowel-Consonant Score

**LeetCode Problem #3813 — Vowel-Consonant Score**
Solve LeetCode Vowel-Consonant Score using PHP and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Vowel-Consonant Score |
| LeetCode | #3813 |
| Difficulty | Easy |
| Language | PHP |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given a   palindromic   string  s  and an integer  k .

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Iterative Traversal**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Vowel-Consonant Score**. Applying **Depth-First Search (DFS) / Breadth-First Search (BFS)** yields the target result step by step.

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
PHP

## Source Code
- [solution.php](./solution.php)

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
- [3812. Minimum Edge Toggles on a Tree](../3812-smallest-palindromic-rearrangement-i/)
- [3635. Earliest Finish Time for Land and Water Rides II](../3635-smallest-divisible-digit-product-ii/)
- [4037. Maximum Valid Split Positions II](../4037-lexicographically-smallest-palindromic-permutation-greater-than-target/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/smallest-palindromic-rearrangement-ii/)
