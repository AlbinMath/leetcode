# LeetCode 2637: Promise Time Limit

**LeetCode Problem #2637 — Promise Time Limit**
Solve LeetCode Promise Time Limit using TypeScript and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Promise Time Limit |
| LeetCode | #2637 |
| Difficulty | Medium |
| Language | TypeScript |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an asynchronous function `fn` and a time `t` in milliseconds, return a new **time limited** version of the input function. `fn` takes arguments provided to the **time limited **function.

The **time limited** function should follow these rules:

If the `fn` completes within the time limit of `t` milliseconds, the **time limited** function should resolve with the result. 
 If the execution of the `fn` exceeds the time limit, the **time limited** function should reject with the string `"Time Limit Exceeded"`.

## Constraints
- `0 <= inputs.length <= 10`
- `0 <= t <= 1000`
- `fn` returns a promise

## Examples
### Example 1
- **Input:** `fn = async (n) => { 
 await new Promise(res => setTimeout(res, 100)); 
 return n * n; 
}
inputs = [5]
t = 50`
- **Output:** `{"rejected":"Time Limit Exceeded","time":50}`
- **Explanation:** const limited = timeLimit(fn, t)
const start = performance.now()
let result;
try {
 const res = await limited(...inputs)
 result = {"resolved": res, "time": Math.floor(performance.now() - start)};
} catch (err) {
 result = {"rejected": err, "time": Math.floor(performance.now() - start)};
}
console.log(result) // Output

The provided function is set to resolve after 100ms. However, the time limit is set to 50ms. It rejects at t=50ms because the time limit was reached.

### Example 2
- **Input:** `fn = async (n) => { 
 await new Promise(res => setTimeout(res, 100)); 
 return n * n; 
}
inputs = [5]
t = 150`
- **Output:** `{"resolved":25,"time":100}`
- **Explanation:** The function resolved 5 * 5 = 25 at t=100ms. The time limit is never reached.

### Example 3
- **Input:** `fn = async (a, b) => { 
 await new Promise(res => setTimeout(res, 120)); 
 return a + b; 
}
inputs = [5,10]
t = 150`
- **Output:** `{"resolved":15,"time":120}`
- **Explanation:** ​​​​The function resolved 5 + 10 = 15 at t=120ms. The time limit is never reached.

### Example 4
- **Input:** `fn = async () => { 
 throw "Error";
}
inputs = []
t = 1000`
- **Output:** `{"rejected":"Error","time":0}`
- **Explanation:** The function immediately throws an error.

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
Returns a function that creates a `Promise.race` between the original async function call and a timeout promise that rejects after `t` milliseconds. Whichever settles first wins.

## Algorithm
1. Initialize state variables / data structure (**Primitive Types**).
2. Process elements sequentially using **Mathematical Simulation & Modular Arithmetic**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `fn = async (n) => { 
 await new Promise(res => setTimeout(res, 100)); 
 return n * n; 
}
inputs = [5]
t = 50`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `{"rejected":"Time Limit Exceeded","time":50}`.
4. **Verification:** const limited = timeLimit(fn, t)
const start = performance.now()
let result;
try {
 const res = await limited(...inputs)
 result = {"resolved": res, "time": Math.floor(performance.now() - start)};
} catch (err) {
 result = {"rejected": err, "time": Math.floor(performance.now() - start)};
}
console.log(result) // Output

The provided function is set to resolve after 100ms. However, the time limit is set to 50ms. It rejects at t=50ms because the time limit was reached.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Primitive Types.

## Pattern
**Math & Logic**

## Topics
- Math
- Simulation

## Language
TypeScript

## Source Code
- [solution.ts](./solution.ts)


```typescript
type Fn = (...args: any[]) => Promise<any>;

function timeLimit(fn: Fn, t: number): Fn {
    return async function (...args: any[]) {
        return new Promise((resolve, reject) => {
            const timer = setTimeout(() => {
                reject("Time Limit Exceeded");
            }, t);

            fn(...args)
                .then((result) => {
                    clearTimeout(timer);
                    resolve(result);
                })
                .catch((error) => {
                    clearTimeout(timer);
                    reject(error);
                });
        });
    };
}
```

## Why This Works
By utilizing **Math & Logic**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [2622. Cache With Time Limit](../../2501-3000/2762-cache-with-time-limit/)
- [1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit](../../1501-2000/1549-longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/)
- [2468. Split Message Based on Limit](../../2501-3000/2563-split-message-based-on-limit/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/promise-time-limit/)
