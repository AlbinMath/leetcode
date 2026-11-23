# LeetCode 1913: Maximum Product Difference Between Two Pairs

**LeetCode Problem #1913 — Maximum Product Difference Between Two Pairs**
Solve LeetCode Maximum Product Difference Between Two Pairs using C++ and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Product Difference Between Two Pairs |
| LeetCode | #1913 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
The  product difference  between two pairs  (a, b)  and  (c, d)  is defined as  (a * b) - (c * d) .

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Dictionary / Hash Map**).
2. Process elements sequentially using **Complement Lookup / Hash Table Frequency**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Maximum Product Difference Between Two Pairs**. Applying **Complement Lookup / Hash Table Frequency** yields the target result step by step.

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
- [1026. Maximum Difference Between Node and Ancestor](../../1001-1500/1092-maximum-difference-between-node-and-ancestor/)
- [1464. Maximum Product of Two Elements in an Array](../../1501-2000/1574-maximum-product-of-two-elements-in-an-array/)
- [1960. Maximum Product of the Length of Two Palindromic Substrings](../../1001-1500/1336-maximum-product-of-the-length-of-two-palindromic-substrings/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-product-difference-between-two-pairs/)
