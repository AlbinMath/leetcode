# 4Sum

## Problem Explanation
Given an array `nums` of `n` integers and an integer `target`, return an array of all unique quadruplets `[nums[a], nums[b], nums[c], nums[d]]` such that `a`, `b`, `c`, and `d` are distinct indices and `nums[a] + nums[b] + nums[c] + nums[d] == target`.

For example, if `nums = [1, 0, -1, 0, -2, 2]` and `target = 0`:
- The output is `[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]`.

## How the Code Works
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
