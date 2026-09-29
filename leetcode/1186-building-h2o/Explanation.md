# Building H2O

## Problem Explanation
There are two kinds of threads: hydrogen and oxygen. Your goal is to group these threads to form water molecules (H₂O). Each water molecule requires exactly two hydrogen threads and one oxygen thread to be released together. The barrier is that threads must wait for the right combination before proceeding.

## How the Code Works
The code uses a **mutex** and **condition variable** for thread synchronization.

1. **Shared State:** `hydrogenCount` and `oxygenCount` track how many of each have been released in the current molecule.
2. **Hydrogen Thread:**
   - Waits until `hydrogenCount < 2` (room for more hydrogen in the current molecule).
   - Increments `hydrogenCount` and releases the hydrogen.
   - If `hydrogenCount == 2`, notifies all waiting threads (the oxygen thread can now proceed).
3. **Oxygen Thread:**
   - Waits until both hydrogens are ready (`hydrogenCount == 2`) and no oxygen has been released yet (`oxygenCount == 0`).
   - Increments `oxygenCount` and releases the oxygen.
   - Resets both counters to `0` and notifies all threads, allowing the next molecule to start forming.

This ensures every water molecule has exactly 2 H atoms and 1 O atom before any thread proceeds.
