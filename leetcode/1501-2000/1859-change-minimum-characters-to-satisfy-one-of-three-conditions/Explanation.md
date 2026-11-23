# LeetCode 1737: Change Minimum Characters to Satisfy One of Three Conditions

**LeetCode Problem #1737 — Change Minimum Characters to Satisfy One of Three Conditions**
Solve LeetCode Change Minimum Characters to Satisfy One of Three Conditions using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Change Minimum Characters to Satisfy One of Three Conditions |
| LeetCode | #1737 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given two strings  a  and  b  that consist of lowercase letters. In one operation, you can change any character in  a  or  b  to  any lowercase letter .

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Integer Bitmask**).
2. Process elements sequentially using **Bitwise Masking & Bit Shift**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Change Minimum Characters to Satisfy One of Three Conditions**. Applying **Bitwise Masking & Bit Shift** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Bit Manipulation**

## Topics
- Bit Manipulation
- Bitwise Math

## Language
Python

## Source Code
- [solution.py](./solution.py)

## Why This Works
By utilizing **Bit Manipulation**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1358. Number of Substrings Containing All Three Characters](../../1001-1500/1460-number-of-substrings-containing-all-three-characters/)
- [1876. Substrings of Size Three with Distinct Characters](../../1501-2000/1987-substrings-of-size-three-with-distinct-characters/)
- [3784. Minimum Deletion Cost to Make All Characters Equal](../../4001-4500/4138-minimum-deletion-cost-to-make-all-characters-equal/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/change-minimum-characters-to-satisfy-one-of-three-conditions/)
