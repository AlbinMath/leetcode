# Daily Temperatures

## Problem Explanation
Given an array of integers `temperatures` representing daily temperatures, return an array `result` where `result[i]` is the number of days you have to wait after the `i`th day to get a warmer temperature. If there is no future day with a warmer temperature, `result[i] = 0`.

## How the Code Works
The code uses a **Monotonic Stack** (decreasing) to efficiently find the next warmer day for each index.

1. **Stack of Indices:** The stack stores indices of days whose "next warmer day" hasn't been found yet, in decreasing order of temperature.
2. **Iteration:** For each day `i`:
   - While the stack is not empty and `temperatures[i]` is greater than the temperature at the index on top of the stack: pop the index `prev` and set `result[prev] = i - prev`.
   - Push `i` onto the stack.
3. Any indices remaining in the stack after the loop already have `result[i] = 0` (initialized at the start).

Time complexity is $O(N)$ (each index is pushed and popped at most once) and space complexity is $O(N)$.
