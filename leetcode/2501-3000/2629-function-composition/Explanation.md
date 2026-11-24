# LeetCode 2629: Function Composition

**LeetCode Problem #2629 — Function Composition**
Solve LeetCode Function Composition using TypeScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Function Composition |
| LeetCode | #2629 |
| Difficulty | Easy |
| Language | TypeScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an array of functions `[f 1 , f_2, f_3, ..., f_n]`, return a new function `fn` that is the **function composition** of the array of functions.

The **function composition** of `[f(x), g(x), h(x)]` is `fn(x) = f(g(h(x)))`.

The **function composition** of an empty list of functions is the **identity function** `f(x) = x`.

You may assume each function in the array accepts one integer as input and returns one integer as output.

## Constraints
- ` -1000 <= x <= 1000 `
- ` 0 <= functions.length <= 1000 `
- all functions accept and return a single integer

## Examples
### Example 1
- **Input:** `functions = [x => x + 1, x => x * x, x => 2 * x], x = 4`
- **Output:** `65`
- **Explanation:** Evaluating from right to left ...
Starting with x = 4.
2 * (4) = 8
(8) * (8) = 64
(64) + 1 = 65

### Example 2
- **Input:** `functions = [x => 10 * x, x => 10 * x, x => 10 * x], x = 1`
- **Output:** `1000`
- **Explanation:** Evaluating from right to left ...
10 * (1) = 10
10 * (10) = 100
10 * (100) = 1000

### Example 3
- **Input:** `functions = [], x = 42`
- **Output:** `42`
- **Explanation:** The composition of zero functions is the identity function

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
Uses `Array.reduceRight` to apply functions from right to left. The composed function takes input `x`, passes it through the last function first, then feeds each result to the previous function.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `functions = [x => x + 1, x => x * x, x => 2 * x], x = 4`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `65`.
4. **Verification:** Evaluating from right to left ...
Starting with x = 4.
2 * (4) = 8
(8) * (8) = 64
(64) + 1 = 65

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
function compose(functions: ((x: number) => number)[]): (x: number) => number {
    return function (x: number): number {
        for (let i = functions.length - 1; i >= 0; i--) {
            x = functions[i](x);
        }
        return x;
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
- [396. Rotate Function](../../0001-0500/0396-rotate-function/)
- [1521. Find a Value of a Mysterious Function Closest to Target](../../1501-2000/1521-find-a-value-of-a-mysterious-function-closest-to-target/)
- [1558. Minimum Numbers of Function Calls to Make Target Array](../../1501-2000/1558-minimum-numbers-of-function-calls-to-make-target-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/function-composition/)
