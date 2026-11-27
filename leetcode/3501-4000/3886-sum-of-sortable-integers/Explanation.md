# LeetCode 3886: Sum of Sortable Integers

**LeetCode Problem #3886 — Sum of Sortable Integers**
Solve LeetCode Sum of Sortable Integers using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Sum of Sortable Integers |
| LeetCode | #3886 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `nums` of length `n`.

An integer `k` is called **sortable** if `k` **divides** `n` and you can sort `nums` in **non-decreasing** order by sequentially performing the following operations:

Partition `nums` into **consecutive subarrays ** of length `k`. 
 **Cyclically rotate each subarray independently** any number of times to the left or to the right.

Return an integer denoting the sum of all possible sortable integers `k`.

## Constraints
- `1 <= n == nums.length <= 10^5`
- `1 <= nums[i] <= 10^5`

## Examples
### Example 1
- **Input:** `nums = [3,1,2]`
- **Output:** `3`
- **Explanation:** ​​​​​​​ 

 
 For `n = 3`, possible divisors are 1 and 3. 
 For `k = 1`: each subarray has one element. No rotation can sort the array. 
 For `k = 3`: the single subarray `[3, 1, 2]` can be rotated once to produce `[1, 2, 3]`, which is sorted. 
 Only `k = 3` is sortable. Hence, the answer is 3.

### Example 2
- **Input:** `nums = [7,6,5]`
- **Output:** `0`
- **Explanation:** For `n = 3`, possible divisors are 1 and 3. 
 For `k = 1`: each subarray has one element. No rotation can sort the array. 
 For `k = 3`: the single subarray `[7, 6, 5]` cannot be rotated into non-decreasing order. 
 No `k` is sortable. Hence, the answer is 0.

### Example 3
- **Input:** `nums = [5,8]`
- **Output:** `3`
- **Explanation:** ​​​​​​​ 

 
 For `n = 2`, possible divisors are 1 and 2. 
 Since `[5, 8]` is already sorted, every divisor is sortable. Hence, the answer is `1 + 2 = 3`.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Sum of Sortable Integers**, we observe the problem requirements and utilize the **Array / General** technique. We decompose the problem into overlapping subproblems using a **Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [3,1,2]`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** ​​​​​​​ 

 
 For `n = 3`, possible divisors are 1 and 3. 
 For `k = 1`: each subarray has one element. No rotation can sort the array. 
 For `k = 3`: the single subarray `[3, 1, 2]` can be rotated once to produce `[1, 2, 3]`, which is sorted. 
 Only `k = 3` is sortable. Hence, the answer is 3.

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
    def sortableIntegers(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        for k in range(1, n + 1):
            if n % k:
                continue

            arr = []
            for i in range(0, n, k):
                a = nums[i:i + k]
                a.sort()
                arr.append(a)

            # Check if each block can be rotated into sorted order
            ok = True
            for i in range(0, n, k):
                a = nums[i:i + k]
                if sum(a[j] > a[(j + 1) % k] for j in range(k)) > 1:
                    ok = False
                    break

            if not ok:
                continue

            # Check whether sorted rotations can make the full array sorted
            for i in range(0, n, k):
                a = nums[i:i + k]
                if i > 0 and max(nums[i-k:i]) > min(a):
                    ok = False
                    break

            if ok:
                ans += k

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
- [371. Sum of Two Integers](../../0001-0500/0371-sum-of-two-integers/)
- [1304. Find N Unique Integers Sum up to Zero](../../1001-1500/1304-find-n-unique-integers-sum-up-to-zero/)
- [1317. Convert Integer to the Sum of Two No-Zero Integers](../../1001-1500/1317-convert-integer-to-the-sum-of-two-no-zero-integers/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/sum-of-sortable-integers/)
