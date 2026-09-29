# Evaluate The Bracket Pairs Of A String

## Problem Explanation
Given a string `s` with bracket pairs like `"(key)"` and a list of `[key, value]` pairs, replace each `(key)` with its value, or `"?"` if the key is not found.

## How the Code Works
1. **Map:** Store all key-value pairs in a hash map.
2. **Parse:** Iterate through the string. When encountering `(`, find the matching `)`, extract the key, look it up in the map, and append the value (or `?`) to the result.
3. Regular characters are appended directly.

Time complexity is $O(N + K)$ where $N$ is string length and $K$ is total key-value data, and space complexity is $O(N + K)$.
