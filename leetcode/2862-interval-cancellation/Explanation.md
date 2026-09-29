# Interval Cancellation

## Problem Explanation
Call a function `fn` with `args` immediately and then every `t` milliseconds. Return a `cancelFn` that stops the interval.

## How the Code Works
Calls `fn(...args)` immediately, then starts `setInterval(fn, t, ...args)`. Returns a function that calls `clearInterval` to cancel the repeating execution.
