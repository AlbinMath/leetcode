# Print In Order

## Problem Explanation
Three threads are given, each printing `"first"`, `"second"`, or `"third"`. Regardless of the order the threads are started, the output must always be `"firstsecondthird"`.

## How the Code Works
The code uses **Semaphores** (or equivalent synchronization) to enforce ordering.

1. Two semaphores control the gates: `sem1` (blocks `second`) and `sem2` (blocks `third`), both starting at `0`.
2. **first():** Prints "first", then releases `sem1`.
3. **second():** Waits on `sem1`, prints "second", then releases `sem2`.
4. **third():** Waits on `sem2`, then prints "third".

This chain of semaphores guarantees the correct order regardless of thread scheduling.
