# Add Two Promises

## Problem Explanation
Given two promises that resolve to numbers, return a promise that resolves to their sum.

## How the Code Works
`const [a, b] = await Promise.all([promise1, promise2]); return a + b;` — waits for both promises in parallel and returns their sum.
