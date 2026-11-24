# LeetCode 2721: Execute Asynchronous Functions in Parallel

**LeetCode Problem #2721 — Execute Asynchronous Functions in Parallel**
Solve LeetCode Execute Asynchronous Functions in Parallel using TypeScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Execute Asynchronous Functions in Parallel |
| LeetCode | #2721 |
| Difficulty | Medium |
| Language | TypeScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an array of asynchronous functions `functions`, return a new promise `promise`. Each function in the array accepts no arguments and returns a promise. All the promises should be executed in parallel.

`promise` resolves:

When all the promises returned from `functions` were resolved successfully in parallel. The resolved value of `promise` should be an array of all the resolved values of promises in the same order as they were in the `functions`. The `promise` should resolve when all the asynchronous functions in the array have completed execution in parallel.

`promise` rejects:

When any of the promises returned from `functions` were rejected. `promise` should also reject with the reason of the first rejection.

Please solve it without using the built-in `Promise.all` function.

## Constraints
- `functions` is an array of functions that returns promises
- `1 <= functions.length <= 10`

## Examples
### Example 1
- **Input:** `functions = [
 () => new Promise(resolve => setTimeout(() => resolve(5), 200))
]`
- **Output:** `{"t": 200, "resolved": [5]}`
- **Explanation:** promiseAll(functions).then(console.log); // [5]

The single function was resolved at 200ms with a value of 5.

### Example 2
- **Input:** `functions = [
 () => new Promise(resolve => setTimeout(() => resolve(1), 200)), 
 () => new Promise((resolve, reject) => setTimeout(() => reject("Error"), 100))
]`
- **Output:** `{"t": 100, "rejected": "Error"}`
- **Explanation:** Since one of the promises rejected, the returned promise also rejected with the same error at the same time.

### Example 3
- **Input:** `functions = [
 () => new Promise(resolve => setTimeout(() => resolve(4), 50)), 
 () => new Promise(resolve => setTimeout(() => resolve(10), 150)), 
 () => new Promise(resolve => setTimeout(() => resolve(16), 100))
]`
- **Output:** `{"t": 150, "resolved": [4, 10, 16]}`
- **Explanation:** All the promises resolved with a value. The returned promise resolved when the last promise resolved.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
Implements `Promise.all` from scratch. Creates a promise that tracks completed count. Each function's result is stored at its index. When all complete, resolve with the results array. If any rejects, immediately reject the outer promise.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Two Pointer Convergence & Scanning**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `functions = [
 () => new Promise(resolve => setTimeout(() => resolve(5), 200))
]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `{"t": 200, "resolved": [5]}`.
4. **Verification:** promiseAll(functions).then(console.log); // [5]

The single function was resolved at 200ms with a value of 5.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

## Language
TypeScript

## Source Code
- [solution.ts](./solution.ts)


```typescript
type P = () => Promise<any>;

function promiseAll(functions: P[]): Promise<any[]> {
    return new Promise((resolve, reject) => {
        const results: any[] = [];
        let completed = 0;

        for (let i = 0; i < functions.length; i++) {
            functions[i]()
                .then((value) => {
                    results[i] = value;
                    completed++;

                    // All promises completed
                    if (completed === functions.length) {
                        resolve(results);
                    }
                })
                .catch((error) => {
                    reject(error);
                });
        }
    });
}
```

## Why This Works
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [1494. Parallel Courses II](../../1001-1500/1494-parallel-courses-ii/)
- [2050. Parallel Courses III](../../2001-2500/2050-parallel-courses-iii/)
- [636. Exclusive Time of Functions](../../0501-1000/0636-exclusive-time-of-functions/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/execute-asynchronous-functions-in-parallel/)
