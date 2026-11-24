# LeetCode 2650: Design Cancellable Function

**LeetCode Problem #2650 — Design Cancellable Function**
Solve LeetCode Design Cancellable Function using TypeScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Design Cancellable Function |
| LeetCode | #2650 |
| Difficulty | Hard |
| Language | TypeScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Sometimes you have a long running task, and you may wish to cancel it before it completes. To help with this goal, write a function `cancellable` that accepts a generator object and returns an array of two values: a **cancel function** and a **promise**.

You may assume the generator function will only yield promises. It is your function's responsibility to pass the values resolved by the promise back to the generator. If the promise rejects, your function should throw that error back to the generator.

If the cancel callback is called before the generator is done, your function should throw an error back to the generator. That error should be the string `"Cancelled"` (Not an `Error` object). If the error was caught, the returned promise should resolve with the next value that was yielded or returned. Otherwise, the promise should reject with the thrown error. No more code should be executed.

When the generator is done, the promise your function returned should resolve the value the generator returned. If, however, the generator throws an error, the returned promise should reject with the error.

An example of how your code would be used:

function* tasks() {
 const val = yield new Promise(resolve => resolve(2 + 2));
 yield new Promise(resolve => setTimeout(resolve, 100));
 return val + 1; // calculation shouldn't be done.
}
const [cancel, promise] = cancellable(tasks());
setTimeout(cancel, 50);
promise.catch(console.log); // logs "Cancelled" at t=50ms

If instead `cancel()` was not called or was called after `t=100ms`, the promise would have resolved `5`.

## Constraints
- `cancelledAt == null or 0 <= cancelledAt <= 1000`
- `generatorFunction` returns a generator object

## Examples
### Example 1
- **Input:** `generatorFunction = function*() { 
 return 42; 
}
cancelledAt = 100`
- **Output:** `{"resolved": 42}`
- **Explanation:** const generator = generatorFunction();
const [cancel, promise] = cancellable(generator);
setTimeout(cancel, 100);
promise.then(console.log); // resolves 42 at t=0ms

The generator immediately yields 42 and finishes. Because of that, the returned promise immediately resolves 42. Note that cancelling a finished generator does nothing.

### Example 2
- **Input:** `generatorFunction = function*() { 
 const msg = yield new Promise(res => res("Hello")); 
 throw `Error: ${msg}`; 
}
cancelledAt = null`
- **Output:** `{"rejected": "Error: Hello"}`
- **Explanation:** A promise is yielded. The function handles this by waiting for it to resolve and then passes the resolved value back to the generator. Then an error is thrown which has the effect of causing the promise to reject with the same thrown error.

### Example 3
- **Input:** `generatorFunction = function*() { 
 yield new Promise(res => setTimeout(res, 200)); 
 return "Success"; 
}
cancelledAt = 100`
- **Output:** `{"rejected": "Cancelled"}`
- **Explanation:** While the function is waiting for the yielded promise to resolve, cancel() is called. This causes an error message to be sent back to the generator. Since this error is uncaught, the returned promise rejected with this error.

### Example 4
- **Input:** `generatorFunction = function*() { 
 let result = 0; 
 yield new Promise(res => setTimeout(res, 100));
 result += yield new Promise(res => res(1)); 
 yield new Promise(res => setTimeout(res, 100)); 
 result += yield new Promise(res => res(1)); 
 return result;
}
cancelledAt = null`
- **Output:** `{"resolved": 2}`
- **Explanation:** 4 promises are yielded. Two of those promises have their values added to the result. After 200ms, the generator finishes with a value of 2, and that value is resolved by the returned promise.

### Example 5
- **Input:** `generatorFunction = function*() { 
 let result = 0; 
 try { 
 yield new Promise(res => setTimeout(res, 100)); 
 result += yield new Promise(res => res(1)); 
 yield new Promise(res => setTimeout(res, 100)); 
 result += yield new Promise(res => res(1)); 
 } catch(e) { 
 return result; 
 } 
 return result; 
}
cancelledAt = 150`
- **Output:** `{"resolved": 1}`
- **Explanation:** The first two yielded promises resolve and cause the result to increment. However, at t=150ms, the generator is cancelled. The error sent to the generator is caught and the result is returned and finally resolved by the returned promise.

### Example 6
- **Input:** `generatorFunction = function*() { 
 try { 
 yield new Promise((resolve, reject) => reject("Promise Rejected")); 
 } catch(e) { 
 let a = yield new Promise(resolve => resolve(2));
 let b = yield new Promise(resolve => resolve(2)); 
 return a + b; 
 }; 
}
cancelledAt = null`
- **Output:** `{"resolved": 4}`
- **Explanation:** The first yielded promise immediately rejects. This error is caught. Because the generator hasn't been cancelled, execution continues as usual. It ends up resolving 2 + 2 = 4.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
Wraps the generator execution in a promise. Maintains a reference to allow cancellation. When `cancel()` is called, it throws an error into the generator via `generator.throw()`, causing the generator to reject.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `generatorFunction = function*() { 
 return 42; 
}
cancelledAt = 100`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `{"resolved": 42}`.
4. **Verification:** const generator = generatorFunction();
const [cancel, promise] = cancellable(generator);
setTimeout(cancel, 100);
promise.then(console.log); // resolves 42 at t=0ms

The generator immediately yields 42 and finishes. Because of that, the returned promise immediately resolves 42. Note that cancelling a finished generator does nothing.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
TypeScript

## Source Code
- [solution.ts](./solution.ts)


```typescript
function cancellable(
    generator: Generator<Promise<any>, any, any>
): [() => void, Promise<any>] {

    let cancelled = false;
    let finished = false;

    const promise = new Promise<any>((resolve, reject) => {

        function step(
            method: "next" | "throw",
            value?: any
        ): void {

            if (finished) return;

            let result: IteratorResult<any>;

            try {
                result = generator[method](value);
            } catch (error) {
                finished = true;
                reject(error);
                return;
            }

            if (result.done) {
                finished = true;
                resolve(result.value);
                return;
            }

            Promise.resolve(result.value).then(
                (value) => {
                    if (cancelled) {
                        step("throw", "Cancelled");
                    } else {
                        step("next", value);
                    }
                },
                (error) => {
                    step("throw", error);
                }
            );
        }

        step("next");
    });

    const cancel = () => {
        if (!finished) {
            cancelled = true;
        }
    };

    return [cancel, promise];
}
```

## Why This Works
By utilizing **Array / General**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [396. Rotate Function](../../0001-0500/0396-rotate-function/)
- [1521. Find a Value of a Mysterious Function Closest to Target](../../1501-2000/1521-find-a-value-of-a-mysterious-function-closest-to-target/)
- [1558. Minimum Numbers of Function Calls to Make Target Array](../../1501-2000/1558-minimum-numbers-of-function-calls-to-make-target-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/design-cancellable-function/)
