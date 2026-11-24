# LeetCode 2727: Is Object Empty

**LeetCode Problem #2727 — Is Object Empty**
Solve LeetCode Is Object Empty using TypeScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Is Object Empty |
| LeetCode | #2727 |
| Difficulty | Easy |
| Language | TypeScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an object or an array, return if it is empty.

An empty object contains no key-value pairs. 
 An empty array contains no elements.

You may assume the object or array is the output of `JSON.parse`.

## Constraints
- `obj` is a valid JSON object or array
- `2 <= JSON.stringify(obj).length <= 10^5`

## Examples
### Example 1
- **Input:** `obj = {"x": 5, "y": 42}`
- **Output:** `false`
- **Explanation:** The object has 2 key-value pairs so it is not empty.

### Example 2
- **Input:** `obj = {}`
- **Output:** `true`
- **Explanation:** The object doesn't have any key-value pairs so it is empty.

### Example 3
- **Input:** `obj = [null, false, 0]`
- **Output:** `false`
- **Explanation:** The array has 3 elements so it is not empty.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
For arrays: `arr.length === 0`. For objects: `Object.keys(obj).length === 0`. Checks if there are any enumerable properties.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `obj = {"x": 5, "y": 42}`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `false`.
4. **Verification:** The object has 2 key-value pairs so it is not empty.

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
type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };

type Obj = Record<string, JSONValue> | JSONValue[];

function isEmpty(obj: Obj): boolean {
    return Object.keys(obj).length === 0;
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
- [2618. Check if Object Instance of Class](../../2501-3000/2618-check-if-object-instance-of-class/)
- [2705. Compact Object](../../2501-3000/2705-compact-object/)
- [2659. Make Array Empty](../../2501-3000/2659-make-array-empty/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/is-object-empty/)
