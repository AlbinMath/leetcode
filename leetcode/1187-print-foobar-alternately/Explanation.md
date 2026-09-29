# Print Foobar Alternately

## Problem Explanation
Two threads are given: one prints `"foo"` and the other prints `"bar"`. They must alternate output to produce `"foobarfoobar..."` exactly `n` times. The `foo` thread must always go first.

## How the Code Works
The code uses **Semaphores** for synchronization.

1. `fooSem` starts at `1` (foo can go first) and `barSem` starts at `0` (bar must wait).
2. **foo thread:** Acquires `fooSem`, prints "foo", then releases `barSem` (allowing bar to proceed).
3. **bar thread:** Acquires `barSem`, prints "bar", then releases `fooSem` (allowing foo to proceed again).

This ping-pong of semaphores ensures strict alternation for `n` iterations.
