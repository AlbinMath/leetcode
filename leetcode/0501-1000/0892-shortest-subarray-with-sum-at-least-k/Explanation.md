# LeetCode 862: Shortest Subarray with Sum at Least K

**LeetCode Problem #862 — Shortest Subarray with Sum at Least K**
Solve LeetCode Shortest Subarray with Sum at Least K using JavaScript and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Shortest Subarray with Sum at Least K |
| LeetCode | #862 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an integer array `nums` and an integer `k`, return *the length of the shortest non-empty **subarray** of *`nums`* with a sum of at least *`k`. If there is no such **subarray**, return `-1`.

A **subarray** is a **contiguous** part of an array.

## Constraints
- `1 <= nums.length <= 10^5`
- `-10^5 <= nums[i] <= 10^5`
- `1 <= k <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [1], k = 1`
- **Output:** `1`

### Example 2
- **Input:** `nums = [1,2], k = 4`
- **Output:** `-1`

### Example 3
- **Input:** `nums = [2,-1,2], k = 3`
- **Output:** `3`

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Shortest Subarray with Sum at Least K**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1], k = 1`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Primitive Types.

## Pattern
**Math & Logic**

## Topics
- Math
- Simulation

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var shortestSubarray = function (nums, k) {
    const n = nums.length;
    const P = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) P[i + 1] = P[i] + nums[i];

    const dq = new Array(n + 1);
    let head = 0, tail = 0; // deque occupies dq[head..tail-1]
    let ans = Infinity;

    for (let j = 0; j <= n; j++) {
        while (head < tail && P[j] - P[dq[head]] >= k) {
            ans = Math.min(ans, j - dq[head]);
            head++;
        }
        while (head < tail && P[dq[tail - 1]] >= P[j]) {
            tail--;
        }
        dq[tail++] = j;
    }

    return ans === Infinity ? -1 : ans;
};
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
- [3795. Minimum Subarray Length With Distinct Sum At Least K](../../4001-4500/4152-minimum-subarray-length-with-distinct-sum-at-least-k/)
- [3095. Shortest Subarray With OR at Least K I](../../3001-3500/3381-shortest-subarray-with-or-at-least-k-i/)
- [3097. Shortest Subarray With OR at Least K II](../../3001-3500/3380-shortest-subarray-with-or-at-least-k-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/)
