# Debounce

## Problem Explanation
Implement a debounce function that delays invoking `fn` until `t` milliseconds after the last call.

## How the Code Works
Uses a closure with a `timer` variable. Each call clears the previous timer with `clearTimeout(timer)` and sets a new one with `setTimeout(fn, t)`. This ensures `fn` only executes after the caller stops calling for `t` ms.
