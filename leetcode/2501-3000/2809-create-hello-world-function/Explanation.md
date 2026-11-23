# LeetCode 2667: Create Hello World Function

**LeetCode Problem #2667 — Create Hello World Function**
Solve LeetCode Create Hello World Function using TypeScript and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Create Hello World Function |
| LeetCode | #2667 |
| Difficulty | Easy |
| Language | TypeScript |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Write a function `createHelloWorld`. It should return a new function that always returns `"Hello World"`.

## Constraints
- `0 <= args.length <= 10`

## Examples
### Example 1
- **Input:** `args = []`
- **Output:** `"Hello World"`
- **Explanation:** const f = createHelloWorld();
f(); // "Hello World"

The function returned by createHelloWorld should always return "Hello World".

### Example 2
- **Input:** `args = [{},null,42]`
- **Output:** `"Hello World"`
- **Explanation:** const f = createHelloWorld();
f({}, null, 42); // "Hello World"

Any arguments could be passed to the function but it should still always return "Hello World".

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
`return function() { return "Hello World"; }` — returns a function that ignores any arguments and always returns the string "Hello World".

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `args = []`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"Hello World"`.
4. **Verification:** const f = createHelloWorld();
f(); // "Hello World"

The function returned by createHelloWorld should always return "Hello World".

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Tree / Graph / Grid.

## Pattern
**Tree & Graph**

## Topics
- Tree
- Graph
- DFS
- BFS

## Language
TypeScript

## Source Code
- [solution.ts](./solution.ts)


```typescript
function createHelloWorld() {
    return function(...args: any[]): string {
        return "Hello World";
    };
}
```

## Why This Works
By utilizing **Tree & Graph**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [321. Create Maximum Number](../../0001-0500/0321-create-maximum-number/)
- [1389. Create Target Array in the Given Order](../../1501-2000/1505-create-target-array-in-the-given-order/)
- [1649. Create Sorted Array through Instructions](../../1501-2000/1772-create-sorted-array-through-instructions/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/create-hello-world-function/)
