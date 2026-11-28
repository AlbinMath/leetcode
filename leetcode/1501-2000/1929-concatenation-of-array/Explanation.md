# LeetCode 1929: Concatenation of Array

**LeetCode Problem #1929 — Concatenation of Array**
Solve LeetCode Concatenation of Array using TypeScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Concatenation of Array |
| LeetCode | #1929 |
| Difficulty | Easy |
| Language | TypeScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an integer array `nums` of length `n`, you want to create an array `ans` of length `2n` where `ans[i] == nums[i]` and `ans[i + n] == nums[i]` for `0 <= i < n` (**0-indexed**).

Specifically, `ans` is the **concatenation** of two `nums` arrays.

Return *the array *`ans`.

## Constraints
- `n == nums.length`
- `1 <= n <= 1000`
- `1 <= nums[i] <= 1000`

## Examples
### Example 1
- **Input:** `nums = [1,2,1]`
- **Output:** `[1,2,1,1,2,1]`
- **Explanation:** The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
- ans = [1,2,1,1,2,1]

### Example 2
- **Input:** `nums = [1,3,2,1]`
- **Output:** `[1,3,2,1,1,3,2,1]`
- **Explanation:** The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
- ans = [1,3,2,1,1,3,2,1]

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code creates a new array of size `2n` and copies `nums` twice — once at the beginning and once starting at index `n`. Alternatively, it simply concatenates the array with itself using spread/concat.

Time complexity is $O(N)$ and space complexity is $O(N)$.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,1]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1,2,1,1,2,1]`.
4. **Verification:** The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
- ans = [1,2,1,1,2,1]

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
function getConcatenation(nums: number[]): number[] {
    return [...nums, ...nums];
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
- [1640. Check Array Formation Through Concatenation](../../1501-2000/1640-check-array-formation-through-concatenation/)
- [2562. Find the Array Concatenation Value](../../2501-3000/2562-find-the-array-concatenation-value/)
- [26. Remove Duplicates from Sorted Array](../../0001-0500/0026-remove-duplicates-from-sorted-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/concatenation-of-array/)
