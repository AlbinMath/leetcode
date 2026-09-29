# Group By

## Problem Explanation
Add a `groupBy(fn)` method to Array prototype that groups elements by the return value of `fn`.

## How the Code Works
Iterates through the array, applies `fn` to each element to get a key, and builds an object where each key maps to an array of elements that produced that key.
