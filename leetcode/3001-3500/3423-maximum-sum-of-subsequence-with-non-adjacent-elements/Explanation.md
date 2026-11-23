# LeetCode 3165: Maximum Sum of Subsequence With Non-adjacent Elements

**LeetCode Problem #3165 — Maximum Sum of Subsequence With Non-adjacent Elements**
Solve LeetCode Maximum Sum of Subsequence With Non-adjacent Elements using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Sum of Subsequence With Non-adjacent Elements |
| LeetCode | #3165 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an array `nums` consisting of integers. You are also given a 2D array `queries`, where `queries[i] = [pos_i, x_i]`.

For query `i`, we first set `nums[pos_i]` equal to `x_i`, then we calculate the answer to query `i` which is the **maximum** sum of a subsequence of `nums` where **no two adjacent elements are selected**.

Return the *sum* of the answers to all queries.

Since the final answer may be very large, return it **modulo** `10^9 + 7`.

A **subsequence** is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

## Constraints
- `1 <= nums.length <= 5 * 10^4`
- `-10^5 <= nums[i] <= 10^5`
- `1 <= queries.length <= 5 * 10^4`
- `queries[i] == [pos_i, x_i]`
- `0 <= pos_i <= nums.length - 1`
- `-10^5 <= x_i <= 10^5`

## Examples
### Example 1
- **Input:** `nums = [3,5,9], queries = [[1,-2],[0,-3]]`
- **Output:** `21`
- **Explanation:** After the 1^st query, `nums = [3,-2,9]` and the maximum sum of a subsequence with non-adjacent elements is `3 + 9 = 12`. 
After the 2^nd query, `nums = [-3,-2,9]` and the maximum sum of a subsequence with non-adjacent elements is 9.

### Example 2
- **Input:** `nums = [0,-1], queries = [[0,-5]]`
- **Output:** `0`
- **Explanation:** After the 1^st query, `nums = [-5,-1]` and the maximum sum of a subsequence with non-adjacent elements is 0 (choosing an empty subsequence).

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Maximum Sum of Subsequence With Non-adjacent Elements**, we observe the problem requirements and utilize the **Dynamic Programming** technique. We decompose the problem into overlapping subproblems using a **DP Table / Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [3,5,9], queries = [[1,-2],[0,-3]]`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `21`.
4. **Verification:** After the 1^st query, `nums = [3,-2,9]` and the maximum sum of a subsequence with non-adjacent elements is `3 + 9 = 12`. 
After the 2^nd query, `nums = [-3,-2,9]` and the maximum sum of a subsequence with non-adjacent elements is 9.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for DP Table / Array.

## Pattern
**Dynamic Programming**

## Topics
- Dynamic Programming
- Memoization
- State Transition

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List

class Solution:
    def maximumSumSubsequence(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        size = 1
        while size < n:
            size *= 2

        # tree[i] = (f00, f01, f10, f11); padding leaves are value 0 -> all zeros
        tree = [(0, 0, 0, 0)] * (2 * size)

        def merge(L, R):
            return (
                max(L[0] + R[2], L[1] + R[0]),
                max(L[0] + R[3], L[1] + R[1]),
                max(L[2] + R[2], L[3] + R[0]),
                max(L[2] + R[3], L[3] + R[1]),
            )

        for i in range(n):
            tree[size + i] = (0, 0, 0, max(nums[i], 0))
        for i in range(size - 1, 0, -1):
            tree[i] = merge(tree[2 * i], tree[2 * i + 1])

        ans = 0
        for pos, x in queries:
            i = size + pos
            tree[i] = (0, 0, 0, max(x, 0))
            i >>= 1
            while i:
                tree[i] = merge(tree[2 * i], tree[2 * i + 1])
                i >>= 1
            ans += tree[1][3]

        return ans % MOD
```

## Why This Works
By utilizing **Dynamic Programming**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Incorrect base case initialization.
2. Flawed state transition equation.
3. Storing unnecessary state leading to Memory Limit Exceeded (MLE).

## Interview Notes
- **Tests:** Subproblem decomposition, state transition logic, and space optimization.
- **Follow-up:** Can space complexity be reduced from $O(n^2)$ to $O(n)$ or $O(1)$?

## Related Problems
- [689. Maximum Sum of 3 Non-Overlapping Subarrays](../../0501-1000/0689-maximum-sum-of-3-non-overlapping-subarrays/)
- [1031. Maximum Sum of Two Non-Overlapping Subarrays](../../1001-1500/1096-maximum-sum-of-two-non-overlapping-subarrays/)
- [2926. Maximum Balanced Subsequence Sum](../../3001-3500/3184-maximum-balanced-subsequence-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-sum-of-subsequence-with-non-adjacent-elements/)
