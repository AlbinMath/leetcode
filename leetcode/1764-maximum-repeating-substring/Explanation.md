# LeetCode 1668: Maximum Repeating Substring

**LeetCode Problem #1668 — Maximum Repeating Substring**
Solve LeetCode Maximum Repeating Substring using C++ and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Repeating Substring |
| LeetCode | #1668 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
For a string  sequence , a string  word  is   k -repeating  if  word  concatenated  k  times is a substring of  sequence . The  word &#39;s  maximum  k -repeating value  is the highest value  k  where  word  is  k -repeating in  sequence . If  word  is not a substring of  sequence ,  word &#39;s maximum  k -repeating value is  0 .

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Maximum Repeating Substring**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [2213. Longest Substring of One Repeating Character](../2319-longest-substring-of-one-repeating-character/)
- [3090. Maximum Length Substring With Two Occurrences](../3349-maximum-length-substring-with-two-occurrences/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-repeating-substring/)
