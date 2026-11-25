# LeetCode 2648: Generate Fibonacci Sequence

**LeetCode Problem #2648 — Generate Fibonacci Sequence**
Solve LeetCode Generate Fibonacci Sequence using TypeScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Generate Fibonacci Sequence |
| LeetCode | #2648 |
| Difficulty | Easy |
| Language | TypeScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Write a generator function that returns a generator object which yields the **fibonacci sequence**.

The **fibonacci sequence** is defined by the relation `X_n = X_n-1 + X_n-2`.

The first few numbers of the series are `0, 1, 1, 2, 3, 5, 8, 13`.

## Constraints
- `0 <= callCount <= 50`

## Examples
### Example 1
- **Input:** `callCount = 5`
- **Output:** `[0,1,1,2,3]`
- **Explanation:** const gen = fibGenerator();
gen.next().value; // 0
gen.next().value; // 1
gen.next().value; // 1
gen.next().value; // 2
gen.next().value; // 3

### Example 2
- **Input:** `callCount = 0`
- **Output:** `[]`
- **Explanation:** gen.next() is never called so nothing is outputted

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
Uses a generator function (`function*`) that maintains two variables `a` and `b`. In an infinite loop, it `yield`s `a`, then updates: `[a, b] = [b, a + b]`.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `callCount = 5`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[0,1,1,2,3]`.
4. **Verification:** const gen = fibGenerator();
gen.next().value; // 0
gen.next().value; // 1
gen.next().value; // 1
gen.next().value; // 2
gen.next().value; // 3

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
function* fibGenerator(): Generator<number> {
    let a = 0;
    let b = 1;

    while (true) {
        yield a;

        [a, b] = [b, a + b];
    }
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
- [842. Split Array into Fibonacci Sequence](../../0501-1000/0842-split-array-into-fibonacci-sequence/)
- [22. Generate Parentheses](../../0001-0500/0022-generate-parentheses/)
- [478. Generate Random Point in a Circle](../../0001-0500/0478-generate-random-point-in-a-circle/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/generate-fibonacci-sequence/)
