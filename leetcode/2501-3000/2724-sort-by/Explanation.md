# LeetCode 2724: Sort By

**LeetCode Problem #2724 — Sort By**
Solve LeetCode Sort By using TypeScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Sort By |
| LeetCode | #2724 |
| Difficulty | Easy |
| Language | TypeScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an array `arr` and a function `fn`, return a sorted array `sortedArr`. You can assume `fn` only returns numbers and those numbers determine the sort order of `sortedArr`. `sortedArr` must be sorted in **ascending order** by `fn` output.

You may assume that `fn` will never duplicate numbers for a given array.

## Constraints
- `arr` is a valid JSON array
- `fn` is a function that returns a number
- `1 <= arr.length <= 5 * 10^5`

## Examples
### Example 1
- **Input:** `arr = [5, 4, 1, 2, 3], fn = (x) => x`
- **Output:** `[1, 2, 3, 4, 5]`
- **Explanation:** fn simply returns the number passed to it so the array is sorted in ascending order.

### Example 2
- **Input:** `arr = [{"x": 1}, {"x": 0}, {"x": -1}], fn = (d) => d.x`
- **Output:** `[{"x": -1}, {"x": 0}, {"x": 1}]`
- **Explanation:** fn returns the value for the "x" key. So the array is sorted based on that value.

### Example 3
- **Input:** `arr = [[3, 4], [5, 2], [10, 1]], fn = (x) => x[1]`
- **Output:** `[[10, 1], [5, 2], [3, 4]]`
- **Explanation:** arr is sorted in ascending order by number at index=1.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
`arr.sort((a, b) => fn(a) - fn(b))` — uses the built-in sort with a comparator that compares the return values of `fn` applied to each element.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `arr = [5, 4, 1, 2, 3], fn = (x) => x`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1, 2, 3, 4, 5]`.
4. **Verification:** fn simply returns the number passed to it so the array is sorted in ascending order.

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
function sortBy<T>(arr: T[], fn: (x: T) => number): T[] {
    return arr.sort((a, b) => fn(a) - fn(b));
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
- [75. Sort Colors](../../0001-0500/0075-sort-colors/)
- [147. Insertion Sort List](../../0001-0500/0147-insertion-sort-list/)
- [148. Sort List](../../0001-0500/0148-sort-list/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/sort-by/)
