# LeetCode 2722: Join Two Arrays by ID

**LeetCode Problem #2722 — Join Two Arrays by ID**
Solve LeetCode Join Two Arrays by ID using TypeScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Join Two Arrays by ID |
| LeetCode | #2722 |
| Difficulty | Medium |
| Language | TypeScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given two arrays `arr1` and `arr2`, return a new array `joinedArray`. All the objects in each of the two inputs arrays will contain an `id` field that has an integer value.

`joinedArray` is an array formed by merging `arr1` and `arr2` based on their `id` key. The length of `joinedArray` should be the length of unique values of `id`. The returned array should be sorted in **ascending** order based on the `id` key.

If a given `id` exists in one array but not the other, the single object with that `id` should be included in the result array without modification.

If two objects share an `id`, their properties should be merged into a single object:

If a key only exists in one object, that single key-value pair should be included in the object. 
 If a key is included in both objects, the value in the object from `arr2` should override the value from `arr1`.

## Constraints
- `arr1` and `arr2` are valid JSON arrays
- Each object in `arr1` and `arr2` has a unique integer `id` key
- `2 <= JSON.stringify(arr1).length <= 10^6`
- `2 <= JSON.stringify(arr2).length <= 10^6`

## Examples
### Example 1
- **Input:** `arr1 = [
 {"id": 1, "x": 1},
 {"id": 2, "x": 9}
], 
arr2 = [
 {"id": 3, "x": 5}
]`
- **Output:** `[
 {"id": 1, "x": 1},
 {"id": 2, "x": 9},
 {"id": 3, "x": 5}
]`
- **Explanation:** There are no duplicate ids so arr1 is simply concatenated with arr2.

### Example 2
- **Input:** `arr1 = [
 {"id": 1, "x": 2, "y": 3},
 {"id": 2, "x": 3, "y": 6}
], 
arr2 = [
 {"id": 2, "x": 10, "y": 20},
 {"id": 3, "x": 0, "y": 0}
]`
- **Output:** `[
 {"id": 1, "x": 2, "y": 3},
 {"id": 2, "x": 10, "y": 20},
 {"id": 3, "x": 0, "y": 0}
]`
- **Explanation:** The two objects with id=1 and id=3 are included in the result array without modifiction. The two objects with id=2 are merged together. The keys from arr2 override the values in arr1.

### Example 3
- **Input:** `arr1 = [
 {"id": 1, "b": {"b": 94},"v": [4, 3], "y": 48}
]
arr2 = [
 {"id": 1, "b": {"c": 84}, "v": [1, 3]}
]`
- **Output:** `[
 {"id": 1, "b": {"c": 84}, "v": [1, 3], "y": 48}
]`
- **Explanation:** The two objects with id=1 are merged together. For the keys "b" and "v" the values from arr2 are used. Since the key "y" only exists in arr1, that value is taken form arr1.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
Uses a Map keyed by id. First insert all objects from arr1, then merge/override with objects from arr2 using `Object.assign` or spread. Sort the result by id.

## Algorithm
1. Initialize state variables / data structure (**Dictionary / Hash Map**).
2. Process elements sequentially using **Complement Lookup / Hash Table Frequency**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `arr1 = [
 {"id": 1, "x": 1},
 {"id": 2, "x": 9}
], 
arr2 = [
 {"id": 3, "x": 5}
]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[
 {"id": 1, "x": 1},
 {"id": 2, "x": 9},
 {"id": 3, "x": 5}
]`.
4. **Verification:** There are no duplicate ids so arr1 is simply concatenated with arr2.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Dictionary / Hash Map.

## Pattern
**Hash Map**

## Topics
- Hash Table
- Array
- Complement Lookup

## Language
TypeScript

## Source Code
- [solution.ts](./solution.ts)


```typescript
function join(arr1: any[], arr2: any[]): any[] {
    const map = new Map<number, any>();

    // Add all objects from arr1
    for (const obj of arr1) {
        map.set(obj.id, { ...obj });
    }

    // Merge arr2 into arr1
    for (const obj of arr2) {
        if (map.has(obj.id)) {
            map.set(obj.id, {
                ...map.get(obj.id),
                ...obj
            });
        } else {
            map.set(obj.id, { ...obj });
        }
    }

    // Sort by id
    return Array.from(map.values()).sort((a, b) => a.id - b.id);
}
```

## Why This Works
By utilizing **Hash Map**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Using the same element twice.
2. Checking the map before inserting elements in the correct order.
3. Inefficient hash functions or unnecessary duplicate key updates.

## Interview Notes
- **Tests:** Hash map usage, complement/frequency lookup, and $O(n)$ time optimization.
- **Follow-up:** Can you solve the problem in $O(1)$ extra space if the input array is sorted?

## Related Problems
- [4. Median of Two Sorted Arrays](../../0001-0500/0004-median-of-two-sorted-arrays/)
- [349. Intersection of Two Arrays](../../0001-0500/0349-intersection-of-two-arrays/)
- [350. Intersection of Two Arrays II](../../0001-0500/0350-intersection-of-two-arrays-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/join-two-arrays-by-id/)
