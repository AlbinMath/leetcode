# Find Greatest Common Divisor Of Array

## Problem Explanation
Given an integer array `nums`, return the GCD of the smallest and largest numbers in the array.

## How the Code Works
1. Find the minimum and maximum of the array.
2. Compute the GCD of those two values using the Euclidean algorithm.

Time complexity is $O(N + \log(\min))$ and space complexity is $O(1)$.
