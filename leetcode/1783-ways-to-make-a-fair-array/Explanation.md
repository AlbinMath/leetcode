# LeetCode 1664: Ways to Make a Fair Array

**LeetCode Problem #1664 — Ways to Make a Fair Array**
Solve LeetCode Ways to Make a Fair Array using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Ways to Make a Fair Array |
| LeetCode | #1664 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given an integer array  nums . You can choose  exactly one  index ( 0-indexed ) and remove the element. Notice that the index of the elements may change after the removal.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Ways to Make a Fair Array**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [1674. Minimum Moves to Make Array Complementary](../1793-minimum-moves-to-make-array-complementary/)
- [1827. Minimum Operations to Make the Array Increasing](../1938-minimum-operations-to-make-the-array-increasing/)
- [1887. Reduction Operations to Make the Array Elements Equal](../2016-reduction-operations-to-make-the-array-elements-equal/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/ways-to-make-a-fair-array/)
