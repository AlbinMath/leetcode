# Shuffle The Array

## Problem Explanation
Given an array `[x1,x2,...,xn,y1,y2,...,yn]`, return it in the form `[x1,y1,x2,y2,...,xn,yn]`.

## How the Code Works
The code creates a new result array and interleaves elements from the first half and second half. For index `i` from `0` to `n-1`, it places `nums[i]` at position `2*i` and `nums[n+i]` at position `2*i+1`.

Time complexity is $O(N)$ and space complexity is $O(N)$.
