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

## Problem
On a  single-threaded  CPU, we execute a program containing  n  functions. Each function has a unique ID between 0 and  n - 1 .

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

## Example
Consider the standard input for **Exclusive Time of Functions**. Applying **Stack Push / Pop Parsing** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
TypeScript

## Source Code
- [solution.ts](./solution.ts)

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
- [1801. Number of Orders in the Backlog](../1801-average-time-of-process-per-machine/)
- [1892. Page Recommendations II](../1892-find-total-time-spent-by-each-employee/)
- [2749. Minimum Operations to Make the Integer Zero](../2749-promise-time-limit/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/exclusive-time-of-functions/)
