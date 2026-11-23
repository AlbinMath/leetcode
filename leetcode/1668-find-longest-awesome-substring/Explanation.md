# LeetCode 1542: Find Longest Awesome Substring

**LeetCode Problem #1542 — Find Longest Awesome Substring**
Solve LeetCode Find Longest Awesome Substring using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Longest Awesome Substring |
| LeetCode | #1542 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given a string  s . An  awesome  substring is a non-empty substring of  s  such that we can make any number of swaps in order to make it a palindrome.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Find Longest Awesome Substring**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Array / General**

## Topics
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)

## Why This Works
By utilizing **Array / General**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1371. Find the Longest Substring Containing Vowels in Even Counts](../1473-find-the-longest-substring-containing-vowels-in-even-counts/)
- [2730. Find the Longest Semi-Repetitive Substring](../2786-find-the-longest-semi-repetitive-substring/)
- [2981. Find Longest Special Substring That Occurs Thrice I](../3267-find-longest-special-substring-that-occurs-thrice-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-longest-awesome-substring/)
