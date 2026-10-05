# LeetCode 15: 3Sum

**LeetCode Problem #15 — 3Sum**
Solve LeetCode 3Sum using JavaScript and Binary Search. This solution finds the optimal result using Modified Binary Search in O(log n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | 3Sum |
| LeetCode | #15 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(log n) |
| Space Complexity | O(1) |

## Problem
Given an integer array nums, return all the triplets  [nums[i], nums[j], nums[k]]  such that  i != j ,  i != k , and  j != k , and  nums[i] + nums[j] + nums[k] == 0 .

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
The code uses **Sorting + Two Pointers** to efficiently find all unique triplets in $O(N^2)$ time.

1. **Sort the Array:** Sorting enables the two-pointer technique and makes it easy to skip duplicate values.
2. **Fix One Element:** It iterates through the array with index `i`, fixing `nums[i]` as the first element of the triplet.
   - If `nums[i] > 0`, the loop breaks early because three positive numbers can never sum to zero.
   - If `nums[i]` equals the previous element (`nums[i - 1]`), it skips to avoid duplicate triplets.
3. **Two Pointers for the Remaining Two:** For each fixed `nums[i]`, it uses two pointers: `left = i + 1` and `right = nums.length - 1`.
   - It calculates `sum = nums[i] + nums[left] + nums[right]`.
   - If `sum === 0`, the triplet is added to the result. Then both pointers are moved inward, skipping over any duplicate values.
   - If `sum < 0`, `left` is incremented to increase the sum.
   - If `sum > 0`, `right` is decremented to decrease the sum.
4. The result contains all unique triplets.

Time complexity is $O(N^2)$ and space complexity is $O(\log N)$ for sorting (ignoring output).

## Algorithm
1. Initialize state variables / data structure (**Sorted Array**).
2. Process elements sequentially using **Modified Binary Search**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **3Sum**. Applying **Modified Binary Search** yields the target result step by step.

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
- [16. 3Sum Closest](../0016-3sum-closest/)
- [4. Median of Two Sorted Arrays](../0004-median-of-two-sorted-arrays/)
- [18. 4Sum](../0018-4sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/3sum/)
