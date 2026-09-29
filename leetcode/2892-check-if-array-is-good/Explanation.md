# Check If Array Is Good

## Problem Explanation
An array is "good" if it's a permutation of `[1, 2, ..., n-1, n, n]` for some `n`. Check if the given array is good.

## How the Code Works
Sort the array. The maximum value should be `n = arr.length - 1`. Check that the last two elements equal `n` and elements 0 through n-2 equal 1 through n-1 respectively.
