# LeetCode 1470: Shuffle the Array

**LeetCode Problem #1470 — Shuffle the Array**
Solve LeetCode Shuffle the Array using TypeScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Shuffle the Array |
| LeetCode | #1470 |
| Difficulty | Easy |
| Language | TypeScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given the array `nums` consisting of `2n` elements in the form `[x_1,x_2,...,x_n,y_1,y_2,...,y_n]`.

*Return the array in the form* `[x_1,y_1,x_2,y_2,...,x_n,y_n]`.

## Constraints
- `1 <= n <= 500`
- `nums.length == 2n`
- `1 <= nums[i] <= 10^3`

## Examples
### Example 1
- **Input:** `nums = [2,5,1,3,4,7], n = 3`
- **Output:** `[2,3,5,4,1,7]`
- **Explanation:** Since x_1=2, x_2=5, x_3=1, y_1=3, y_2=4, y_3=7 then the answer is [2,3,5,4,1,7].

### Example 2
- **Input:** `nums = [1,2,3,4,4,3,2,1], n = 4`
- **Output:** `[1,4,2,3,3,2,4,1]`

### Example 3
- **Input:** `nums = [1,1,2,2], n = 2`
- **Output:** `[1,2,1,2]`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code creates a new result array and interleaves elements from the first half and second half. For index `i` from `0` to `n-1`, it places `nums[i]` at position `2*i` and `nums[n+i]` at position `2*i+1`.

Time complexity is $O(N)$ and space complexity is $O(N)$.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,5,1,3,4,7], n = 3`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[2,3,5,4,1,7]`.
4. **Verification:** Since x_1=2, x_2=5, x_3=1, y_1=3, y_2=4, y_3=7 then the answer is [2,3,5,4,1,7].

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
function shuffle(nums: number[], n: number): number[] {
    const result: number[] = [];

    for (let i = 0; i < n; i++) {
        result.push(nums[i]);
        result.push(nums[i + n]);
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
- [384. Shuffle an Array](../../0001-0500/0384-shuffle-an-array/)
- [1528. Shuffle String](../../1501-2000/1651-shuffle-string/)
- [26. Remove Duplicates from Sorted Array](../../0001-0500/0026-remove-duplicates-from-sorted-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/shuffle-the-array/)
