# Cache With Time Limit

## Problem Explanation
Implement a cache where each key has an expiration time. `set(key, value, duration)` stores a value that expires after `duration` ms. `get(key)` returns the value if not expired. `count()` returns the number of non-expired keys.

## How the Code Works
Uses a Map to store `{value, timer}` for each key. On `set`, clear any existing timer and create a new `setTimeout` that deletes the key after `duration` ms. On `get`, return the value if the key exists. On `count`, return the Map's size.
