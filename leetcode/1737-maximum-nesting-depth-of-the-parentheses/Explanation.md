# Maximum Nesting Depth Of The Parentheses

## Problem Explanation
Given a valid parenthesized string (VPS), return the maximum nesting depth.

## How the Code Works
The code tracks the current `depth` using a counter. For each `(`, increment depth and update `maxDepth`. For each `)`, decrement depth. The maximum value of `depth` during the scan is the answer.

Time complexity is $O(N)$ and space complexity is $O(1)$.
