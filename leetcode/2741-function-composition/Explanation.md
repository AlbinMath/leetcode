# Function Composition

## Problem Explanation
Given an array of functions `[f1, f2, ..., fn]`, return a new function that is the composition `f1(f2(...fn(x)))`.

## How the Code Works
Uses `Array.reduceRight` to apply functions from right to left. The composed function takes input `x`, passes it through the last function first, then feeds each result to the previous function.
