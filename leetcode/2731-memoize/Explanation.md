# Memoize

## Problem Explanation
Implement a `memoize` function that caches the results of a function call. If the same inputs are provided again, return the cached result instead of recalculating.

## How the Code Works
The memoize function wraps the input function with a closure that maintains a cache (Map/Object). Before calling the original function, it checks if the arguments have been seen before (using a key derived from the arguments). If cached, return the stored result; otherwise, call the function, store the result, and return it.
