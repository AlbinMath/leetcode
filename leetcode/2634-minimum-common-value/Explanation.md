# Minimum Common Value

## Problem Explanation
Given two sorted integer arrays, return the smallest integer common to both. Return -1 if none.

## How the Code Works
Use **two pointers**, one for each array. If values match, return it. Otherwise advance the pointer with the smaller value. If either pointer reaches the end, return -1. Time: $O(N + M)$, Space: $O(1)$.
