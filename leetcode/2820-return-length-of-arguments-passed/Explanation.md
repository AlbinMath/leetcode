# Return Length Of Arguments Passed

## Problem Explanation
Create a function that returns the number of arguments passed to it.

## How the Code Works
Uses rest parameters: `function(...args) { return args.length; }`. The spread operator collects all arguments into an array, and `.length` gives the count.
