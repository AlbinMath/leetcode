# LeetCode 3090: Maximum Length Substring With Two Occurrences

**LeetCode Problem #3090 — Maximum Length Substring With Two Occurrences**
Solve LeetCode Maximum Length Substring With Two Occurrences using Swift and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Length Substring With Two Occurrences |
| LeetCode | #3090 |
| Difficulty | Easy |
| Language | Swift |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given a string  s , return the  maximum  length of a  substring  such that it contains  at most two occurrences  of each character.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Iterative Traversal**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Maximum Length Substring With Two Occurrences**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Array / General**

## Topics
- Array

## Language
Swift

## Source Code
- [solution.swift](./solution.swift)

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
- [1111. Maximum Nesting Depth of Two Valid Parentheses Strings](../1208-maximum-nesting-depth-of-two-valid-parentheses-strings/)
- [1464. Maximum Product of Two Elements in an Array](../1574-maximum-product-of-two-elements-in-an-array/)
- [1624. Largest Substring Between Two Equal Characters](../1746-largest-substring-between-two-equal-characters/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/)
