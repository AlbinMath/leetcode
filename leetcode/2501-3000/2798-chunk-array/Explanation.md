# LeetCode 2677: Chunk Array

**LeetCode Problem #2677 — Chunk Array**
Solve LeetCode Chunk Array using TypeScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Chunk Array |
| LeetCode | #2677 |
| Difficulty | Easy |
| Language | TypeScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an array `arr` and a chunk size `size`, return a **chunked** array.

A **chunked** array contains the original elements in `arr`, but consists of subarrays each of length `size`. The length of the last subarray may be less than `size` if `arr.length` is not evenly divisible by `size`.

Please solve it without using lodash's `_.chunk` function.

## Constraints
- `arr` is a string representing the array.
- `2 <= arr.length <= 10^5`
- `1 <= size <= arr.length + 1`

## Examples
### Example 1
- **Input:** `arr = [1,2,3,4,5], size = 1`
- **Output:** `[[1],[2],[3],[4],[5]]`
- **Explanation:** The arr has been split into subarrays each with 1 element.

### Example 2
- **Input:** `arr = [1,9,6,3,2], size = 3`
- **Output:** `[[1,9,6],[3,2]]`
- **Explanation:** The arr has been split into subarrays with 3 elements. However, only two elements are left for the 2nd subarray.

### Example 3
- **Input:** `arr = [8,5,3,2,6], size = 6`
- **Output:** `[[8,5,3,2,6]]`
- **Explanation:** Size is greater than arr.length thus all elements are in the first subarray.

### Example 4
- **Input:** `arr = [], size = 1`
- **Output:** `[]`
- **Explanation:** There are no elements to be chunked so an empty array is returned.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
Iterates through the array in steps of `size`, slicing `arr.slice(i, i + size)` for each chunk and pushing it to the result.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `arr = [1,2,3,4,5], size = 1`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[[1],[2],[3],[4],[5]]`.
4. **Verification:** The arr has been split into subarrays each with 1 element.

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
function chunk(arr: any[], size: number): any[][] {
    const result: any[][] = [];

    for (let i = 0; i < arr.length; i += size) {
        result.push(arr.slice(i, i + size));
    }

    return result;
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
- [26. Remove Duplicates from Sorted Array](../../0001-0500/0026-remove-duplicates-from-sorted-array/)
- [33. Search in Rotated Sorted Array](../../0001-0500/0033-search-in-rotated-sorted-array/)
- [34. Find First and Last Position of Element in Sorted Array](../../0001-0500/0034-find-first-and-last-position-of-element-in-sorted-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/chunk-array/)
