# Promise Time Limit

## Problem Explanation
Create a function that wraps an async function with a time limit. If the function doesn't resolve within `t` ms, reject with "Time Limit Exceeded".

## How the Code Works
Returns a function that creates a `Promise.race` between the original async function call and a timeout promise that rejects after `t` milliseconds. Whichever settles first wins.
