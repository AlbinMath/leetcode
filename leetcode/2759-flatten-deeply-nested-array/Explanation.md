# Flatten Deeply Nested Array

## Problem Explanation
Flatten a multi-dimensional array up to depth `n`.

## How the Code Works
Uses recursion: if depth > 0, iterate through elements. If an element is an array, recursively flatten it with `depth - 1`. Otherwise, add the element directly to the result.
