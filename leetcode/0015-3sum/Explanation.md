# 3Sum

## Problem Explanation
Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`. The solution set must not contain duplicate triplets.

For example, if `nums = [-1, 0, 1, 2, -1, -4]`:
- The distinct triplets that sum to zero are: `[-1, -1, 2]` and `[-1, 0, 1]`.

## How the Code Works
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
