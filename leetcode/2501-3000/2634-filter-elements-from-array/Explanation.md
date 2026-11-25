# LeetCode 2634: Filter Elements from Array

**LeetCode Problem #2634 — Filter Elements from Array**
Solve LeetCode Filter Elements from Array using TypeScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Filter Elements from Array |
| LeetCode | #2634 |
| Difficulty | Easy |
| Language | TypeScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an integer array `arr` and a filtering function `fn`, return a filtered array `filteredArr`.

The `fn` function takes one or two arguments:

`arr[i]` - number from the `arr` 
 `i` - index of `arr[i]`

`filteredArr` should only contain the elements from the `arr` for which the expression `fn(arr[i], i)` evaluates to a **truthy** value. A **truthy** value is a value where `Boolean(value)` returns `true`.

Please solve it without the built-in `Array.filter` method.

## Constraints
- `0 <= arr.length <= 1000`
- `-10^9 <= arr[i] <= 10^9`

## Examples
### Example 1
- **Input:** `arr = [0,10,20,30], fn = function greaterThan10(n) { return n > 10; }`
- **Output:** `[20,30]`
- **Explanation:** const newArray = filter(arr, fn); // [20, 30]
The function filters out values that are not greater than 10

### Example 2
- **Input:** `arr = [1,2,3], fn = function firstIndex(n, i) { return i === 0; }`
- **Output:** `[1]`
- **Explanation:** fn can also accept the index of each element
In this case, the function removes elements not at index 0

### Example 3
- **Input:** `arr = [-2,-1,0,1,2], fn = function plusOne(n) { return n + 1 }`
- **Output:** `[-2,0,1,2]`
- **Explanation:** Falsey values such as 0 should be filtered out

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
Iterates through the array, calls `fn(arr[i], i)` for each element, and pushes elements to the result array when the callback returns a truthy value.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `arr = [0,10,20,30], fn = function greaterThan10(n) { return n > 10; }`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[20,30]`.
4. **Verification:** const newArray = filter(arr, fn); // [20, 30]
The function filters out values that are not greater than 10

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
function filter(
    arr: number[],
    fn: (n: number, i: number) => any
): number[] {
    const result: number[] = [];

    for (let i = 0; i < arr.length; i++) {
        if (fn(arr[i], i)) {
            result.push(arr[i]);
        }
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
- [80. Remove Duplicates from Sorted Array II](../../0001-0500/0080-remove-duplicates-from-sorted-array-ii/)
- [453. Minimum Moves to Equal Array Elements](../../0001-0500/0453-minimum-moves-to-equal-array-elements/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/filter-elements-from-array/)
