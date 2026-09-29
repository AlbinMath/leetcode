# Chunk Array

## Problem Explanation
Split an array into groups (chunks) of size `size`. The last chunk may be smaller.

## How the Code Works
Iterates through the array in steps of `size`, slicing `arr.slice(i, i + size)` for each chunk and pushing it to the result.
