# Execute Asynchronous Functions In Parallel

## Problem Explanation
Given an array of async functions, execute them in parallel and return all results, or reject if any fails.

## How the Code Works
Implements `Promise.all` from scratch. Creates a promise that tracks completed count. Each function's result is stored at its index. When all complete, resolve with the results array. If any rejects, immediately reject the outer promise.
