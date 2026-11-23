# LeetCode 485: Max Consecutive Ones

**LeetCode Problem #485 — Max Consecutive Ones**
Solve LeetCode Max Consecutive Ones using TypeScript and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Max Consecutive Ones |
| LeetCode | #485 |
| Difficulty | Easy |
| Language | TypeScript |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a binary array `nums`, return *the maximum number of consecutive *`1`*'s in the array*.

## Constraints
- `1 <= nums.length <= 10^5`
- `nums[i]` is either `0` or `1`.

## Examples
### Example 1
- **Input:** `nums = [1,1,0,1,1,1]`
- **Output:** `3`
- **Explanation:** The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

### Example 2
- **Input:** `nums = [1,0,1,1,0,1]`
- **Output:** `2`

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code uses a simple **single-pass counting** approach.

1. It maintains two variables: `current` (the length of the current streak of `1`s) and `max` (the longest streak seen so far).
2. For each element:
   - If it's `1`, increment `current` and update `max` if `current` exceeds it.
   - If it's `0`, reset `current` to `0`.
3. Return `max`.

Time complexity is $O(N)$ and space complexity is $O(1)$.

## Algorithm
1. Initialize state variables / data structure (**Primitive Types**).
2. Process elements sequentially using **Mathematical Simulation & Modular Arithmetic**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,1,0,1,1,1]`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

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
function findMaxConsecutiveOnes(nums: number[]): number {
    let current = 0;
    let max = 0;

    for (const num of nums) {
        if (num === 1) {
            current++;
            max = Math.max(max, current);
        } else {
            current = 0;
        }
    }

    return max;
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
- [1004. Max Consecutive Ones III](../../1001-1500/1046-max-consecutive-ones-iii/)
- [600. Non-negative Integers without Consecutive Ones](../../0501-1000/0600-non-negative-integers-without-consecutive-ones/)
- [1703. Minimum Adjacent Swaps for K Consecutive Ones](../../1501-2000/1805-minimum-adjacent-swaps-for-k-consecutive-ones/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/max-consecutive-ones/)
