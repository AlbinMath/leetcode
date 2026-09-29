# Memoize II

## Problem Explanation
Implement a memoize function that works with functions accepting any type of arguments (not just primitives). Two calls with the same references should return cached results.

## How the Code Works
Uses a **trie-like cache** or `WeakMap`/`Map` structure keyed by argument references. For each call, traverses the cache structure using each argument as a key, creating new nodes as needed. At the final node, stores the computed result for future lookups.
