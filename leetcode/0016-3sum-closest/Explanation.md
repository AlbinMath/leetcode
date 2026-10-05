# LeetCode 16: 3Sum Closest

**LeetCode Problem #16 — 3Sum Closest**
Solve LeetCode 3Sum Closest using JavaScript and Binary Search. This solution finds the optimal result using Modified Binary Search in O(log n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | 3Sum Closest |
| LeetCode | #16 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(log n) |
| Space Complexity | O(1) |

## Problem
You are given an integer array  nums  of length  n  and an integer  target .

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
This solution uses **Sorting + Two Pointers**, very similar to the 3Sum problem, but instead of looking for an exact match, it tracks which sum is closest to the target.

1. **Sort the Array:** The array is sorted in ascending order to enable the two-pointer approach.
2. **Initialize Closest:** The variable `closest` is initialized to the sum of the first three elements as a starting reference.
3. **Fix One Element:** It iterates through the array with index `i`, fixing `nums[i]` as the first element.
4. **Two Pointers:** For each `i`, it sets `left = i + 1` and `right = nums.length - 1`.
   - It calculates `sum = nums[i] + nums[left] + nums[right]`.
   - If the absolute difference between `sum` and `target` is smaller than the current `closest`, it updates `closest = sum`.
   - If `sum < target`, it increments `left` to increase the sum.
   - If `sum > target`, it decrements `right` to decrease the sum.
   - If `sum === target`, it returns `sum` immediately (can't get any closer than an exact match).
5. After all iterations, it returns `closest`.

Time complexity is $O(N^2)$ and space complexity is $O(\log N)$ for sorting.

## Algorithm
1. Initialize state variables / data structure (**Sorted Array**).
2. Process elements sequentially using **Modified Binary Search**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **3Sum Closest**. Applying **Modified Binary Search** yields the target result step by step.

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
- [15. 3Sum](../0015-3sum/)
- [4. Median of Two Sorted Arrays](../0004-median-of-two-sorted-arrays/)
- [18. 4Sum](../0018-4sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/3sum-closest/)
