# Sleep

## Problem Explanation
Implement a `sleep` function that returns a Promise which resolves after `millis` milliseconds.

## How the Code Works
Returns `new Promise(resolve => setTimeout(resolve, millis))`. The `setTimeout` schedules the `resolve` callback after the specified delay, making the promise resolve after that time.
