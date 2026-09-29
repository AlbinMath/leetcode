# Print Zero Even Odd

## Problem Explanation
Three threads must cooperate to print the sequence `"0102030405..."` up to `n`. The `zero` thread prints `0`, the `even` thread prints even numbers, and the `odd` thread prints odd numbers.

## How the Code Works
The code uses three **Semaphores** for synchronization.

1. **Semaphore State:** `zero` starts at `1` (goes first), `even` and `odd` start at `0`.
2. **zero thread:** For each number `i` from `1` to `n`, acquires the `zero` semaphore, prints `0`, then releases either `odd` (if `i` is odd) or `even` (if `i` is even).
3. **odd thread:** For each odd number, acquires the `odd` semaphore, prints the odd number, then releases `zero`.
4. **even thread:** For each even number, acquires the `even` semaphore, prints the even number, then releases `zero`.

This creates the pattern: zero→odd→zero→even→zero→odd→... producing `"010203..."`.
