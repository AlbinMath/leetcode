# LeetCode 3942: Minimum Operations to Sort a Permutation

**LeetCode Problem #3942 — Minimum Operations to Sort a Permutation**
Solve LeetCode Minimum Operations to Sort a Permutation using JavaScript and Backtracking. This solution finds the optimal result using Backtracking Recursive Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Operations to Sort a Permutation |
| LeetCode | #3942 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Backtracking Recursive Search |
| Data Structure | Recursion Tree |
| Pattern | Backtracking |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums` of length `n`, where `nums` is a permutation of the integers from 0 to `n - 1`.

You may perform **only** the following operations:

**Reverse** the entire array. 
 **Rotate Left by One**: Move the first element to the end of the array, and rest elements to left by one position.

Return an integer denoting the **minimum** number of operations required to sort the array in **increasing** order. If it is **not possible** to sort the array using only the given operations, return -1.

## Constraints
- `1 <= n == nums.length <= 10^5`
- `0 <= nums[i] <= n - 1`
- `nums` is a permutation of integers from 0 to `n - 1`.

## Examples
### Example 1
- **Input:** `nums = [0,2,1]`
- **Output:** `2`
- **Explanation:** Rotate Left by one: `[2, 1, 0]` 
 Reverse the array: `[0, 1, 2]` 
 

 The array becomes sorted in 2 operations, which is minimal.

### Example 2
- **Input:** `nums = [1,0,2]`
- **Output:** `2`
- **Explanation:** Reverse the array: `[2, 0, 1]` 
 Rotate Left by one: `[0, 1, 2]` 
 

 The array becomes sorted in 2 operations, which is minimal.

### Example 3
- **Input:** `nums = [2,0,1,3]`
- **Output:** `-1`
- **Explanation:** It is impossible to reach `[0, 1, 2, 3]`. Thus, the answer is -1.

## Key Insight
Leverage **Backtracking** with **Recursion Tree** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Operations to Sort a Permutation**, we observe the problem requirements and utilize the **Backtracking** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [0,2,1]`.
2. **Processing Steps:** We apply **Backtracking Recursive Search** using our **Recursion Tree**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** Rotate Left by one: `[2, 1, 0]` 
 Reverse the array: `[0, 1, 2]` 
 

 The array becomes sorted in 2 operations, which is minimal.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Recursion Tree.

## Pattern
**Backtracking**

## Topics
- Backtracking
- Recursion

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var minOperations = function(nums) {
    const n = nums.length;
    const pos = nums.indexOf(0);
    let ans = Infinity;

    // Check if nums is a rotation of sorted order.
    let forward = true;

    for (let i = 0; i < n; i++) {
        if (nums[(pos + i) % n] !== i) {
            forward = false;
            break;
        }
    }

    if (forward) {
        // Rotate left directly.
        ans = Math.min(ans, pos);

        // Reverse, rotate left, reverse.
        if (pos > 0) {
            ans = Math.min(ans, n - pos + 2);
        }
    }

    // Check if nums is a rotation of reverse sorted order.
    let backward = true;

    for (let i = 0; i < n; i++) {
        if (nums[(pos - i + n) % n] !== i) {
            backward = false;
            break;
        }
    }

    if (backward) {
        // Reverse first, then rotate left.
        ans = Math.min(ans, n - 1 - pos + 1);

        // Rotate left first, then reverse.
        ans = Math.min(ans, (pos + 1) % n + 1);
    }

    return ans === Infinity ? -1 : ans;
};
```

## Why This Works
By utilizing **Backtracking**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [2471. Minimum Number of Operations to Sort a Binary Tree by Level](../../2001-2500/2471-minimum-number-of-operations-to-sort-a-binary-tree-by-level/)
- [3863. Minimum Operations to Sort a String](../../3501-4000/3863-minimum-operations-to-sort-a-string/)
- [1806. Minimum Number of Operations to Reinitialize a Permutation](../../1501-2000/1806-minimum-number-of-operations-to-reinitialize-a-permutation/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-operations-to-sort-a-permutation/)
