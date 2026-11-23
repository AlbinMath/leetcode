# LeetCode 2631: Group By

**LeetCode Problem #2631 — Group By**
Solve LeetCode Group By using TypeScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Group By |
| LeetCode | #2631 |
| Difficulty | Medium |
| Language | TypeScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Write code that enhances all arrays such that you can call the `array.groupBy(fn)` method on any array and it will return a **grouped** version of the array.

A **grouped** array is an object where each key is the output of `fn(arr[i])` and each value is an array containing all items in the original array which generate that key.

The provided callback `fn` will accept an item in the array and return a string key.

The order of each value list should be the order the items appear in the array. Any order of keys is acceptable.

Please solve it without lodash's `_.groupBy` function.

## Constraints
- `0 <= array.length <= 10^5`
- `fn` returns a string

## Examples
### Example 1
- **Input:** `array = [
 {"id":"1"},
 {"id":"1"},
 {"id":"2"}
], 
fn = function (item) { 
 return item.id; 
}`
- **Output:** `{ 
 "1": [{"id": "1"}, {"id": "1"}], 
 "2": [{"id": "2"}] 
}`
- **Explanation:** Output is from array.groupBy(fn).
The selector function gets the "id" out of each item in the array.
There are two objects with an "id" of 1. Both of those objects are put in the first array.
There is one object with an "id" of 2. That object is put in the second array.

### Example 2
- **Input:** `array = [
 [1, 2, 3],
 [1, 3, 5],
 [1, 5, 9]
]
fn = function (list) { 
 return String(list[0]); 
}`
- **Output:** `{ 
 "1": [[1, 2, 3], [1, 3, 5], [1, 5, 9]] 
}`
- **Explanation:** The array can be of any type. In this case, the selector function defines the key as being the first element in the array. 
All the arrays have 1 as their first element so they are grouped together.
{
 "1": [[1, 2, 3], [1, 3, 5], [1, 5, 9]]
}

### Example 3
- **Input:** `array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
fn = function (n) { 
 return String(n > 5);
}`
- **Output:** `{
 "true": [6, 7, 8, 9, 10],
 "false": [1, 2, 3, 4, 5]
}`
- **Explanation:** The selector function splits the array by whether each number is greater than 5.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
Iterates through the array, applies `fn` to each element to get a key, and builds an object where each key maps to an array of elements that produced that key.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `array = [
 {"id":"1"},
 {"id":"1"},
 {"id":"2"}
], 
fn = function (item) { 
 return item.id; 
}`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `{ 
 "1": [{"id": "1"}, {"id": "1"}], 
 "2": [{"id": "2"}] 
}`.
4. **Verification:** Output is from array.groupBy(fn).
The selector function gets the "id" out of each item in the array.
There are two objects with an "id" of 1. Both of those objects are put in the first array.
There is one object with an "id" of 2. That object is put in the second array.

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
declare global {
    interface Array<T> {
        groupBy(fn: (item: T) => string): Record<string, T[]>;
    }
}

Array.prototype.groupBy = function<T>(
    fn: (item: T) => string
): Record<string, T[]> {
    const result: Record<string, T[]> = {};

    for (const item of this) {
        const key = fn(item);

        if (!result[key]) {
            result[key] = [];
        }

        result[key].push(item);
    }

    return result;
};
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
- [25. Reverse Nodes in k-Group](../../0001-0500/0025-reverse-nodes-in-k-group/)
- [49. Group Anagrams](../../0001-0500/0049-group-anagrams/)
- [1399. Count Largest Group](../../1001-1500/1500-count-largest-group/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/group-by/)
