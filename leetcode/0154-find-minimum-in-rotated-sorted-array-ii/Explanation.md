# Find Minimum In Rotated Sorted Array II

## Problem Explanation
This is the same as "Find Minimum in Rotated Sorted Array" but with **duplicates** allowed. Given a rotated sorted array `nums` that may contain duplicates, find the minimum element.

For example, `nums = [2,2,2,0,1]` → minimum is `0`.

## How the Code Works
The code uses **Binary Search** with an extra case to handle duplicates.

1. It maintains two pointers `left` and `right`.
2. In each iteration, it calculates `mid`.
3. **Three Cases:**
   - `nums[mid] < nums[right]`: The minimum is at `mid` or to the left → `right = mid`.
   - `nums[mid] > nums[right]`: The minimum is in the right half → `left = mid + 1`.
   - `nums[mid] == nums[right]`: **Duplicates make it impossible to determine which side the minimum is on.** The solution safely decrements `right--`. This only eliminates one duplicate and doesn't risk skipping the minimum.
4. When `left === right`, `nums[left]` is the minimum.

The worst-case time complexity is $O(N)$ (when all elements are duplicates), but the average case is $O(\log N)$. Space complexity is $O(1)$.
