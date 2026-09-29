# Is Object Empty

## Problem Explanation
Return `true` if an object or array is empty (has no keys/elements).

## How the Code Works
For arrays: `arr.length === 0`. For objects: `Object.keys(obj).length === 0`. Checks if there are any enumerable properties.
