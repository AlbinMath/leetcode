# LeetCode 1955: Count Number of Special Subsequences

**LeetCode Problem #1955 — Count Number of Special Subsequences**
Solve LeetCode Count Number of Special Subsequences using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Number of Special Subsequences |
| LeetCode | #1955 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
A sequence is **special** if it consists of a **positive** number of `0`s, followed by a **positive** number of `1`s, then a **positive** number of `2`s.

For example, `[0,1,2]` and `[0,0,1,1,1,2]` are special. 
 In contrast, `[2,1,0]`, `[1]`, and `[0,1,2,0]` are not special.

Given an array `nums` (consisting of **only** integers `0`, `1`, and `2`), return* the **number of different subsequences** that are special*. Since the answer may be very large, **return it modulo **`10^9 + 7`.

A **subsequence** of an array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements. Two subsequences are **different** if the **set of indices** chosen are different.

## Constraints
- `1 <= nums.length <= 10^5`
- `0 <= nums[i] <= 2`

## Examples
### Example 1
- **Input:** `nums = [0,1,2,2]`
- **Output:** `3`
- **Explanation:** The special subsequences are bolded [

### Example 2
- **Input:** `nums = [2,2,0,0]`
- **Output:** `0`
- **Explanation:** There are no special subsequences in [2,2,0,0].

### Example 3
- **Input:** `nums = [0,1,2,0,1,2]`
- **Output:** `7`
- **Explanation:** The special subsequences are bolded:
- [

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Count Number of Special Subsequences**, we observe the problem requirements and utilize the **Dynamic Programming** technique. We decompose the problem into overlapping subproblems using a **DP Table / Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [0,1,2,2]`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** The special subsequences are bolded [

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
    def countSpecialSubsequences(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        dp0 = dp1 = dp2 = 0
        
        for x in nums:
            if x == 0:
                dp0 = (2 * dp0 + 1) % MOD
            elif x == 1:
                dp1 = (2 * dp1 + dp0) % MOD
            else:
                dp2 = (2 * dp2 + dp1) % MOD
                
        return dp2
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
- [3120. Count the Number of Special Characters I](../../3001-3500/3120-count-the-number-of-special-characters-i/)
- [3404. Count Special Subsequences](../../3001-3500/3404-count-special-subsequences/)
- [792. Number of Matching Subsequences](../../0501-1000/0792-number-of-matching-subsequences/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-number-of-special-subsequences/)
