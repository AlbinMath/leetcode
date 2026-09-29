# Sort By

## Problem Explanation
Sort an array based on a provided function `fn` that returns the sort key for each element.

## How the Code Works
`arr.sort((a, b) => fn(a) - fn(b))` — uses the built-in sort with a comparator that compares the return values of `fn` applied to each element.
