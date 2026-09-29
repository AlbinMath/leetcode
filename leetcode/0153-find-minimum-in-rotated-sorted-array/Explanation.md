# Find Minimum In Rotated Sorted Array

## Problem Explanation
Suppose an array of length `n` sorted in ascending order is rotated between `1` and `n` times. Given the rotated array `nums` with **unique** elements, find the minimum element. The algorithm must run in $O(\log N)$ time.

For example, `nums = [3,4,5,1,2]` (originally `[1,2,3,4,5]`, rotated 3 times) → minimum is `1`.

## How the Code Works
The code uses **Binary Search** to find the minimum.

1. It maintains two pointers `left` and `right`.
2. In each iteration, it calculates `mid = left + (right - left) / 2`.
3. **Key Decision:**
   - If `nums[mid] > nums[right]`: The minimum must be in the right half (the rotation point is to the right of `mid`), so `left = mid + 1`.
   - Otherwise (`nums[mid] <= nums[right]`): The minimum is at `mid` or to the left, so `right = mid`.
4. When `left === right`, the minimum element has been found.

Time complexity is $O(\log N)$ and space complexity is $O(1)$.
