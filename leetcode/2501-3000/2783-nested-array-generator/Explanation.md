# LeetCode 2649: Nested Array Generator

**LeetCode Problem #2649 — Nested Array Generator**
Solve LeetCode Nested Array Generator using TypeScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Nested Array Generator |
| LeetCode | #2649 |
| Difficulty | Medium |
| Language | TypeScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a **multi-dimensional array** of integers, return a generator object which yields integers in the same order as **inorder traversal**.

A **multi-dimensional array** is a recursive data structure that contains both integers and other **multi-dimensional arrays**.

**inorder traversal** iterates over each array from left to right, yielding any integers it encounters or applying **inorder traversal** to any arrays it encounters.

## Constraints
- `0 <= arr.flat().length <= 10^5`
- `0 <= arr.flat()[i] <= 10^5`
- `maxNestingDepth <= 10^5`

## Examples
### Example 1
- **Input:** `arr = [[[6]],[1,3],[]]`
- **Output:** `[6,1,3]`
- **Explanation:** const generator = inorderTraversal(arr);
generator.next().value; // 6
generator.next().value; // 1
generator.next().value; // 3
generator.next().done; // true

### Example 2
- **Input:** `arr = []`
- **Output:** `[]`
- **Explanation:** There are no integers so the generator doesn't yield anything.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
Uses a recursive generator: for each element, if it's an array, `yield*` the recursive call on that sub-array. Otherwise, `yield` the element directly. This lazily flattens the nested structure.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `arr = [[[6]],[1,3],[]]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[6,1,3]`.
4. **Verification:** const generator = inorderTraversal(arr);
generator.next().value; // 6
generator.next().value; // 1
generator.next().value; // 3
generator.next().done; // true

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
type MultiDimensionalArray = (number | MultiDimensionalArray)[];

function* inorderTraversal(
    arr: MultiDimensionalArray
): Generator<number> {

    for (const item of arr) {
        if (Array.isArray(item)) {
            yield* inorderTraversal(item);
        } else {
            yield item;
        }
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
- [2625. Flatten Deeply Nested Array](../../2501-3000/2759-flatten-deeply-nested-array/)
- [26. Remove Duplicates from Sorted Array](../../0001-0500/0026-remove-duplicates-from-sorted-array/)
- [33. Search in Rotated Sorted Array](../../0001-0500/0033-search-in-rotated-sorted-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/nested-array-generator/)
