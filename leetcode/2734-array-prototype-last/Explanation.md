# Array Prototype Last

## Problem Explanation
Add a `last()` method to the Array prototype that returns the last element, or `-1` if the array is empty.

## How the Code Works
`Array.prototype.last = function() { return this.length ? this[this.length - 1] : -1; }`. Checks if the array has elements and returns the last one, or -1 if empty.
