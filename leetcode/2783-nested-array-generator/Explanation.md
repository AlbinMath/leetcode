# Nested Array Generator

## Problem Explanation
Create a generator that yields all values from a multi-dimensional array in order.

## How the Code Works
Uses a recursive generator: for each element, if it's an array, `yield*` the recursive call on that sub-array. Otherwise, `yield` the element directly. This lazily flattens the nested structure.
