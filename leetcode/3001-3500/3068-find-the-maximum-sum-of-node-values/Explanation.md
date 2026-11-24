# LeetCode 3068: Find the Maximum Sum of Node Values

**LeetCode Problem #3068 — Find the Maximum Sum of Node Values**
Solve LeetCode Find the Maximum Sum of Node Values using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find the Maximum Sum of Node Values |
| LeetCode | #3068 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There exists an **undirected** tree with `n` nodes numbered `0` to `n - 1`. You are given a **0-indexed** 2D integer array `edges` of length `n - 1`, where `edges[i] = [u_i, v_i]` indicates that there is an edge between nodes `u_i` and `v_i` in the tree. You are also given a **positive** integer `k`, and a **0-indexed** array of **non-negative** integers `nums` of length `n`, where `nums[i]` represents the **value** of the node numbered `i`.

Alice wants the sum of values of tree nodes to be **maximum**, for which Alice can perform the following operation **any** number of times (**including zero**) on the tree:

Choose any edge `[u, v]` connecting the nodes `u` and `v`, and update their values as follows:

`nums[u] = nums[u] XOR k` 
 `nums[v] = nums[v] XOR k`

Return *the **maximum** possible **sum** of the **values** Alice can achieve by performing the operation **any** number of times*.

## Constraints
- `2 <= n == nums.length <= 2 * 10^4`
- `1 <= k <= 10^9`
- `0 <= nums[i] <= 10^9`
- `edges.length == n - 1`
- `edges[i].length == 2`
- `0 <= edges[i][0], edges[i][1] <= n - 1`
- The input is generated such that `edges` represent a valid tree.

## Examples
### Example 1
- **Input:** `nums = [1,2,1], k = 3, edges = [[0,1],[0,2]]`
- **Output:** `6`
- **Explanation:** Alice can achieve the maximum sum of 6 using a single operation:
- Choose the edge [0,2]. nums[0] and nums[2] become: 1 XOR 3 = 2, and the array nums becomes: [1,2,1] -> [2,2,2].
The total sum of values is 2 + 2 + 2 = 6.
It can be shown that 6 is the maximum achievable sum of values.

### Example 2
- **Input:** `nums = [2,3], k = 7, edges = [[0,1]]`
- **Output:** `9`
- **Explanation:** Alice can achieve the maximum sum of 9 using a single operation:
- Choose the edge [0,1]. nums[0] becomes: 2 XOR 7 = 5 and nums[1] become: 3 XOR 7 = 4, and the array nums becomes: [2,3] -> [5,4].
The total sum of values is 5 + 4 = 9.
It can be shown that 9 is the maximum achievable sum of values.

### Example 3
- **Input:** `nums = [7,7,7,7,7,7], k = 3, edges = [[0,1],[0,2],[0,3],[0,4],[0,5]]`
- **Output:** `42`
- **Explanation:** The maximum achievable sum is 42 which can be achieved by Alice performing no operations.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Find the Maximum Sum of Node Values**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,1], k = 3, edges = [[0,1],[0,2]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `6`.
4. **Verification:** Alice can achieve the maximum sum of 6 using a single operation:
- Choose the edge [0,2]. nums[0] and nums[2] become: 1 XOR 3 = 2, and the array nums becomes: [1,2,1] -> [2,2,2].
The total sum of values is 2 + 2 + 2 = 6.
It can be shown that 6 is the maximum achievable sum of values.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution(object):
    def maximumValueSum(self, nums, k, edges):
        total = 0
        flips = 0
        min_abs = float('inf')
        for x in nums:
            gain = (x ^ k) - x
            if gain > 0:
                total += x ^ k
                flips += 1
            else:
                total += x
            if abs(gain) < min_abs:
                min_abs = abs(gain)
        if flips % 2:
            total -= min_abs
        return total
```

## Why This Works
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [3547. Maximum Sum of Edge Values in a Graph](../../3501-4000/3547-maximum-sum-of-edge-values-in-a-graph/)
- [2859. Sum of Values at Indices With K Set Bits](../../2501-3000/2859-sum-of-values-at-indices-with-k-set-bits/)
- [3117. Minimum Sum of Values by Dividing Array](../../3001-3500/3117-minimum-sum-of-values-by-dividing-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-the-maximum-sum-of-node-values/)
