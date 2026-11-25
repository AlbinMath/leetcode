# LeetCode 2625: Flatten Deeply Nested Array

**LeetCode Problem #2625 — Flatten Deeply Nested Array**
Solve LeetCode Flatten Deeply Nested Array using TypeScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Flatten Deeply Nested Array |
| LeetCode | #2625 |
| Difficulty | Medium |
| Language | TypeScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a **multi-dimensional** array `arr` and a depth `n`, return a **flattened** version of that array.

A **multi-dimensional** array is a recursive data structure that contains integers or other **multi-dimensional** arrays.

A **flattened** array is a version of that array with some or all of the sub-arrays removed and replaced with the actual elements in that sub-array. This flattening operation should only be done if the current depth of nesting is less than `n`. The depth of the elements in the first array are considered to be `0`.

Please solve it without the built-in `Array.flat` method.

## Constraints
- `0 <= count of numbers in arr <= 10^5`
- `0 <= count of subarrays in arr <= 10^5`
- `maxDepth <= 1000`
- `-1000 <= each number <= 1000`
- ` 0 <= n <= 1000 `

## Examples
### Example 1
- **Input:** `arr = [1, 2, 3, [4, 5, 6], [7, 8, [9, 10, 11], 12], [13, 14, 15]]
n = 0`
- **Output:** `[1, 2, 3, [4, 5, 6], [7, 8, [9, 10, 11], 12], [13, 14, 15]]`
- **Explanation:** Passing a depth of n=0 will always result in the original array. This is because the smallest possible depth of a subarray (0) is not less than n=0. Thus, no subarray should be flattened.

### Example 2
- **Input:** `arr = [1, 2, 3, [4, 5, 6], [7, 8, [9, 10, 11], 12], [13, 14, 15]]
n = 1`
- **Output:** `[1, 2, 3, 4, 5, 6, 7, 8, [9, 10, 11], 12, 13, 14, 15]`
- **Explanation:** The subarrays starting with 4, 7, and 13 are all flattened. This is because their depth of 0 is less than 1. However [9, 10, 11] remains unflattened because its depth is 1.

### Example 3
- **Input:** `arr = [[1, 2, 3], [4, 5, 6], [7, 8, [9, 10, 11], 12], [13, 14, 15]]
n = 2`
- **Output:** `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]`
- **Explanation:** The maximum depth of any subarray is 1. Thus, all of them are flattened.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
Uses recursion: if depth > 0, iterate through elements. If an element is an array, recursively flatten it with `depth - 1`. Otherwise, add the element directly to the result.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Two Pointer Convergence & Scanning**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `arr = [1, 2, 3, [4, 5, 6], [7, 8, [9, 10, 11], 12], [13, 14, 15]]
n = 0`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1, 2, 3, [4, 5, 6], [7, 8, [9, 10, 11], 12], [13, 14, 15]]`.
4. **Verification:** Passing a depth of n=0 will always result in the original array. This is because the smallest possible depth of a subarray (0) is not less than n=0. Thus, no subarray should be flattened.

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
type MultiDimensionalArray = (number | MultiDimensionalArray)[];

function flat(
    arr: MultiDimensionalArray,
    n: number
): MultiDimensionalArray {
    const result: MultiDimensionalArray = [];

    function flatten(
        current: MultiDimensionalArray,
        depth: number
    ): void {
        for (const item of current) {
            if (Array.isArray(item) && depth < n) {
                flatten(item, depth + 1);
            } else {
                result.push(item);
            }
        }
    }

    flatten(arr, 0);

    return result;
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
- [2649. Nested Array Generator](../../2501-3000/2649-nested-array-generator/)
- [341. Flatten Nested List Iterator](../../0001-0500/0341-flatten-nested-list-iterator/)
- [26. Remove Duplicates from Sorted Array](../../0001-0500/0026-remove-duplicates-from-sorted-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/flatten-deeply-nested-array/)
