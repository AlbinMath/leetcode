# Filter Elements From Array

## Problem Explanation
Implement `Array.prototype.filter` from scratch. Given a callback `fn(element, index)`, return a new array with only elements where `fn` returns truthy.

## How the Code Works
Iterates through the array, calls `fn(arr[i], i)` for each element, and pushes elements to the result array when the callback returns a truthy value.
