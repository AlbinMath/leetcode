# LeetCode 1755: Closest Subsequence Sum

**LeetCode Problem #1755 — Closest Subsequence Sum**
Solve LeetCode Closest Subsequence Sum using JavaScript and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Closest Subsequence Sum |
| LeetCode | #1755 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums` and an integer `goal`.

You want to choose a subsequence of `nums` such that the sum of its elements is the closest possible to `goal`. That is, if the sum of the subsequence's elements is `sum`, then you want to **minimize the absolute difference** `abs(sum - goal)`.

Return *the **minimum** possible value of* `abs(sum - goal)`.

Note that a subsequence of an array is an array formed by removing some elements **(possibly all or none)** of the original array.

## Constraints
- `1 <= nums.length <= 40`
- `-10^7 <= nums[i] <= 10^7`
- `-10^9 <= goal <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [5,-7,3,5], goal = 6`
- **Output:** `0`
- **Explanation:** Choose the whole array as a subsequence, with a sum of 6.
This is equal to the goal, so the absolute difference is 0.

### Example 2
- **Input:** `nums = [7,-9,15,-2], goal = -5`
- **Output:** `1`
- **Explanation:** Choose the subsequence [7,-9,-2], with a sum of -4.
The absolute difference is abs(-4 - (-5)) = abs(1) = 1, which is the minimum.

### Example 3
- **Input:** `nums = [1,2,3], goal = -7`
- **Output:** `7`

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Closest Subsequence Sum**, we observe the problem requirements and utilize the **Dynamic Programming** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [5,-7,3,5], goal = 6`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `0`.
4. **Verification:** Choose the whole array as a subsequence, with a sum of 6.
This is equal to the goal, so the absolute difference is 0.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Sorted Array.

## Pattern
**Binary Search**

## Topics
- Binary Search
- Divide and Conquer
- Search Space

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
/**
 * @param {number[]} nums
 * @param {number} goal
 * @return {number}
 */
var minAbsDifference = function(nums, goal) {
    const n = nums.length;
    const mid = Math.floor(n / 2);

    // Generate every possible subset sum for an array.
    function getSubsetSums(arr) {
        const sums = [0];

        for (const num of arr) {
            const size = sums.length;

            for (let i = 0; i < size; i++) {
                sums.push(sums[i] + num);
            }
        }

        return sums;
    }

    const leftSums = getSubsetSums(nums.slice(0, mid));
    const rightSums = getSubsetSums(nums.slice(mid));

    // Sort one half to enable binary search.
    rightSums.sort((a, b) => a - b);

    let answer = Math.abs(goal);

    for (const leftSum of leftSums) {
        if (answer === 0) return 0;

        const target = goal - leftSum;

        // Find the first rightSum >= target.
        let low = 0;
        let high = rightSums.length;

        while (low < high) {
            const m = Math.floor((low + high) / 2);

            if (rightSums[m] < target) {
                low = m + 1;
            } else {
                high = m;
            }
        }

        // Check the first sum >= target.
        if (low < rightSums.length) {
            answer = Math.min(
                answer,
                Math.abs(leftSum + rightSums[low] - goal)
            );
        }

        // Also check the closest sum below target.
        if (low > 0) {
            answer = Math.min(
                answer,
                Math.abs(leftSum + rightSums[low - 1] - goal)
            );
        }
    }

    return answer;
};
```

## Why This Works
By utilizing **Binary Search**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Applying standard binary search without accounting for array rotation or duplicates.
2. Off-by-one errors when updating boundary pointers (`left = mid + 1` vs `right = mid - 1`).
3. Integer overflow during midpoint calculation (use `mid = left + (right - left) // 2`).

## Interview Notes
- **Tests:** Logarithmic search space reduction, boundary handling, and invariant preservation.
- **Follow-up:** How does performance change if the array contains duplicate elements?

## Related Problems
- [1425. Constrained Subsequence Sum](../../1001-1500/1425-constrained-subsequence-sum/)
- [2099. Find Subsequence of Length K With the Largest Sum](../../2001-2500/2099-find-subsequence-of-length-k-with-the-largest-sum/)
- [2389. Longest Subsequence With Limited Sum](../../2001-2500/2389-longest-subsequence-with-limited-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/closest-subsequence-sum/)
