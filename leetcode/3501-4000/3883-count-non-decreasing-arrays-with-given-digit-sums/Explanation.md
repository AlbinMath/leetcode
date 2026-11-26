# LeetCode 3883: Count Non Decreasing Arrays With Given Digit Sums

**LeetCode Problem #3883 — Count Non Decreasing Arrays With Given Digit Sums**
Solve LeetCode Count Non Decreasing Arrays With Given Digit Sums using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Non Decreasing Arrays With Given Digit Sums |
| LeetCode | #3883 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `digitSum` of length `n`.

An array `arr` of length `n` is considered **valid** if:

`0 <= arr[i] <= 5000` 
 it is **non-decreasing**. 
 the **sum of the digits** of `arr[i]` **equals** `digitSum[i]`.

Return an integer denoting the number of **distinct valid arrays**. Since the answer may be large, return it modulo `10^9 + 7`.

An array is said to be **non-decreasing** if each element is greater than or equal to the previous element, if it exists.

## Constraints
- `1 <= digitSum.length <= 1000`
- `0 <= digitSum[i] <= 50`

## Examples
### Example 1
- **Input:** `digitSum = [25,1]`
- **Output:** `6`
- **Explanation:** Numbers whose sum of digits is 25 are 799, 889, 898, 979, 988, and 997. 

 The only number whose sum of digits is 1 that can appear after these values while keeping the array non-decreasing is 1000. 

 Thus, the valid arrays are `[799, 1000]`, `[889, 1000]`, `[898, 1000]`, `[979, 1000]`, `[988, 1000]`, and `[997, 1000]`. 

 Hence, the answer is 6.

### Example 2
- **Input:** `digitSum = [1]`
- **Output:** `4`
- **Explanation:** The valid arrays are `[1]`, `[10]`, `[100]`, and `[1000]`. 

 Thus, the answer is 4.

### Example 3
- **Input:** `digitSum = [2,49,23]`
- **Output:** `0`
- **Explanation:** There is no integer in the range [0, 5000] whose sum of digits is 49. Thus, the answer is 0.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Count Non Decreasing Arrays With Given Digit Sums**, we observe the problem requirements and utilize the **Math & Logic** technique. We decompose the problem into overlapping subproblems using a **Primitive Types**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `digitSum = [25,1]`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `6`.
4. **Verification:** Numbers whose sum of digits is 25 are 799, 889, 898, 979, 988, and 997. 

 The only number whose sum of digits is 1 that can appear after these values while keeping the array non-decreasing is 1000. 

 Thus, the valid arrays are `[799, 1000]`, `[889, 1000]`, `[898, 1000]`, `[979, 1000]`, `[988, 1000]`, and `[997, 1000]`. 

 Hence, the answer is 6.

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
    def countArrays(self, digitSum: List[int]) -> int:
        MOD = 10**9 + 7
        M = 5001
        ds = [sum(map(int, str(v))) for v in range(M)]

        # first position: every value with matching digit sum counts once
        dp = [1 if ds[v] == digitSum[0] else 0 for v in range(M)]

        for i in range(1, len(digitSum)):
            target = digitSum[i]
            new = [0] * M
            run = 0
            for v in range(M):
                run = (run + dp[v]) % MOD      # sum of dp[u] for u <= v
                if ds[v] == target:
                    new[v] = run
            dp = new

        return sum(dp) % MOD
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
- [3420. Count Non-Decreasing Subarrays After K Operations](../../3001-3500/3420-count-non-decreasing-subarrays-after-k-operations/)
- [828. Count Unique Characters of All Substrings of a Given String](../../0501-1000/0828-count-unique-characters-of-all-substrings-of-a-given-string/)
- [1442. Count Triplets That Can Form Two Arrays of Equal XOR](../../1001-1500/1442-count-triplets-that-can-form-two-arrays-of-equal-xor/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-non-decreasing-arrays-with-given-digit-sums/)
