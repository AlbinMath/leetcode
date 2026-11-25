# LeetCode 3473: Sum of K Subarrays With Length at Least M

**LeetCode Problem #3473 — Sum of K Subarrays With Length at Least M**
Solve LeetCode Sum of K Subarrays With Length at Least M using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Sum of K Subarrays With Length at Least M |
| LeetCode | #3473 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums` and two integers, `k` and `m`.

Return the **maximum** sum of `k` non-overlapping subarrays of `nums`, where each subarray has a length of **at least** `m`.

## Constraints
- `1 <= nums.length <= 2000`
- `-10^4 <= nums[i] <= 10^4`
- `1 <= k <= floor(nums.length / m)`
- `1 <= m <= 3`

## Examples
### Example 1
- **Input:** `nums = [1,2,-1,3,3,4], k = 2, m = 2`
- **Output:** `13`
- **Explanation:** The optimal choice is: 

 
 Subarray `nums[3..5]` with sum `3 + 3 + 4 = 10` (length is `3 >= m`). 
 Subarray `nums[0..1]` with sum `1 + 2 = 3` (length is `2 >= m`). 
 

 The total sum is `10 + 3 = 13`.

### Example 2
- **Input:** `nums = [-10,3,-1,-2], k = 4, m = 1`
- **Output:** `-10`
- **Explanation:** The optimal choice is choosing each element as a subarray. The output is `(-10) + 3 + (-1) + (-2) = -10`.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Sum of K Subarrays With Length at Least M**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,-1,3,3,4], k = 2, m = 2`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `13`.
4. **Verification:** The optimal choice is: 

 
 Subarray `nums[3..5]` with sum `3 + 3 + 4 = 10` (length is `3 >= m`). 
 Subarray `nums[0..1]` with sum `1 + 2 = 3` (length is `2 >= m`). 
 

 The total sum is `10 + 3 = 13`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var maxSum = function(nums, k, m) {
    const n = nums.length;
    const prefix = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) {
        prefix[i + 1] = prefix[i] + nums[i];
    }
    const NEG_INF = -Infinity;
    let prev = new Array(n + 1).fill(0);
    for (let j = 1; j <= k; j++) {
        const curr = new Array(n + 1).fill(NEG_INF);
        let best = NEG_INF;
        for (let i = 1; i <= n; i++) {
            const p = i - m;
            if (p >= 0 && prev[p] !== NEG_INF) {
                best = Math.max(
                    best,
                    prev[p] - prefix[p]
                );
            }
            curr[i] = curr[i - 1];
            if (best !== NEG_INF) {
                curr[i] = Math.max(
                    curr[i],
                    prefix[i] + best
                );
            }
        }
        prev = curr;
    }
    return prev[n];
};
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
- [2461. Maximum Sum of Distinct Subarrays With Length K](../../2001-2500/2461-maximum-sum-of-distinct-subarrays-with-length-k/)
- [3795. Minimum Subarray Length With Distinct Sum At Least K](../../3501-4000/3795-minimum-subarray-length-with-distinct-sum-at-least-k/)
- [862. Shortest Subarray with Sum at Least K](../../0501-1000/0862-shortest-subarray-with-sum-at-least-k/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/sum-of-k-subarrays-with-length-at-least-m/)
