# Rank Transform Of An Array

## Problem Explanation
Given an array of integers `arr`, replace each element with its rank. The rank is assigned based on value: the smallest element gets rank 1, the second smallest gets rank 2, and equal elements get the same rank.

## How the Code Works
1. **Sort a Copy:** Clone the array and sort it.
2. **Map Values to Ranks:** Iterate through the sorted array, assigning incrementing ranks. Skip duplicates (if a value was already assigned a rank, don't increment).
3. **Replace:** Build the result by looking up each original element's rank from the map.

Time complexity is $O(N \log N)$ for sorting and space complexity is $O(N)$.
