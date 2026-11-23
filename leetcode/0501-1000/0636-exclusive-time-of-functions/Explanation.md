# LeetCode 636: Exclusive Time of Functions

**LeetCode Problem #636 — Exclusive Time of Functions**
Solve LeetCode Exclusive Time of Functions using TypeScript and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Exclusive Time of Functions |
| LeetCode | #636 |
| Difficulty | Medium |
| Language | TypeScript |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
On a **single-threaded** CPU, we execute a program containing `n` functions. Each function has a unique ID between 0 and `n - 1`.

Function calls are **stored in a call stack **: when a function call starts, its ID is pushed onto the stack, and when a function call ends, its ID is popped off the stack. The function whose ID is at the top of the stack is **the current function being executed**. Each time a function starts or ends, we write a log with the ID, whether it started or ended, and the timestamp.

You are given a list `logs`, where `logs[i]` represents the `i^th` log message formatted as a string `"{function_id}:{"start" | "end"}:{timestamp}"`. For example, `"0:start:3"` means a function call with function ID 0 **started at the beginning** of timestamp 3, and `"1:end:2"` means a function call with function ID 1 **ended at the end** of timestamp 2. Note that a function can be called multiple times, possibly recursively .

A function's **exclusive time** is the sum of execution times for all function calls in the program. For example, if a function is called twice, one call executing for 2 time units and another call executing for 1 time unit, the **exclusive time** is `2 + 1 = 3`.

Return *the **exclusive time** of each function in an array, where the value at the *`i^th`* index represents the exclusive time for the function with ID *`i`.

## Constraints
- `1 <= n <= 100`
- `2 <= logs.length <= 500`
- `0 <= function_id < n`
- `0 <= timestamp <= 10^9`
- No two start events will happen at the same timestamp.
- No two end events will happen at the same timestamp.
- Each function has an `"end"` log for each `"start"` log.

## Examples
### Example 1
- **Input:** `n = 2, logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]`
- **Output:** `[3,4]`
- **Explanation:** Function 0 starts at the beginning of time 0, then it executes 2 for units of time and reaches the end of time 1.
Function 1 starts at the beginning of time 2, executes for 4 units of time, and ends at the end of time 5.
Function 0 resumes execution at the beginning of time 6 and executes for 1 unit of time.
So function 0 spends 2 + 1 = 3 units of total time executing, and function 1 spends 4 units of total time executing.

### Example 2
- **Input:** `n = 1, logs = ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]`
- **Output:** `[8]`
- **Explanation:** Function 0 starts at the beginning of time 0, executes for 2 units of time, and recursively calls itself.
Function 0 (recursive call) starts at the beginning of time 2 and executes for 4 units of time.
Function 0 (initial call) resumes execution then immediately calls itself again.
Function 0 (2nd recursive call) starts at the beginning of time 6 and executes for 1 unit of time.
Function 0 (initial call) resumes execution at the beginning of time 7 and executes for 1 unit of time.
So function 0 spends 2 + 4 + 1 + 1 = 8 units of total time executing.

### Example 3
- **Input:** `n = 2, logs = ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]`
- **Output:** `[7,1]`
- **Explanation:** Function 0 starts at the beginning of time 0, executes for 2 units of time, and recursively calls itself.
Function 0 (recursive call) starts at the beginning of time 2 and executes for 4 units of time.
Function 0 (initial call) resumes execution then immediately calls function 1.
Function 1 starts at the beginning of time 6, executes 1 unit of time, and ends at the end of time 6.
Function 0 resumes execution at the beginning of time 7 and executes for 1 unit of time.
So function 0 spends 2 + 4 + 1 = 7 units of total time executing, and function 1 spends 1 unit of total time executing.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code uses a **Stack** to simulate the function call stack.

1. **Stack:** Stores the IDs of currently active functions. The top of the stack is the currently executing function.
2. **prevTime:** Tracks the timestamp of the last event processed.
3. **Processing Each Log:**
   - **Start event:** The function currently on top of the stack (if any) gets credited with the elapsed time (`time - prevTime`). The new function's ID is pushed onto the stack. `prevTime` is updated to `time`.
   - **End event:** The function on top of the stack is popped and credited with `time - prevTime + 1` (the `+1` accounts for the fact that end timestamps are inclusive). `prevTime` is set to `time + 1` (the next time unit starts after this end).
4. The `result` array accumulates the exclusive time for each function ID.

Time complexity is $O(L)$ where $L$ is the number of logs, and space complexity is $O(N)$ for the stack.

## Algorithm
1. Initialize state variables / data structure (**Stack**).
2. Process elements sequentially using **Stack Push / Pop Parsing**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `n = 2, logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[3,4]`.
4. **Verification:** Function 0 starts at the beginning of time 0, then it executes 2 for units of time and reaches the end of time 1.
Function 1 starts at the beginning of time 2, executes for 4 units of time, and ends at the end of time 5.
Function 0 resumes execution at the beginning of time 6 and executes for 1 unit of time.
So function 0 spends 2 + 1 = 3 units of total time executing, and function 1 spends 4 units of total time executing.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
TypeScript

## Source Code
- [solution.ts](./solution.ts)


```typescript
function exclusiveTime(n: number, logs: string[]): number[] {
    const result = new Array(n).fill(0);
    const stack: number[] = [];

    let prevTime = 0;

    for (const log of logs) {
        const [idStr, type, timeStr] = log.split(":");
        const id = Number(idStr);
        const time = Number(timeStr);

        if (type === "start") {
            // Previous function runs until just before this start
            if (stack.length > 0) {
                result[stack[stack.length - 1]] += time - prevTime;
            }

            stack.push(id);
            prevTime = time;
        } else {
            // Current function runs through the end timestamp
            result[stack.pop()!] += time - prevTime + 1;

            // Next execution starts after this timestamp
            prevTime = time + 1;
        }
    }

    return result;
}
```

## Why This Works
By utilizing **Stack & Queue**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [121. Best Time to Buy and Sell Stock](../../0001-0500/0121-best-time-to-buy-and-sell-stock/)
- [122. Best Time to Buy and Sell Stock II](../../0001-0500/0122-best-time-to-buy-and-sell-stock-ii/)
- [123. Best Time to Buy and Sell Stock III](../../0001-0500/0123-best-time-to-buy-and-sell-stock-iii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/exclusive-time-of-functions/)
