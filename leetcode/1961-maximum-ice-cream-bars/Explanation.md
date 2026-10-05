# LeetCode 1961: Check If String Is a Prefix of Array

**LeetCode Problem #1961 — Check If String Is a Prefix of Array**
Solve LeetCode Check If String Is a Prefix of Array using Java and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Check If String Is a Prefix of Array |
| LeetCode | #1961 |
| Difficulty | Easy |
| Language | Java |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
It is a sweltering summer day, and a boy wants to buy some ice cream bars.

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
1. **Sort** the costs in ascending order.
2. **Greedy:** Buy the cheapest bars first. Iterate through sorted costs, subtracting each cost from coins. Stop when you can't afford the next bar.
3. Return the count.

Time complexity is $O(N \log N)$ and space complexity is $O(\log N)$.

## Algorithm
1. Initialize state variables / data structure (**Sorted Array**).
2. Process elements sequentially using **Modified Binary Search**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Check If String Is a Prefix of Array**. Applying **Modified Binary Search** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Binary Search**

## Topics
- Binary Search
- Divide and Conquer
- Search Space

## Language
Java

## Source Code
- [solution.java](./solution.java)

## Why This Works
By utilizing **Binary Search**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Applying standard binary search without accounting for array rotation or duplicates.
2. Off-by-one errors when updating boundary pointers (`left = mid + 1` vs `right = mid - 1`).
3. Integer overflow during midpoint calculation (use `mid = left + (right - left) // 2`).

## Interview Notes
- **Tests:** Logarithmic search space reduction, boundary handling, and invariant preservation.
- **Follow-up:** How does performance change if the array contains duplicate elements?

## Related Problems
- [628. Maximum Product of Three Numbers](../0628-maximum-product-of-three-numbers/)
- [1208. Get Equal Substrings Within Budget](../1208-maximum-nesting-depth-of-two-valid-parentheses-strings/)
- [1297. Maximum Number of Occurrences of a Substring](../1297-maximum-number-of-balloons/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-ice-cream-bars/)
