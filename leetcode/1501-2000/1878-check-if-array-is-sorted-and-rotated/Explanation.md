# LeetCode 1752: Check if Array Is Sorted and Rotated

**LeetCode Problem #1752 — Check if Array Is Sorted and Rotated**
Solve LeetCode Check if Array Is Sorted and Rotated using C++ and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Check if Array Is Sorted and Rotated |
| LeetCode | #1752 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given an array  nums , return  true   if the array was originally sorted in non-decreasing order, then rotated  some  number of positions (including zero) . Otherwise, return  false .

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
The code counts the number of "breaks" where `nums[i] > nums[(i+1) % n]`. A sorted-and-rotated array can have **at most one** such break (at the rotation point). If there are 0 or 1 breaks, return `true`; otherwise, `false`.

Time complexity is $O(N)$ and space complexity is $O(1)$.

## Algorithm
1. Initialize state variables / data structure (**Sorted Array**).
2. Process elements sequentially using **Modified Binary Search**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Check if Array Is Sorted and Rotated**. Applying **Modified Binary Search** yields the target result step by step.

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
C++

## Source Code
- [solution.cpp](./solution.cpp)

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
- [2267.  Check if There Is a Valid Parentheses String Path](../../2001-2500/2349-check-if-there-is-a-valid-parentheses-string-path/)
- [1250. Check If It Is a Good Array](../../1001-1500/1372-check-if-it-is-a-good-array/)
- [1961. Check If String Is a Prefix of Array](../../2001-2500/2093-check-if-string-is-a-prefix-of-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/)
