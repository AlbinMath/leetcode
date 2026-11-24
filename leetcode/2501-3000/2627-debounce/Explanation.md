# LeetCode 2627: Debounce

**LeetCode Problem #2627 — Debounce**
Solve LeetCode Debounce using TypeScript and Sliding Window. This solution finds the optimal result using Dynamic Sliding Window Traversal in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Debounce |
| LeetCode | #2627 |
| Difficulty | Medium |
| Language | TypeScript |
| Algorithm | Dynamic Sliding Window Traversal |
| Data Structure | Array / Hash Set |
| Pattern | Sliding Window |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a function `fn` and a time in milliseconds `t`, return a **debounced** version of that function.

A **debounced** function is a function whose execution is delayed by `t` milliseconds and whose execution is cancelled if it is called again within that window of time. The debounced function should also receive the passed parameters.

For example, let's say `t = 50ms`, and the function was called at `30ms`, `60ms`, and `100ms`.

The first 2 function calls would be cancelled, and the 3rd function call would be executed at `150ms`.

If instead `t = 35ms`, The 1st call would be cancelled, the 2nd would be executed at `95ms`, and the 3rd would be executed at `135ms`.

The above diagram shows how debounce will transform events. Each rectangle represents 100ms and the debounce time is 400ms. Each color represents a different set of inputs.

Please solve it without using lodash's `_.debounce()` function.

## Constraints
- `0 <= t <= 1000`
- `1 <= calls.length <= 10`
- `0 <= calls[i].t <= 1000`
- `0 <= calls[i].inputs.length <= 10`

## Examples
### Example 1
- **Input:** `t = 50
calls = [
 {"t": 50, inputs: [1]},
 {"t": 75, inputs: [2]}
]`
- **Output:** `[{"t": 125, inputs: [2]}]`
- **Explanation:** let start = Date.now();
function log(...inputs) { 
 console.log([Date.now() - start, inputs ])
}
const dlog = debounce(log, 50);
setTimeout(() => dlog(1), 50);
setTimeout(() => dlog(2), 75);

The 1st call is cancelled by the 2nd call because the 2nd call occurred before 100ms
The 2nd call is delayed by 50ms and executed at 125ms. The inputs were (2).

### Example 2
- **Input:** `t = 20
calls = [
 {"t": 50, inputs: [1]},
 {"t": 100, inputs: [2]}
]`
- **Output:** `[{"t": 70, inputs: [1]}, {"t": 120, inputs: [2]}]`
- **Explanation:** The 1st call is delayed until 70ms. The inputs were (1).
The 2nd call is delayed until 120ms. The inputs were (2).

### Example 3
- **Input:** `t = 150
calls = [
 {"t": 50, inputs: [1, 2]},
 {"t": 300, inputs: [3, 4]},
 {"t": 300, inputs: [5, 6]}
]`
- **Output:** `[{"t": 200, inputs: [1,2]}, {"t": 450, inputs: [5, 6]}]`
- **Explanation:** The 1st call is delayed by 150ms and ran at 200ms. The inputs were (1, 2).
The 2nd call is cancelled by the 3rd call
The 3rd call is delayed by 150ms and ran at 450ms. The inputs were (5, 6).

## Key Insight
Maintain a dynamic contiguous window with two pointers (`left` and `right`), expanding to include new elements and shrinking when window invariants are violated.

## Approach
Uses a closure with a `timer` variable. Each call clears the previous timer with `clearTimeout(timer)` and sets a new one with `setTimeout(fn, t)`. This ensures `fn` only executes after the caller stops calling for `t` ms.

## Algorithm
1. Initialize state variables / data structure (**Array / Hash Set**).
2. Process elements sequentially using **Dynamic Sliding Window Traversal**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `t = 50
calls = [
 {"t": 50, inputs: [1]},
 {"t": 75, inputs: [2]}
]`.
2. **Processing Steps:** We apply **Dynamic Sliding Window Traversal** using our **Array / Hash Set**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[{"t": 125, inputs: [2]}]`.
4. **Verification:** let start = Date.now();
function log(...inputs) { 
 console.log([Date.now() - start, inputs ])
}
const dlog = debounce(log, 50);
setTimeout(() => dlog(1), 50);
setTimeout(() => dlog(2), 75);

The 1st call is cancelled by the 2nd call because the 2nd call occurred before 100ms
The 2nd call is delayed by 50ms and executed at 125ms. The inputs were (2).

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array / Hash Set.

## Pattern
**Sliding Window**

## Topics
- Sliding Window
- Two Pointers
- Subarrays

## Language
TypeScript

## Source Code
- [solution.ts](./solution.ts)


```typescript
function debounce(
    fn: (...args: any[]) => any,
    t: number
): (...args: any[]) => void {
    let timer: ReturnType<typeof setTimeout>;

    return function (...args: any[]) {
        // Cancel the previous scheduled call
        clearTimeout(timer);

        // Schedule the latest call
        timer = setTimeout(() => {
            fn(...args);
        }, t);
    };
}
```

## Why This Works
By utilizing **Sliding Window**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Shrinking the window too late or missing invalid state checks.
2. Forgetting to update window metrics (e.g. char counts) during contraction.
3. Misinterpreting fixed vs variable window requirements.

## Interview Notes
- **Tests:** Two-pointer window management, state tracking, and contiguous subarray analysis.
- **Follow-up:** How do you handle non-positive integer values in subarray sum windows?

## Related Problems
- [3. Longest Substring Without Repeating Characters](../../0001-0500/0003-longest-substring-without-repeating-characters/)
- [30. Substring with Concatenation of All Words](../../0001-0500/0030-substring-with-concatenation-of-all-words/)
- [76. Minimum Window Substring](../../0001-0500/0076-minimum-window-substring/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/debounce/)
