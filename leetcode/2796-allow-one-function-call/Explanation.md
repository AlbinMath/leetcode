# Allow One Function Call

## Problem Explanation
Create a wrapper that allows the given function to be called at most once. Subsequent calls return `undefined`.

## How the Code Works
Uses a boolean flag `called` in a closure. On the first call, sets `called = true` and returns the function's result. On subsequent calls, returns `undefined`.
