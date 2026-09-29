# Maximum Product Of Two Elements In An Array

## Problem Explanation
Given an array of integers, return the maximum value of `(nums[i]-1)*(nums[j]-1)` where `i != j`.

## How the Code Works
The code finds the two largest elements in the array (either by sorting or a single-pass scan). The maximum product is `(largest - 1) * (secondLargest - 1)` since subtracting 1 from the two biggest numbers gives the best result.

Time complexity is $O(N)$ with a single pass (or $O(N \log N)$ with sorting) and space complexity is $O(1)$.
