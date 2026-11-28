# LeetCode 2635: Apply Transform Over Each Element in Array

**LeetCode Problem #2635 — Apply Transform Over Each Element in Array**
Solve LeetCode Apply Transform Over Each Element in Array using TypeScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Apply Transform Over Each Element in Array |
| LeetCode | #2635 |
| Difficulty | Easy |
| Language | TypeScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given an integer array `arr` and a mapping function `fn`, return a new array with a transformation applied to each element.

The returned array should be created such that `returnedArray[i] = fn(arr[i], i)`.

Please solve it without the built-in `Array.map` method.

## Constraints
- `0 <= arr.length <= 1000`
- ` -10^9 <= arr[i] <= 10^9 `
- `fn` returns an integer.

## Examples
### Example 1
- **Input:** `arr = [1,2,3], fn = function plusone(n) { return n + 1; }`
- **Output:** `[2,3,4]`
- **Explanation:** const newArray = map(arr, plusone); // [2,3,4]
The function increases each value in the array by one.

### Example 2
- **Input:** `arr = [1,2,3], fn = function plusI(n, i) { return n + i; }`
- **Output:** `[1,3,5]`
- **Explanation:** The function increases each value by the index it resides in.

### Example 3
- **Input:** `arr = [10,20,30], fn = function constant() { return 42; }`
- **Output:** `[42,42,42]`
- **Explanation:** The function always returns 42.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
Iterates through the array, applies `fn(arr[i], i)` to each element, and pushes the transformed value to the result array.

## Algorithm
1. Initialize state variables / data structure (**Dictionary / Hash Map**).
2. Process elements sequentially using **Complement Lookup / Hash Table Frequency**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `arr = [1,2,3], fn = function plusone(n) { return n + 1; }`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[2,3,4]`.
4. **Verification:** const newArray = map(arr, plusone); // [2,3,4]
The function increases each value in the array by one.

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
function map(
    arr: number[],
    fn: (n: number, i: number) => number
): number[] {
    const result: number[] = [];

    for (let i = 0; i < arr.length; i++) {
        result.push(fn(arr[i], i));
    }

    return result;
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
- [1331. Rank Transform of an Array](../../1001-1500/1331-rank-transform-of-an-array/)
- [3467. Transform Array by Parity](../../3001-3500/3467-transform-array-by-parity/)
- [3576. Transform Array to All Equal Elements](../../3501-4000/3576-transform-array-to-all-equal-elements/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/apply-transform-over-each-element-in-array/)
