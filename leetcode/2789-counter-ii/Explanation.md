# Counter II

## Problem Explanation
Create a counter with `increment()`, `decrement()`, and `reset()` methods. The counter starts at `init` and reset returns it to `init`.

## How the Code Works
Uses a closure to capture `init` and a mutable `count` variable. `increment` returns `++count`, `decrement` returns `--count`, and `reset` sets `count = init` and returns it.
