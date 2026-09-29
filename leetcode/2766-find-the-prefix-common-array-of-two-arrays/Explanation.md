# Find The Prefix Common Array Of Two Arrays

## Problem Explanation
Given permutations A and B, compute C where C[i] = count of numbers that have appeared in both A[0..i] and B[0..i].

## How the Code Works
Maintain a frequency counter. For each index i, increment counts for A[i] and B[i]. If a count reaches 2, that number has appeared in both arrays up to this point. Track the running count of such numbers.
