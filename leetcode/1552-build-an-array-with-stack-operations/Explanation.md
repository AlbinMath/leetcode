# Build An Array With Stack Operations

## Problem Explanation
Given a target array and integer `n`, simulate building the target using `Push` and `Pop` operations on an empty stack, reading integers `1, 2, ..., n` in order. Return the sequence of operations.

## How the Code Works
The code iterates through numbers 1 to n while tracking which element of the target we need next. If the current number matches the next target element, push it. If it doesn't match, push then immediately pop it (to skip that number). Stop once the entire target is built.

Time complexity is $O(N)$ and space complexity is $O(N)$ for the output.
