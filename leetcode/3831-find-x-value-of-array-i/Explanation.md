# LeetCode 3524: Find X Value of Array I

**LeetCode Problem #3524 — Find X Value of Array I**
Solve LeetCode Find X Value of Array I using JavaScript and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find X Value of Array I |
| LeetCode | #3524 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given an array of  positive  integers  nums , and a  positive  integer  k .

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
The code uses **Dynamic Programming** to count the products of all possible contiguous subarrays efficiently.
1. It initializes an array `result` of size `k` to store the final counts for each remainder.
2. It uses a `dp` array (size `k`), where `dp[r]` keeps track of how many subarrays ending at the *previous* element have a product whose remainder modulo `k` is `r`.
3. It iterates through each `num` in `nums`:
   - It calculates the remainder `x` of the current number itself (`num % k`).
   - It creates a `next` array to represent subarrays ending at the *current* position.
   - It counts the subarray that consists *only* of the current element: `next[x]++`.
   - It extends all previous subarrays: for every remainder `r` in `dp`, the new remainder if the current number is appended is `(r * x) % k`. It adds the count `dp[r]` to `next[newRemainder]`.
   - After computing all subarrays ending at the current position (`next`), it adds these counts to the overall `result` array.
   - Finally, it updates `dp = next` for the next iteration.
4. It returns the `result` array containing the aggregated counts.

## Algorithm
1. Initialize state variables / data structure (**Sorted Array**).
2. Process elements sequentially using **Modified Binary Search**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Find X Value of Array I**. Applying **Modified Binary Search** yields the target result step by step.

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
JavaScript

## Source Code
- [solution.js](./solution.js)

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
- [3525. Find X Value of Array II](../3840-find-x-value-of-array-ii/)
- [153. Find Minimum in Rotated Sorted Array](../0153-find-minimum-in-rotated-sorted-array/)
- [154. Find Minimum in Rotated Sorted Array II](../0154-find-minimum-in-rotated-sorted-array-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-x-value-of-array-i/)
