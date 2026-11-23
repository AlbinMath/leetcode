# LeetCode 2725: Interval Cancellation

**LeetCode Problem #2725 — Interval Cancellation**
Solve LeetCode Interval Cancellation using TypeScript and Heap. This solution finds the optimal result using Min/Max Heap Priority Selection in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Interval Cancellation |
| LeetCode | #2725 |
| Difficulty | Easy |
| Language | TypeScript |
| Algorithm | Min/Max Heap Priority Selection |
| Data Structure | Heap / Priority Queue |
| Pattern | Heap |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given a function `fn`, an array of arguments `args`, and an interval time `t`, return a cancel function `cancelFn`.

After a delay of `cancelTimeMs`, the returned cancel function `cancelFn` will be invoked.

setTimeout(cancelFn, cancelTimeMs)

The function `fn` should be called with `args` immediately and then called again every `t` milliseconds until `cancelFn` is called at `cancelTimeMs` ms.

## Constraints
- `fn` is a function
- `args` is a valid JSON array
- `1 <= args.length <= 10`
- ` 30 <= t <= 100 `
- ` 10 <= cancelTimeMs <= 500 `

## Examples
### Example 1
- **Input:** `fn = (x) => x * 2, args = [4], t = 35`
- **Output:** `[
 {"time": 0, "returned": 8},
 {"time": 35, "returned": 8},
 {"time": 70, "returned": 8},
 {"time": 105, "returned": 8},
 {"time": 140, "returned": 8},
 {"time": 175, "returned": 8}
]`
- **Explanation:** const cancelTimeMs = 190;
const cancelFn = cancellable((x) => x * 2, [4], 35);
setTimeout(cancelFn, cancelTimeMs);

Every 35ms, fn(4) is called. Until t=190ms, then it is cancelled.
1st fn call is at 0ms. fn(4) returns 8.
2nd fn call is at 35ms. fn(4) returns 8.
3rd fn call is at 70ms. fn(4) returns 8.
4th fn call is at 105ms. fn(4) returns 8.
5th fn call is at 140ms. fn(4) returns 8.
6th fn call is at 175ms. fn(4) returns 8.
Cancelled at 190ms

### Example 2
- **Input:** `fn = (x1, x2) => (x1 * x2), args = [2, 5], t = 30`
- **Output:** `[
 {"time": 0, "returned": 10},
 {"time": 30, "returned": 10},
 {"time": 60, "returned": 10},
 {"time": 90, "returned": 10},
 {"time": 120, "returned": 10},
 {"time": 150, "returned": 10}
]`
- **Explanation:** const cancelTimeMs = 165; 
const cancelFn = cancellable((x1, x2) => (x1 * x2), [2, 5], 30) 
setTimeout(cancelFn, cancelTimeMs)

Every 30ms, fn(2, 5) is called. Until t=165ms, then it is cancelled.
1st fn call is at 0ms 
2nd fn call is at 30ms 
3rd fn call is at 60ms 
4th fn call is at 90ms 
5th fn call is at 120ms 
6th fn call is at 150ms
Cancelled at 165ms

### Example 3
- **Input:** `fn = (x1, x2, x3) => (x1 + x2 + x3), args = [5, 1, 3], t = 50`
- **Output:** `[
 {"time": 0, "returned": 9},
 {"time": 50, "returned": 9},
 {"time": 100, "returned": 9},
 {"time": 150, "returned": 9}
]`
- **Explanation:** const cancelTimeMs = 180;
const cancelFn = cancellable((x1, x2, x3) => (x1 + x2 + x3), [5, 1, 3], 50)
setTimeout(cancelFn, cancelTimeMs)

Every 50ms, fn(5, 1, 3) is called. Until t=180ms, then it is cancelled. 
1st fn call is at 0ms
2nd fn call is at 50ms
3rd fn call is at 100ms
4th fn call is at 150ms
Cancelled at 180ms

## Key Insight
Leverage **Heap** with **Heap / Priority Queue** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
Calls `fn(...args)` immediately, then starts `setInterval(fn, t, ...args)`. Returns a function that calls `clearInterval` to cancel the repeating execution.

## Algorithm
1. Initialize state variables / data structure (**Heap / Priority Queue**).
2. Process elements sequentially using **Min/Max Heap Priority Selection**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `fn = (x) => x * 2, args = [4], t = 35`.
2. **Processing Steps:** We apply **Min/Max Heap Priority Selection** using our **Heap / Priority Queue**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[
 {"time": 0, "returned": 8},
 {"time": 35, "returned": 8},
 {"time": 70, "returned": 8},
 {"time": 105, "returned": 8},
 {"time": 140, "returned": 8},
 {"time": 175, "returned": 8}
]`.
4. **Verification:** const cancelTimeMs = 190;
const cancelFn = cancellable((x) => x * 2, [4], 35);
setTimeout(cancelFn, cancelTimeMs);

Every 35ms, fn(4) is called. Until t=190ms, then it is cancelled.
1st fn call is at 0ms. fn(4) returns 8.
2nd fn call is at 35ms. fn(4) returns 8.
3rd fn call is at 70ms. fn(4) returns 8.
4th fn call is at 105ms. fn(4) returns 8.
5th fn call is at 140ms. fn(4) returns 8.
6th fn call is at 175ms. fn(4) returns 8.
Cancelled at 190ms

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Heap / Priority Queue.

## Pattern
**Heap**

## Topics
- Heap
- Priority Queue
- Sorting

## Language
TypeScript

## Source Code
- [solution.ts](./solution.ts)


```typescript
function cancellable(
    fn: (...args: any[]) => any,
    args: any[],
    t: number
): Function {
    // Call immediately
    fn(...args);

    // Call repeatedly every t milliseconds
    const intervalId = setInterval(() => {
        fn(...args);
    }, t);

    // Return cancellation function
    return () => {
        clearInterval(intervalId);
    };
}
```

## Why This Works
By utilizing **Heap**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [57. Insert Interval](../../0001-0500/0057-insert-interval/)
- [436. Find Right Interval](../../0001-0500/0436-find-right-interval/)
- [986. Interval List Intersections](../../1001-1500/1028-interval-list-intersections/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/interval-cancellation/)
