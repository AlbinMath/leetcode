# LeetCode 3681: Maximum XOR of Subsequences

**LeetCode Problem #3681 — Maximum XOR of Subsequences**
Solve LeetCode Maximum XOR of Subsequences using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum XOR of Subsequences |
| LeetCode | #3681 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `nums` of length `n` where each element is a non-negative integer.

Select **two** subsequences of `nums` (they may be empty and are **allowed** to **overlap**), each preserving the original order of elements, and let:

`X` be the bitwise XOR of all elements in the first subsequence. 
 `Y` be the bitwise XOR of all elements in the second subsequence.

Return the **maximum** possible value of `X XOR Y`.

**Note:** The XOR of an **empty** subsequence is 0.

## Constraints
- `2 <= nums.length <= 10^5`
- `0 <= nums[i] <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [1,2,3]`
- **Output:** `3`
- **Explanation:** Choose subsequences: 

 
 First subsequence `[2]`, whose XOR is 2. 
 Second subsequence `[2,3]`, whose XOR is 1. 
 

 Then, XOR of both subsequences = `2 XOR 1 = 3`. 

 This is the maximum XOR value achievable from any two subsequences.

### Example 2
- **Input:** `nums = [5,2]`
- **Output:** `7`
- **Explanation:** Choose subsequences: 

 
 First subsequence `[5]`, whose XOR is 5. 
 Second subsequence `[2]`, whose XOR is 2. 
 

 Then, XOR of both subsequences = `5 XOR 2 = 7`. 

 This is the maximum XOR value achievable from any two subsequences.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Maximum XOR of Subsequences**, we observe the problem requirements and utilize the **Dynamic Programming** technique. We decompose the problem into overlapping subproblems using a **DP Table / Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,3]`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** Choose subsequences: 

 
 First subsequence `[2]`, whose XOR is 2. 
 Second subsequence `[2,3]`, whose XOR is 1. 
 

 Then, XOR of both subsequences = `2 XOR 1 = 3`. 

 This is the maximum XOR value achievable from any two subsequences.

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
    def maxXorSubsequences(self, nums):
        basis = [0] * 30
        for x in nums:
            for b in range(29, -1, -1):
                if not (x >> b) & 1:
                    continue
                if basis[b] == 0:
                    basis[b] = x
                    break
                x ^= basis[b]

        res = 0
        for b in range(29, -1, -1):
            if basis[b] and (res ^ basis[b]) > res:
                res ^= basis[b]
        return res
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
- [2002. Maximum Product of the Length of Two Palindromic Subsequences](../../2001-2500/2002-maximum-product-of-the-length-of-two-palindromic-subsequences/)
- [2842. Count K-Subsequences of a String With Maximum Beauty](../../2501-3000/2842-count-k-subsequences-of-a-string-with-maximum-beauty/)
- [3428. Maximum and Minimum Sums of at Most Size K Subsequences](../../3001-3500/3428-maximum-and-minimum-sums-of-at-most-size-k-subsequences/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-xor-of-subsequences/)
