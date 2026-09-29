# Check If Array Is Sorted And Rotated

## Problem Explanation
Given an array `nums`, return `true` if it was originally sorted in non-decreasing order and then rotated some number of positions (including zero).

## How the Code Works
The code counts the number of "breaks" where `nums[i] > nums[(i+1) % n]`. A sorted-and-rotated array can have **at most one** such break (at the rotation point). If there are 0 or 1 breaks, return `true`; otherwise, `false`.

Time complexity is $O(N)$ and space complexity is $O(1)$.
