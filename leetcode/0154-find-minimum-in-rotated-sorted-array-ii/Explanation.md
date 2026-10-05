# LeetCode 154: Find Minimum in Rotated Sorted Array II

**LeetCode Problem #154 — Find Minimum in Rotated Sorted Array II**
Solve LeetCode Find Minimum in Rotated Sorted Array II using C++ and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Minimum in Rotated Sorted Array II |
| LeetCode | #154 |
| Difficulty | Hard |
| Language | C++ |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Suppose an array of length  n  sorted in ascending order is  rotated  between  1  and  n  times. For example, the array  nums = [0,1,4,4,5,6,7]  might become:

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
The code uses **Binary Search** with an extra case to handle duplicates.

1. It maintains two pointers `left` and `right`.
2. In each iteration, it calculates `mid`.
3. **Three Cases:**
   - `nums[mid] < nums[right]`: The minimum is at `mid` or to the left → `right = mid`.
   - `nums[mid] > nums[right]`: The minimum is in the right half → `left = mid + 1`.
   - `nums[mid] == nums[right]`: **Duplicates make it impossible to determine which side the minimum is on.** The solution safely decrements `right--`. This only eliminates one duplicate and doesn't risk skipping the minimum.
4. When `left === right`, `nums[left]` is the minimum.

The worst-case time complexity is $O(N)$ (when all elements are duplicates), but the average case is $O(\log N)$. Space complexity is $O(1)$.

## Algorithm
1. Initialize state variables / data structure (**Sorted Array**).
2. Process elements sequentially using **Modified Binary Search**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Find Minimum in Rotated Sorted Array II**. Applying **Modified Binary Search** yields the target result step by step.

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
- [153. Find Minimum in Rotated Sorted Array](../0153-find-minimum-in-rotated-sorted-array/)
- [33. Search in Rotated Sorted Array](../0033-search-in-rotated-sorted-array/)
- [1752. Check if Array Is Sorted and Rotated](../1878-check-if-array-is-sorted-and-rotated/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/)
