# LeetCode 2695: Array Wrapper

**LeetCode Problem #2695 — Array Wrapper**
Solve LeetCode Array Wrapper using TypeScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Array Wrapper |
| LeetCode | #2695 |
| Difficulty | Easy |
| Language | TypeScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Create a class `ArrayWrapper` that accepts an array of integers in its constructor. This class should have two features:

When two instances of this class are added together with the `+` operator, the resulting value is the sum of all the elements in both arrays. 
 When the `String()` function is called on the instance, it will return a comma separated string surrounded by brackets. For example, `[1,2,3]`.

## Constraints
- `0 <= nums.length <= 1000`
- `0 <= nums[i] <= 1000`
- `Note: nums is the array passed to the constructor`

## Examples
### Example 1
- **Input:** `nums = [[1,2],[3,4]], operation = "Add"`
- **Output:** `10`
- **Explanation:** const obj1 = new ArrayWrapper([1,2]);
const obj2 = new ArrayWrapper([3,4]);
obj1 + obj2; // 10

### Example 2
- **Input:** `nums = [[23,98,42,70]], operation = "String"`
- **Output:** `"[23,98,42,70]"`
- **Explanation:** const obj = new ArrayWrapper([23,98,42,70]);
String(obj); // "[23,98,42,70]"

### Example 3
- **Input:** `nums = [[],[]], operation = "Add"`
- **Output:** `0`
- **Explanation:** const obj1 = new ArrayWrapper([]);
const obj2 = new ArrayWrapper([]);
obj1 + obj2; // 0

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
Override `valueOf()` to return the sum of the internal array (used by `+` operator) and `toString()` to return `"[elements]"` format.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [[1,2],[3,4]], operation = "Add"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `10`.
4. **Verification:** const obj1 = new ArrayWrapper([1,2]);
const obj2 = new ArrayWrapper([3,4]);
obj1 + obj2; // 10

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
class ArrayWrapper {
    nums: number[];

    constructor(nums: number[]) {
        this.nums = nums;
    }

    valueOf(): number {
        return this.nums.reduce((sum, num) => sum + num, 0);
    }

    toString(): string {
        return `[${this.nums.join(",")}]`;
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
- [26. Remove Duplicates from Sorted Array](../../0001-0500/0026-remove-duplicates-from-sorted-array/)
- [33. Search in Rotated Sorted Array](../../0001-0500/0033-search-in-rotated-sorted-array/)
- [34. Find First and Last Position of Element in Sorted Array](../../0001-0500/0034-find-first-and-last-position-of-element-in-sorted-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/array-wrapper/)
