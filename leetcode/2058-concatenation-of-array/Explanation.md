# Concatenation Of Array

## Problem Explanation
Given an integer array `nums` of length `n`, return an array of length `2n` that is the concatenation of `nums` with itself.

## How the Code Works
The code creates a new array of size `2n` and copies `nums` twice — once at the beginning and once starting at index `n`. Alternatively, it simply concatenates the array with itself using spread/concat.

Time complexity is $O(N)$ and space complexity is $O(N)$.
