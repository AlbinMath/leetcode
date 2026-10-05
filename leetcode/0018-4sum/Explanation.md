# LeetCode 18: 4Sum

**LeetCode Problem #18 — 4Sum**
Solve LeetCode 4Sum using C++ and Binary Search. This solution finds the optimal result using Modified Binary Search in O(log n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | 4Sum |
| LeetCode | #18 |
| Difficulty | Medium |
| Language | C++ |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(log n) |
| Space Complexity | O(1) |

## Problem
Given an array  nums  of  n  integers, return  an array of all the  unique  quadruplets   [nums[a], nums[b], nums[c], nums[d]]  such that:

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
The code extends the 3Sum approach by adding one more loop, using **Sorting + Two Nested Loops + Two Pointers** for an $O(N^3)$ solution.

1. **Sort the Array:** The array is sorted to enable the two-pointer technique and duplicate skipping.
2. **First Loop (`i`):** Fixes the first element. Skips duplicates by checking `nums[i] == nums[i - 1]`.
3. **Second Loop (`j`):** Fixes the second element starting from `i + 1`. Also skips duplicates.
4. **Two Pointers (`left`, `right`):** For each pair `(i, j)`, two pointers search for the remaining two elements.
   - The sum is computed using `long long` to avoid integer overflow.
   - If `sum == target`, the quadruplet is added and both pointers move inward, skipping duplicates.
   - If `sum < target`, `left` is incremented.
   - If `sum > target`, `right` is decremented.

The time complexity is $O(N^3)$ and space complexity is $O(\log N)$ for sorting.

## Algorithm
1. Initialize state variables / data structure (**Sorted Array**).
2. Process elements sequentially using **Modified Binary Search**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **4Sum**. Applying **Modified Binary Search** yields the target result step by step.

## Complexity
- **Time Complexity:** O(log n)
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
- [4. Median of Two Sorted Arrays](../0004-median-of-two-sorted-arrays/)
- [15. 3Sum](../0015-3sum/)
- [16. 3Sum Closest](../0016-3sum-closest/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/4sum/)
