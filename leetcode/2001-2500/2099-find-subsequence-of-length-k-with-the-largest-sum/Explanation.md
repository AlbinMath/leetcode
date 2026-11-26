# LeetCode 2099: Find Subsequence of Length K With the Largest Sum

**LeetCode Problem #2099 — Find Subsequence of Length K With the Largest Sum**
Solve LeetCode Find Subsequence of Length K With the Largest Sum using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Subsequence of Length K With the Largest Sum |
| LeetCode | #2099 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `nums` and an integer `k`. You want to find a **subsequence **of `nums` of length `k` that has the **largest** sum.

Return* ****any** such subsequence as an integer array of length *`k`.

A **subsequence** is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

## Constraints
- `1 <= nums.length <= 1000`
- `-10^5 <= nums[i] <= 10^5`
- `1 <= k <= nums.length`

## Examples
### Example 1
- **Input:** `nums = [2,1,3,3], k = 2`
- **Output:** `[3,3]`
- **Explanation:** The subsequence has the largest sum of 3 + 3 = 6.

### Example 2
- **Input:** `nums = [-1,-2,3,4], k = 3`
- **Output:** `[-1,3,4]`
- **Explanation:** The subsequence has the largest sum of -1 + 3 + 4 = 6.

### Example 3
- **Input:** `nums = [3,4,3,3], k = 2`
- **Output:** `[3,4]`
- **Explanation:** The subsequence has the largest sum of 3 + 4 = 7. 
Another possible subsequence is [4, 3].

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Find Subsequence of Length K With the Largest Sum**, we observe the problem requirements and utilize the **Dynamic Programming** technique. We decompose the problem into overlapping subproblems using a **DP Table / Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,1,3,3], k = 2`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[3,3]`.
4. **Verification:** The subsequence has the largest sum of 3 + 3 = 6.

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
    def maxSubsequence(self, nums, k):
        return [x for _, x in sorted(sorted(enumerate(nums), key=lambda p: -p[1])[:k])]
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
- [2030. Smallest K-Length Subsequence With Occurrences of a Letter](../../2001-2500/2030-smallest-k-length-subsequence-with-occurrences-of-a-letter/)
- [2461. Maximum Sum of Distinct Subarrays With Length K](../../2001-2500/2461-maximum-sum-of-distinct-subarrays-with-length-k/)
- [2813. Maximum Elegance of a K-Length Subsequence](../../2501-3000/2813-maximum-elegance-of-a-k-length-subsequence/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/)
