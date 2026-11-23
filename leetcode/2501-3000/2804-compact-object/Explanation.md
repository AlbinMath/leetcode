# LeetCode 2705: Compact Object

**LeetCode Problem #2705 — Compact Object**
Solve LeetCode Compact Object using TypeScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Compact Object |
| LeetCode | #2705 |
| Difficulty | Medium |
| Language | TypeScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an object or array `obj`, return a **compact object**.

A **compact object** is the same as the original object, except with keys containing **falsy** values removed. This operation applies to the object and any nested objects. Arrays are considered objects where the indices are keys. A value is considered **falsy** when `Boolean(value)` returns `false`.

You may assume the `obj` is the output of `JSON.parse`. In other words, it is valid JSON.

## Constraints
- `obj` is a valid JSON object
- `2 <= JSON.stringify(obj).length <= 10^6`

## Examples
### Example 1
- **Input:** `obj = [null, 0, false, 1]`
- **Output:** `[1]`
- **Explanation:** All falsy values have been removed from the array.

### Example 2
- **Input:** `obj = {"a": null, "b": [false, 1]}`
- **Output:** `{"b": [1]}`
- **Explanation:** obj["a"] and obj["b"][0] had falsy values and were removed.

### Example 3
- **Input:** `obj = [null, 0, 5, [0], [false, 16]]`
- **Output:** `[5, [], [16]]`
- **Explanation:** obj[0], obj[1], obj[3][0], and obj[4][0] were falsy and removed.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
Recursively traverses the object. For arrays, filters out falsy values and recurses on each element. For objects, iterates entries, keeps only truthy values, and recurses on nested structures.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `obj = [null, 0, false, 1]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1]`.
4. **Verification:** All falsy values have been removed from the array.

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
type JSONValue =
    | null
    | boolean
    | number
    | string
    | JSONValue[]
    | { [key: string]: JSONValue };

function compactObject(obj: JSONValue): JSONValue {
    // Handle arrays
    if (Array.isArray(obj)) {
        return obj
            .filter(Boolean)
            .map((item) => compactObject(item));
    }

    // Handle objects
    if (typeof obj === "object" && obj !== null) {
        const result: { [key: string]: JSONValue } = {};

        for (const key in obj) {
            if (Boolean(obj[key])) {
                result[key] = compactObject(obj[key]);
            }
        }

        return result;
    }

    // Primitive truthy values
    return obj;
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
- [2618. Check if Object Instance of Class](../../2501-3000/2758-check-if-object-instance-of-class/)
- [2727. Is Object Empty](../../2501-3000/2864-is-object-empty/)
- [5. Longest Palindromic Substring](../../0001-0500/0005-longest-palindromic-substring/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/compact-object/)
