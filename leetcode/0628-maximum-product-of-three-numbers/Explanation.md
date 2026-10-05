# LeetCode 628: Maximum Product of Three Numbers

**LeetCode Problem #628 — Maximum Product of Three Numbers**
Solve LeetCode Maximum Product of Three Numbers using Elixir and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Product of Three Numbers |
| LeetCode | #628 |
| Difficulty | Easy |
| Language | Elixir |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given an integer array  nums .

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
The code uses **sorting** and considers two possible candidates for the maximum product:

1. **Sort the Array:** Sort `nums` in ascending order.
2. **Two Candidates:**
   - `a * b * c` — the product of the three largest numbers (last three elements in the sorted array).
   - `a * x * y` — the product of the largest number and the two smallest numbers (first two elements). This handles the case where two large negative numbers multiply to give a large positive result.
3. Return the maximum of these two candidates.

Time complexity is $O(N \log N)$ for sorting and space complexity is $O(\log N)$.

## Algorithm
1. Initialize state variables / data structure (**Sorted Array**).
2. Process elements sequentially using **Modified Binary Search**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Maximum Product of Three Numbers**. Applying **Modified Binary Search** yields the target result step by step.

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
Elixir

## Source Code
- [solution.ex](./solution.ex)

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
- [1574. Shortest Subarray to be Removed to Make Array Sorted](../1574-maximum-product-of-two-elements-in-an-array/)
- [3859. Count Subarrays With K Distinct Integers](../3859-maximum-product-of-two-digits/)
- [2. Add Two Numbers](../0002-add-two-numbers/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-product-of-three-numbers/)
