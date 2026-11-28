# LeetCode 2666: Allow One Function Call

**LeetCode Problem #2666 — Allow One Function Call**
Solve LeetCode Allow One Function Call using TypeScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Allow One Function Call |
| LeetCode | #2666 |
| Difficulty | Easy |
| Language | TypeScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a function `fn`, return a new function that is identical to the original function except that it ensures `fn` is called at most once.

The first time the returned function is called, it should return the same result as `fn`. 
 Every subsequent time it is called, it should return `undefined`.

## Constraints
- `calls` is a valid JSON array
- `1 <= calls.length <= 10`
- `1 <= calls[i].length <= 100`
- `2 <= JSON.stringify(calls).length <= 1000`

## Examples
### Example 1
- **Input:** `fn = (a,b,c) => (a + b + c), calls = [[1,2,3],[2,3,6]]`
- **Output:** `[{"calls":1,"value":6}]`
- **Explanation:** const onceFn = once(fn);
onceFn(1, 2, 3); // 6
onceFn(2, 3, 6); // undefined, fn was not called

### Example 2
- **Input:** `fn = (a,b,c) => (a * b * c), calls = [[5,7,4],[2,3,6],[4,6,8]]`
- **Output:** `[{"calls":1,"value":140}]`
- **Explanation:** const onceFn = once(fn);
onceFn(5, 7, 4); // 140
onceFn(2, 3, 6); // undefined, fn was not called
onceFn(4, 6, 8); // undefined, fn was not called

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
Uses a boolean flag `called` in a closure. On the first call, sets `called = true` and returns the function's result. On subsequent calls, returns `undefined`.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `fn = (a,b,c) => (a + b + c), calls = [[1,2,3],[2,3,6]]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[{"calls":1,"value":6}]`.
4. **Verification:** const onceFn = once(fn);
onceFn(1, 2, 3); // 6
onceFn(2, 3, 6); // undefined, fn was not called

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
function once(fn: Function): Function {
    let called = false;

    return function(...args: any[]) {
        if (called) {
            return undefined;
        }

        called = true;
        return fn(...args);
    };
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
- [2693. Call Function with Custom Context](../../2501-3000/2693-call-function-with-custom-context/)
- [396. Rotate Function](../../0001-0500/0396-rotate-function/)
- [793. Preimage Size of Factorial Zeroes Function](../../0501-1000/0793-preimage-size-of-factorial-zeroes-function/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/allow-one-function-call/)
