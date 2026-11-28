# LeetCode 3287: Find the Maximum Sequence Value of Array

**LeetCode Problem #3287 — Find the Maximum Sequence Value of Array**
Solve LeetCode Find the Maximum Sequence Value of Array using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find the Maximum Sequence Value of Array |
| LeetCode | #3287 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `nums` and a **positive** integer `k`.

The **value** of a sequence `seq` of size `2 * x` is defined as:

`(seq[0] OR seq[1] OR ... OR seq[x - 1]) XOR (seq[x] OR seq[x + 1] OR ... OR seq[2 * x - 1])`.

Return the **maximum** **value** of any subsequence of `nums` having size `2 * k`.

## Constraints
- `2 <= nums.length <= 400`
- `1 <= nums[i] < 2^7`
- `1 <= k <= nums.length / 2`

## Examples
### Example 1
- **Input:** `nums = [2,6,7], k = 1`
- **Output:** `5`
- **Explanation:** The subsequence `[2, 7]` has the maximum value of `2 XOR 7 = 5`.

### Example 2
- **Input:** `nums = [4,2,5,6,7], k = 2`
- **Output:** `2`
- **Explanation:** The subsequence `[4, 5, 6, 7]` has the maximum value of `(4 OR 5) XOR (6 OR 7) = 2`.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Find the Maximum Sequence Value of Array**, we observe the problem requirements and utilize the **Array / General** technique. We decompose the problem into overlapping subproblems using a **Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,6,7], k = 1`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `5`.
4. **Verification:** The subsequence `[2, 7]` has the maximum value of `2 XOR 7 = 5`.

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
class Solution(object):
    def maxValue(self, nums, k):
        n = len(nums)

        def build(arr):
            # res[i] = set of ORs from choosing exactly k of the first i elements
            dp = [set() for _ in range(k + 1)]
            dp[0].add(0)
            res = [frozenset()] * (len(arr) + 1)
            for i, x in enumerate(arr):
                for j in range(min(k, i + 1), 0, -1):
                    if dp[j - 1]:
                        dp[j] |= {v | x for v in dp[j - 1]}
                res[i + 1] = frozenset(dp[k])
            return res

        pre = build(nums)
        suf = build(nums[::-1])  # suf[m] = ORs from choosing k of the last m elements

        best = 0
        for i in range(k, n - k + 1):
            A = pre[i]
            B = suf[n - i]
            for a in A:
                for b in B:
                    v = a ^ b
                    if v > best:
                        best = v
        return best
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
- [3796. Find Maximum Value in a Constrained Sequence](../../3501-4000/3796-find-maximum-value-in-a-constrained-sequence/)
- [3993. Maximum Value of an Alternating Sequence](../../3501-4000/3993-maximum-value-of-an-alternating-sequence/)
- [1420. Build Array Where You Can Find The Maximum Exactly K Comparisons](../../1001-1500/1420-build-array-where-you-can-find-the-maximum-exactly-k-comparisons/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-the-maximum-sequence-value-of-array/)
