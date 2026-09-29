# 3Sum Closest

## Problem Explanation
Given an integer array `nums` of length `n` and an integer `target`, find three integers in `nums` such that the sum is **closest** to `target`. Return the sum of the three integers. You may assume that each input has exactly one solution.

For example, if `nums = [-1, 2, 1, -4]` and `target = 1`:
- The sum that is closest to the target is `2` (i.e., `-1 + 2 + 1 = 2`).

## How the Code Works
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
