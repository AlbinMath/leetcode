# LeetCode 448: Find All Numbers Disappeared in an Array

**LeetCode Problem #448 — Find All Numbers Disappeared in an Array**
Solve LeetCode Find All Numbers Disappeared in an Array using TypeScript and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find All Numbers Disappeared in an Array |
| LeetCode | #448 |
| Difficulty | Easy |
| Language | TypeScript |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an array `nums` of `n` integers where `nums[i]` is in the range `[1, n]`, return *an array of all the integers in the range* `[1, n]` *that do not appear in* `nums`.

## Constraints
- `n == nums.length`
- `1 <= n <= 10^5`
- `1 <= nums[i] <= n`

## Examples
### Example 1
- **Input:** `nums = [4,3,2,7,8,2,3,1]`
- **Output:** `[5,6]`

### Example 2
- **Input:** `nums = [1,1]`
- **Output:** `[2]`

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code uses the **array itself as a hash set** by negating values at corresponding indices.

1. **Mark Presence:** For each number `num` in the array, compute `index = |num| - 1` (using absolute value since values may already be negated). If `nums[index]` is positive, negate it to mark that the number `index + 1` exists in the array.
2. **Find Missing:** After marking, iterate through the array. If `nums[i]` is still positive, it means no number `i + 1` was encountered in the array, so `i + 1` is missing and gets pushed to the result.

Time complexity is $O(N)$ and space complexity is $O(1)$ (excluding the output array).

## Algorithm
1. Initialize state variables / data structure (**Primitive Types**).
2. Process elements sequentially using **Mathematical Simulation & Modular Arithmetic**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [4,3,2,7,8,2,3,1]`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[5,6]`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Primitive Types.

## Pattern
**Math & Logic**

## Topics
- Math
- Simulation

## Language
TypeScript

## Source Code
- [solution.ts](./solution.ts)


```typescript
function findDisappearedNumbers(nums: number[]): number[] {
    const result: number[] = [];

    // Mark the index corresponding to each number
    for (const num of nums) {
        const index = Math.abs(num) - 1;

        if (nums[index] > 0) {
            nums[index] = -nums[index];
        }
    }

    // Positive values mean the number is missing
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] > 0) {
            result.push(i + 1);
        }
    }

    return result;
}
```

## Why This Works
By utilizing **Math & Logic**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [2150. Find All Lonely Numbers in the Array](../../2001-2500/2270-find-all-lonely-numbers-in-the-array/)
- [2593. Find Score of an Array After Marking All Elements](../../2501-3000/2695-find-score-of-an-array-after-marking-all-elements/)
- [34. Find First and Last Position of Element in Sorted Array](../../0001-0500/0034-find-first-and-last-position-of-element-in-sorted-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/)
