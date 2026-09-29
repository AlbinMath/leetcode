# Exclusive Time Of Functions

## Problem Explanation
Given `n` functions with IDs from `0` to `n-1` and a list of logs in the format `"id:start_or_end:timestamp"`, compute the exclusive time of each function. Exclusive time is the total time a function spent executing, excluding time spent in nested function calls. Functions are single-threaded and can be called recursively.

## How the Code Works
The code uses a **Stack** to simulate the function call stack.

1. **Stack:** Stores the IDs of currently active functions. The top of the stack is the currently executing function.
2. **prevTime:** Tracks the timestamp of the last event processed.
3. **Processing Each Log:**
   - **Start event:** The function currently on top of the stack (if any) gets credited with the elapsed time (`time - prevTime`). The new function's ID is pushed onto the stack. `prevTime` is updated to `time`.
   - **End event:** The function on top of the stack is popped and credited with `time - prevTime + 1` (the `+1` accounts for the fact that end timestamps are inclusive). `prevTime` is set to `time + 1` (the next time unit starts after this end).
4. The `result` array accumulates the exclusive time for each function ID.

Time complexity is $O(L)$ where $L$ is the number of logs, and space complexity is $O(N)$ for the stack.
