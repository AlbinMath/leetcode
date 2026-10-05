# LeetCode 1807: Evaluate the Bracket Pairs of a String

**LeetCode Problem #1807 — Evaluate the Bracket Pairs of a String**
Solve LeetCode Evaluate the Bracket Pairs of a String using C++ and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Evaluate the Bracket Pairs of a String |
| LeetCode | #1807 |
| Difficulty | Medium |
| Language | C++ |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given a string  s  that contains some bracket pairs, with each pair containing a  non-empty  key.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
1. **Map:** Store all key-value pairs in a hash map.
2. **Parse:** Iterate through the string. When encountering `(`, find the matching `)`, extract the key, look it up in the map, and append the value (or `?`) to the result.
3. Regular characters are appended directly.

Time complexity is $O(N + K)$ where $N$ is string length and $K$ is total key-value data, and space complexity is $O(N + K)$.

## Algorithm
1. Initialize state variables / data structure (**Dictionary / Hash Map**).
2. Process elements sequentially using **Complement Lookup / Hash Table Frequency**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Evaluate the Bracket Pairs of a String**. Applying **Complement Lookup / Hash Table Frequency** yields the target result step by step.

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
C++

## Source Code
- [solution.cpp](./solution.cpp)

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
- [150. Evaluate Reverse Polish Notation](../0150-evaluate-reverse-polish-notation/)
- [796. Rotate String](../0812-rotate-string/)
- [2267.  Check if There Is a Valid Parentheses String Path](../2349-check-if-there-is-a-valid-parentheses-string-path/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/)
