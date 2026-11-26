# LeetCode 1589: Maximum Sum Obtained of Any Permutation

**LeetCode Problem #1589 — Maximum Sum Obtained of Any Permutation**
Solve LeetCode Maximum Sum Obtained of Any Permutation using JavaScript and Backtracking. This solution finds the optimal result using Backtracking Recursive Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Sum Obtained of Any Permutation |
| LeetCode | #1589 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Backtracking Recursive Search |
| Data Structure | Recursion Tree |
| Pattern | Backtracking |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
We have an array of integers, `nums`, and an array of `requests` where `requests[i] = [start_i, end_i]`. The `i^th` request asks for the sum of `nums[start_i] + nums[start_i + 1] + ... + nums[end_i - 1] + nums[end_i]`. Both `start_i` and `end_i` are *0-indexed*.

Return *the maximum total sum of all requests **among all permutations** of* `nums`.

Since the answer may be too large, return it **modulo** `10^9 + 7`.

## Constraints
- `n == nums.length`
- `1 <= n <= 10^5`
- `0 <= nums[i] <= 10^5`
- `1 <= requests.length <= 10^5`
- `requests[i].length == 2`
- `0 <= start_i <= end_i < n`

## Examples
### Example 1
- **Input:** `nums = [1,2,3,4,5], requests = [[1,3],[0,1]]`
- **Output:** `19`
- **Explanation:** One permutation of nums is [2,1,3,4,5] with the following result: 
requests[0] -> nums[1] + nums[2] + nums[3] = 1 + 3 + 4 = 8
requests[1] -> nums[0] + nums[1] = 2 + 1 = 3
Total sum: 8 + 3 = 11.
A permutation with a higher total sum is [3,5,4,2,1] with the following result:
requests[0] -> nums[1] + nums[2] + nums[3] = 5 + 4 + 2 = 11
requests[1] -> nums[0] + nums[1] = 3 + 5 = 8
Total sum: 11 + 8 = 19, which is the best that you can do.

### Example 2
- **Input:** `nums = [1,2,3,4,5,6], requests = [[0,1]]`
- **Output:** `11`
- **Explanation:** A permutation with the max total sum is [6,5,4,3,2,1] with request sums [11].

### Example 3
- **Input:** `nums = [1,2,3,4,5,10], requests = [[0,2],[1,3],[1,1]]`
- **Output:** `47`
- **Explanation:** A permutation with the max total sum is [4,10,5,3,2,1] with request sums [19,18,10].

## Key Insight
Leverage **Backtracking** with **Recursion Tree** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Sum Obtained of Any Permutation**, we observe the problem requirements and utilize the **Backtracking** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,3,4,5], requests = [[1,3],[0,1]]`.
2. **Processing Steps:** We apply **Backtracking Recursive Search** using our **Recursion Tree**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `19`.
4. **Verification:** One permutation of nums is [2,1,3,4,5] with the following result: 
requests[0] -> nums[1] + nums[2] + nums[3] = 1 + 3 + 4 = 8
requests[1] -> nums[0] + nums[1] = 2 + 1 = 3
Total sum: 8 + 3 = 11.
A permutation with a higher total sum is [3,5,4,2,1] with the following result:
requests[0] -> nums[1] + nums[2] + nums[3] = 5 + 4 + 2 = 11
requests[1] -> nums[0] + nums[1] = 3 + 5 = 8
Total sum: 11 + 8 = 19, which is the best that you can do.

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
var maxSumRangeQuery = function(nums, requests) {
    const MOD = 1000000007;
    const n = nums.length;
    let diff = new Array(n + 1).fill(0);
    for (let [start, end] of requests) {
        diff[start]++;
        diff[end + 1]--;
    }
    let freq = new Array(n).fill(0);
    let current = 0;

    for (let i = 0; i < n; i++) {
        current += diff[i];
        freq[i] = current;
    }
    nums.sort((a, b) => a - b);
    freq.sort((a, b) => a - b);
    let result = 0;

    for (let i = 0; i < n; i++) {
        result = (result + nums[i] * freq[i]) % MOD;
    }

    return result;
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
- [2064. Minimized Maximum of Products Distributed to Any Store](../../2001-2500/2064-minimized-maximum-of-products-distributed-to-any-store/)
- [124. Binary Tree Maximum Path Sum](../../0001-0500/0124-binary-tree-maximum-path-sum/)
- [689. Maximum Sum of 3 Non-Overlapping Subarrays](../../0501-1000/0689-maximum-sum-of-3-non-overlapping-subarrays/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/)
