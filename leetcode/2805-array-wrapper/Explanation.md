# Array Wrapper

## Problem Explanation
Create an ArrayWrapper class. When two instances are added with `+`, return the sum of all elements. `String()` should return a comma-separated representation in brackets.

## How the Code Works
Override `valueOf()` to return the sum of the internal array (used by `+` operator) and `toString()` to return `"[elements]"` format.
