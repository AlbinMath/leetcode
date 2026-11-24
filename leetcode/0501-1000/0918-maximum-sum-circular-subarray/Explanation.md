# LeetCode 918: Maximum Sum Circular Subarray

**LeetCode Problem #918 — Maximum Sum Circular Subarray**
Solve LeetCode Maximum Sum Circular Subarray using JavaScript and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Sum Circular Subarray |
| LeetCode | #918 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given a **circular integer array** `nums` of length `n`, return *the maximum possible sum of a non-empty **subarray** of *`nums`.

A **circular array** means the end of the array connects to the beginning of the array. Formally, the next element of `nums[i]` is `nums[(i + 1) % n]` and the previous element of `nums[i]` is `nums[(i - 1 + n) % n]`.

A **subarray** may only include each element of the fixed buffer `nums` at most once. Formally, for a subarray `nums[i], nums[i + 1], ..., nums[j]`, there does not exist `i <= k1`, `k2 <= j` with `k1 % n == k2 % n`.

## Constraints
- `n == nums.length`
- `1 <= n <= 3 * 10^4`
- `-3 * 10^4 <= nums[i] <= 3 * 10^4`

## Examples
### Example 1
- **Input:** `nums = [1,-2,3,-2]`
- **Output:** `3`
- **Explanation:** Subarray [3] has maximum sum 3.

### Example 2
- **Input:** `nums = [5,-3,5]`
- **Output:** `10`
- **Explanation:** Subarray [5,5] has maximum sum 5 + 5 = 10.

### Example 3
- **Input:** `nums = [-3,-2,-3]`
- **Output:** `-2`
- **Explanation:** Subarray [-2] has maximum sum -2.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Sum Circular Subarray**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,-2,3,-2]`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** Subarray [3] has maximum sum 3.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var maxSubarraySumCircular = function(nums) {
    let totalSum = 0;

    let currentMax = 0;
    let maxSum = -Infinity;

    let currentMin = 0;
    let minSum = Infinity;

    for (const num of nums) {
        totalSum += num;

        // Maximum subarray (Kadane's algorithm)
        currentMax = Math.max(num, currentMax + num);
        maxSum = Math.max(maxSum, currentMax);

        // Minimum subarray
        currentMin = Math.min(num, currentMin + num);
        minSum = Math.min(minSum, currentMin);
    }

    // If every number is negative, wrapping would give 0,
    // which is invalid because the subarray must be non-empty.
    if (maxSum < 0) {
        return maxSum;
    }

    return Math.max(maxSum, totalSum - minSum);
};
```

## Why This Works
By utilizing **Stack & Queue**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1800. Maximum Ascending Subarray Sum](../../1501-2000/1800-maximum-ascending-subarray-sum/)
- [2841. Maximum Sum of Almost Unique Subarray](../../2501-3000/2841-maximum-sum-of-almost-unique-subarray/)
- [3962. Maximum Subarray Sum After at Most K Swaps](../../3501-4000/3962-maximum-subarray-sum-after-at-most-k-swaps/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-sum-circular-subarray/)
