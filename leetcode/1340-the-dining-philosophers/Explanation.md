# The Dining Philosophers

## Problem Explanation
Five philosophers sit around a table with five forks. Each philosopher needs both forks adjacent to them to eat. The challenge is to allow concurrent eating without deadlocks.

## How the Code Works
The code uses `std::lock` with `defer_lock` to acquire both forks atomically.

1. Each fork is represented by a `mutex`. Philosopher `i` needs forks `i` and `(i+1) % 5`.
2. `unique_lock` with `defer_lock` creates lock guards without immediately locking.
3. `std::lock(leftLock, rightLock)` acquires both locks simultaneously using a deadlock-avoidance algorithm.
4. The philosopher picks up forks, eats, puts them down, and the locks are automatically released when the `unique_lock` objects go out of scope.

This eliminates deadlocks because `std::lock` uses an internal ordering to prevent circular wait.
