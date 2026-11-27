# LeetCode 2389: Longest Subsequence With Limited Sum

**LeetCode Problem #2389 — Longest Subsequence With Limited Sum**
Solve LeetCode Longest Subsequence With Limited Sum using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest Subsequence With Limited Sum |
| LeetCode | #2389 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `nums` of length `n`, and an integer array `queries` of length `m`.

Return *an array *`answer`* of length *`m`* where *`answer[i]`* is the **maximum** size of a **subsequence** that you can take from *`nums`* such that the **sum** of its elements is less than or equal to *`queries[i]`.

A **subsequence** is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

## Constraints
- `n == nums.length`
- `m == queries.length`
- `1 <= n, m <= 1000`
- `1 <= nums[i], queries[i] <= 10^6`

## Examples
### Example 1
- **Input:** `nums = [4,5,2,1], queries = [3,10,21]`
- **Output:** `[2,3,4]`
- **Explanation:** We answer the queries as follows:
- The subsequence [2,1] has a sum less than or equal to 3. It can be proven that 2 is the maximum size of such a subsequence, so answer[0] = 2.
- The subsequence [4,5,1] has a sum less than or equal to 10. It can be proven that 3 is the maximum size of such a subsequence, so answer[1] = 3.
- The subsequence [4,5,2,1] has a sum less than or equal to 21. It can be proven that 4 is the maximum size of such a subsequence, so answer[2] = 4.

### Example 2
- **Input:** `nums = [2,3,4,5], queries = [1]`
- **Output:** `[0]`
- **Explanation:** The empty subsequence is the only subsequence that has a sum less than or equal to 1, so answer[0] = 0.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Longest Subsequence With Limited Sum**, we observe the problem requirements and utilize the **Dynamic Programming** technique. We decompose the problem into overlapping subproblems using a **DP Table / Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [4,5,2,1], queries = [3,10,21]`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[2,3,4]`.
4. **Verification:** We answer the queries as follows:
- The subsequence [2,1] has a sum less than or equal to 3. It can be proven that 2 is the maximum size of such a subsequence, so answer[0] = 2.
- The subsequence [4,5,1] has a sum less than or equal to 10. It can be proven that 3 is the maximum size of such a subsequence, so answer[1] = 3.
- The subsequence [4,5,2,1] has a sum less than or equal to 21. It can be proven that 4 is the maximum size of such a subsequence, so answer[2] = 4.

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
class Solution:
    def answerQueries(self, nums, queries):
        nums.sort()
        order = sorted(range(len(queries)), key=lambda i: queries[i])
        ans = [0] * len(queries)
        k, total = 0, 0
        for qi in order:
            while k < len(nums) and total + nums[k] <= queries[qi]:
                total += nums[k]
                k += 1
            ans[qi] = k
        return ans
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
- [300. Longest Increasing Subsequence](../../0001-0500/0300-longest-increasing-subsequence/)
- [516. Longest Palindromic Subsequence](../../0501-1000/0516-longest-palindromic-subsequence/)
- [521. Longest Uncommon Subsequence I](../../0501-1000/0521-longest-uncommon-subsequence-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longest-subsequence-with-limited-sum/)
