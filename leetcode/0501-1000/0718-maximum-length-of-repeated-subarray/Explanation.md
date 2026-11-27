# LeetCode 718: Maximum Length of Repeated Subarray

**LeetCode Problem #718 — Maximum Length of Repeated Subarray**
Solve LeetCode Maximum Length of Repeated Subarray using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Length of Repeated Subarray |
| LeetCode | #718 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given two integer arrays `nums1` and `nums2`, return *the maximum length of a subarray that appears in **both** arrays*.

## Constraints
- `1 <= nums1.length, nums2.length <= 1000`
- `0 <= nums1[i], nums2[i] <= 100`

## Examples
### Example 1
- **Input:** `nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]`
- **Output:** `3`
- **Explanation:** The repeated subarray with maximum length is [3,2,1].

### Example 2
- **Input:** `nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]`
- **Output:** `5`
- **Explanation:** The repeated subarray with maximum length is [0,0,0,0,0].

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Maximum Length of Repeated Subarray**, we observe the problem requirements and utilize the **Array / General** technique. We decompose the problem into overlapping subproblems using a **Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** The repeated subarray with maximum length is [3,2,1].

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
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums2)
        dp = [0] * (n + 1)
        best = 0
        for x in nums1:
            for j in range(n, 0, -1):
                if x == nums2[j - 1]:
                    dp[j] = dp[j - 1] + 1
                    if dp[j] > best:
                        best = dp[j]
                else:
                    dp[j] = 0
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
- [1567. Maximum Length of Subarray With Positive Product](../../1501-2000/1567-maximum-length-of-subarray-with-positive-product/)
- [3381. Maximum Subarray Sum With Length Divisible by K](../../3001-3500/3381-maximum-subarray-sum-with-length-divisible-by-k/)
- [3755. Find Maximum Balanced XOR Subarray Length](../../3501-4000/3755-find-maximum-balanced-xor-subarray-length/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-length-of-repeated-subarray/)
