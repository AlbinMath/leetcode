# LeetCode 1793: Maximum Score of a Good Subarray

**LeetCode Problem #1793 — Maximum Score of a Good Subarray**
Solve LeetCode Maximum Score of a Good Subarray using C++ and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Score of a Good Subarray |
| LeetCode | #1793 |
| Difficulty | Hard |
| Language | C++ |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given an integer array  nums  of  even  length  n  and an integer  limit . In one move, you can replace any integer from  nums  with another integer between  1  and  limit , inclusive.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
The code uses a **Difference Array** technique to efficiently calculate the cost for every possible target sum.

1. For each pair `(a, b)`, determine the ranges of target sums achievable with 0, 1, or 2 replacements.
2. Use a difference array to mark these ranges: target sum = `a+b` needs 0 moves, sums in `[min(a,b)+1, max(a,b)+limit]` need 1 move, all others need 2.
3. Sweep through the difference array to find the target sum with minimum total moves.

Time complexity is $O(N + \text{limit})$ and space complexity is $O(\text{limit})$.

## Algorithm
1. Initialize state variables / data structure (**Dictionary / Hash Map**).
2. Process elements sequentially using **Complement Lookup / Hash Table Frequency**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Maximum Score of a Good Subarray**. Applying **Complement Lookup / Hash Table Frequency** yields the target result step by step.

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
- [153. Find Minimum in Rotated Sorted Array](../0153-find-minimum-in-rotated-sorted-array/)
- [154. Find Minimum in Rotated Sorted Array II](../0154-find-minimum-in-rotated-sorted-array-ii/)
- [2212. Maximum Points in an Archery Competition](../2212-removing-minimum-and-maximum-from-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-moves-to-make-array-complementary/)
