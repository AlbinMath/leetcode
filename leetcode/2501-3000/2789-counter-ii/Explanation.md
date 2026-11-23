# LeetCode 2665: Counter II

**LeetCode Problem #2665 — Counter II**
Solve LeetCode Counter II using TypeScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Counter II |
| LeetCode | #2665 |
| Difficulty | Easy |
| Language | TypeScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Write a function `createCounter`. It should accept an initial integer `init`. It should return an object with three functions.

The three functions are:

`increment()` increases the current value by 1 and then returns it. 
 `decrement()` reduces the current value by 1 and then returns it. 
 `reset()` sets the current value to `init` and then returns it.

## Constraints
- `-1000 <= init <= 1000`
- `0 <= calls.length <= 1000`
- `calls[i]` is one of "increment", "decrement" and "reset"

## Examples
### Example 1
- **Input:** `init = 5, calls = ["increment","reset","decrement"]`
- **Output:** `[6,5,4]`
- **Explanation:** const counter = createCounter(5);
counter.increment(); // 6
counter.reset(); // 5
counter.decrement(); // 4

### Example 2
- **Input:** `init = 0, calls = ["increment","increment","decrement","reset","reset"]`
- **Output:** `[1,2,1,0,0]`
- **Explanation:** const counter = createCounter(0);
counter.increment(); // 1
counter.increment(); // 2
counter.decrement(); // 1
counter.reset(); // 0
counter.reset(); // 0

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
Uses a closure to capture `init` and a mutable `count` variable. `increment` returns `++count`, `decrement` returns `--count`, and `reset` sets `count = init` and returns it.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `init = 5, calls = ["increment","reset","decrement"]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[6,5,4]`.
4. **Verification:** const counter = createCounter(5);
counter.increment(); // 6
counter.reset(); // 5
counter.decrement(); // 4

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
function createCounter(init: number) {
    let current = init;

    return {
        increment() {
            current++;
            return current;
        },

        decrement() {
            current--;
            return current;
        },

        reset() {
            current = init;
            return current;
        }
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
- [2620. Counter](../../2501-3000/2732-counter/)
- [5. Longest Palindromic Substring](../../0001-0500/0005-longest-palindromic-substring/)
- [26. Remove Duplicates from Sorted Array](../../0001-0500/0026-remove-duplicates-from-sorted-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/counter-ii/)
