# Generate Fibonacci Sequence

## Problem Explanation
Create a generator function that yields the Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, ...

## How the Code Works
Uses a generator function (`function*`) that maintains two variables `a` and `b`. In an infinite loop, it `yield`s `a`, then updates: `[a, b] = [b, a + b]`.
