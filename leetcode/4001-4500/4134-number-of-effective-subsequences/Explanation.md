# LeetCode 3757: Number of Effective Subsequences

**LeetCode Problem #3757 — Number of Effective Subsequences**
Solve LeetCode Number of Effective Subsequences using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Effective Subsequences |
| LeetCode | #3757 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `nums`.

The **strength** of the array is defined as the **bitwise OR** of all its elements.

A ** subsequence ** is considered **effective** if removing that subsequence **strictly decreases** the strength of the remaining elements.

Return the number of **effective subsequences** in `nums`. Since the answer may be large, return it **modulo** `10^9 + 7`.

The bitwise OR of an empty array is 0.

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^6`

## Examples
### Example 1
- **Input:** `nums = [1,2,3]`
- **Output:** `3`
- **Explanation:** The Bitwise OR of the array is `1 OR 2 OR 3 = 3`. 
 Subsequences that are effective are:
 
 `[1, 3]`: The remaining element `[2]` has a Bitwise OR of 2. 
 `[2, 3]`: The remaining element `[1]` has a Bitwise OR of 1. 
 `[1, 2, 3]`: The remaining elements `[]` have a Bitwise OR of 0. 
 
 
 Thus, the total number of effective subsequences is 3.

### Example 2
- **Input:** `nums = [7,4,6]`
- **Output:** `4`
- **Explanation:** ​​​​​​​ 

 
 The Bitwise OR of the array is `7 OR 4 OR 6 = 7`. 
 Subsequences that are effective are:
 
 `[7]`: The remaining elements `[4, 6]` have a Bitwise OR of 6. 
 `[7, 4]`: The remaining element `[6]` has a Bitwise OR of 6. 
 `[7, 6]`: The remaining element `[4]` has a Bitwise OR of 4. 
 `[7, 4, 6]`: The remaining elements `[]` have a Bitwise OR of 0. 
 
 
 Thus, the total number of effective subsequences is 4.

### Example 3
- **Input:** `nums = [8,8]`
- **Output:** `1`
- **Explanation:** The Bitwise OR of the array is `8 OR 8 = 8`. 
 Only the subsequence `[8, 8]` is effective since removing it leaves `[]` which has a Bitwise OR of 0. 
 Thus, the total number of effective subsequences is 1.

### Example 4
- **Input:** `nums = [2,2,1]`
- **Output:** `5`
- **Explanation:** The Bitwise OR of the array is `2 OR 2 OR 1 = 3`. 
 Subsequences that are effective are:
 
 `[1]`: The remaining elements `[2, 2]` have a Bitwise OR of 2. 
 `[2, 1]` (using `nums[0]`, `nums[2]`): The remaining element `[2]` has a Bitwise OR of 2. 
 `[2, 1]` (using `nums[1]`, `nums[2]`): The remaining element `[2]` has a Bitwise OR of 2. 
 `[2, 2]`: The remaining element `[1]` has a Bitwise OR of 1. 
 `[2, 2, 1]`: The remaining elements `[]` have a Bitwise OR of 0. 
 
 
 Thus, the total number of effective subsequences is 5.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Number of Effective Subsequences**, we observe the problem requirements and utilize the **Dynamic Programming** technique. We decompose the problem into overlapping subproblems using a **DP Table / Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

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
4. **Verification:** The Bitwise OR of the array is `1 OR 2 OR 3 = 3`. 
 Subsequences that are effective are:
 
 `[1, 3]`: The remaining element `[2]` has a Bitwise OR of 2. 
 `[2, 3]`: The remaining element `[1]` has a Bitwise OR of 1. 
 `[1, 2, 3]`: The remaining elements `[]` have a Bitwise OR of 0. 
 
 
 Thus, the total number of effective subsequences is 3.

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
    def countEffective(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        total_or = 0
        for x in nums:
            total_or |= x

        bits = [b for b in range(20) if total_or & (1 << b)]
        d = len(bits)
        size = 1 << d
        full = size - 1

        # Compress each number into the relevant bit positions.
        freq = [0] * size

        for x in nums:
            mask = 0
            for i, b in enumerate(bits):
                if x & (1 << b):
                    mask |= 1 << i
            freq[mask] += 1

        # SOS DP: count elements whose masks are subsets of each mask.
        for i in range(d):
            bit = 1 << i
            for mask in range(size):
                if mask & bit:
                    freq[mask] += freq[mask ^ bit]

        # Powers of 2 modulo MOD.
        pow2 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow2[i] = pow2[i - 1] * 2 % MOD

        # Count subsequences whose removal preserves the original OR.
        ineffective = 0

        for mask in range(size):
            ways = pow2[freq[mask]]

            if (d - mask.bit_count()) % 2 == 0:
                ineffective += ways
            else:
                ineffective -= ways

            ineffective %= MOD

        # All subsequences minus ineffective subsequences.
        return (pow2[n] - ineffective) % MOD
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
- [792. Number of Matching Subsequences](../../0501-1000/0808-number-of-matching-subsequences/)
- [1498. Number of Subsequences That Satisfy the Given Sum Condition](../../1501-2000/1621-number-of-subsequences-that-satisfy-the-given-sum-condition/)
- [1819. Number of Different Subsequences GCDs](../../1501-2000/1947-number-of-different-subsequences-gcds/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-effective-subsequences/)
