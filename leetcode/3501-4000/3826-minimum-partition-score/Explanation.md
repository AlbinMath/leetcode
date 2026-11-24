# LeetCode 3826: Minimum Partition Score

**LeetCode Problem #3826 — Minimum Partition Score**
Solve LeetCode Minimum Partition Score using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Partition Score |
| LeetCode | #3826 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `nums` and an integer `k`.

Your task is to partition `nums` into **exactly** `k` subarrays and return an integer denoting the **minimum possible score** among all valid partitions.

The **score** of a partition is the **sum** of the **values** of all its subarrays.

The **value** of a subarray is defined as `sumArr * (sumArr + 1) / 2`, where `sumArr` is the sum of its elements.

## Constraints
- `1 <= nums.length <= 1000`
- `1 <= nums[i] <= 10^4`
- `1 <= k <= nums.length `

## Examples
### Example 1
- **Input:** `nums = [5,1,2,1], k = 2`
- **Output:** `25`
- **Explanation:** We must partition the array into `k = 2` subarrays. One optimal partition is `[5]` and `[1, 2, 1]`. 
 The first subarray has `sumArr = 5` and `value = 5 &times; 6 / 2 = 15`. 
 The second subarray has `sumArr = 1 + 2 + 1 = 4` and `value = 4 &times; 5 / 2 = 10`. 
 The score of this partition is `15 + 10 = 25`, which is the minimum possible score.

### Example 2
- **Input:** `nums = [1,2,3,4], k = 1`
- **Output:** `55`
- **Explanation:** Since we must partition the array into `k = 1` subarray, all elements belong to the same subarray: `[1, 2, 3, 4]`. 
 This subarray has `sumArr = 1 + 2 + 3 + 4 = 10` and `value = 10 &times; 11 / 2 = 55`.​​​​​​​ 
 The score of this partition is 55, which is the minimum possible score.

### Example 3
- **Input:** `nums = [1,1,1], k = 3`
- **Output:** `3`
- **Explanation:** We must partition the array into `k = 3` subarrays. The only valid partition is `[1], [1], [1]`. 
 Each subarray has `sumArr = 1` and `value = 1 &times; 2 / 2 = 1`. 
 The score of this partition is `1 + 1 + 1 = 3`, which is the minimum possible score.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Minimum Partition Score**, we observe the problem requirements and utilize the **Tree & Graph** technique. We perform a recursive Depth-First Search (DFS) traversal. The algorithm handles base cases at leaf nodes and aggregates results from subtrees back up to the root.

## Algorithm
1. Define base cases for null/leaf nodes.
2. Recursively traverse child nodes.
3. Combine child results to determine current node output.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [5,1,2,1], k = 2`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `25`.
4. **Verification:** We must partition the array into `k = 2` subarrays. One optimal partition is `[5]` and `[1, 2, 1]`. 
 The first subarray has `sumArr = 5` and `value = 5 &times; 6 / 2 = 15`. 
 The second subarray has `sumArr = 1 + 2 + 1 = 4` and `value = 4 &times; 5 / 2 = 10`. 
 The score of this partition is `15 + 10 = 25`, which is the minimum possible score.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Dictionary / Hash Map.

## Pattern
**Hash Map**

## Topics
- Hash Table
- Array
- Complement Lookup

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def minPartitionScore(self, nums, k):
        n = len(nums)
        P = [0] * (n + 1)
        for i, v in enumerate(nums):
            P[i + 1] = P[i] + v

        INF = float('inf')
        prev = [INF] * (n + 1)
        prev[0] = 0

        for t in range(1, k + 1):
            cur = [INF] * (n + 1)

            # cur[i] needs i >= t, and j in [t-1, i-1]
            def compute(lo, hi, optlo, opthi):
                if lo > hi:
                    return
                mid = (lo + hi) // 2
                best = INF
                bj = optlo
                top = min(mid - 1, opthi)
                for j in range(optlo, top + 1):
                    if prev[j] == INF:
                        continue
                    d = P[mid] - P[j]
                    val = prev[j] + d * (d + 1) // 2
                    if val < best:
                        best = val
                        bj = j
                cur[mid] = best
                compute(lo, mid - 1, optlo, bj)
                compute(mid + 1, hi, bj, opthi)

            compute(t, n, t - 1, n - 1)
            prev = cur

        return prev[n]
```

## Why This Works
By utilizing **Hash Map**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Using the same element twice.
2. Checking the map before inserting elements in the correct order.
3. Inefficient hash functions or unnecessary duplicate key updates.

## Interview Notes
- **Tests:** Hash map usage, complement/frequency lookup, and $O(n)$ time optimization.
- **Follow-up:** Can you solve the problem in $O(1)$ extra space if the input array is sorted?

## Related Problems
- [2322. Minimum Score After Removals on a Tree](../../2001-2500/2322-minimum-score-after-removals-on-a-tree/)
- [2492. Minimum Score of a Path Between Two Cities](../../2001-2500/2492-minimum-score-of-a-path-between-two-cities/)
- [2565. Subsequence With the Minimum Score](../../2501-3000/2565-subsequence-with-the-minimum-score/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-partition-score/)
