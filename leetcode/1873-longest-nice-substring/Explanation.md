# LeetCode 1763: Longest Nice Substring

**LeetCode Problem #1763 — Longest Nice Substring**
Solve LeetCode Longest Nice Substring using C++ and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest Nice Substring |
| LeetCode | #1763 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
A string  s  is  nice  if, for every letter of the alphabet that  s  contains, it appears  both  in uppercase and lowercase. For example,  "abABB"  is nice because  &#39;A&#39;  and  &#39;a&#39;  appear, and  &#39;B&#39;  and  &#39;b&#39;  appear. However,  "abA"  is not because  &#39;b&#39;  appears, but  &#39;B&#39;  does not.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Longest Nice Substring**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Array / General**

## Topics
- Array

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)

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
- [3. Longest Substring Without Repeating Characters](../0003-longest-substring-without-repeating-characters/)
- [5. Longest Palindromic Substring](../0005-longest-palindromic-substring/)
- [2213. Longest Substring of One Repeating Character](../2319-longest-substring-of-one-repeating-character/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longest-nice-substring/)
