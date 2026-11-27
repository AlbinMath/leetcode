# LeetCode 1713: Minimum Operations to Make a Subsequence

**LeetCode Problem #1713 — Minimum Operations to Make a Subsequence**
Solve LeetCode Minimum Operations to Make a Subsequence using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Operations to Make a Subsequence |
| LeetCode | #1713 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an array `target` that consists of **distinct** integers and another integer array `arr` that **can** have duplicates.

In one operation, you can insert any integer at any position in `arr`. For example, if `arr = [1,4,1,2]`, you can add `3` in the middle and make it `[1,4, 3 ,1,2]`. Note that you can insert the integer at the very beginning or end of the array.

Return *the **minimum** number of operations needed to make *`target`* a **subsequence** of *`arr`*.*

A **subsequence** of an array is a new array generated from the original array by deleting some elements (possibly none) without changing the remaining elements' relative order. For example, `[2,7,4]` is a subsequence of `[4, 2 ,3, 7 ,2,1, 4 ]` (the underlined elements), while `[2,4,2]` is not.

## Constraints
- `1 <= target.length, arr.length <= 10^5`
- `1 <= target[i], arr[i] <= 10^9`
- `target` contains no duplicates.

## Examples
### Example 1
- **Input:** `target = [5,1,3], `arr` = [9,4,2,3,4]`
- **Output:** `2`
- **Explanation:** You can add 5 and 1 in such a way that makes `arr` = [ 5 ,9,4, 1 ,2,3,4], then target will be a subsequence of `arr`.

### Example 2
- **Input:** `target = [6,4,8,1,3,2], `arr` = [4,7,6,2,3,8,6,1]`
- **Output:** `3`

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Minimum Operations to Make a Subsequence**, we observe the problem requirements and utilize the **Dynamic Programming** technique. We decompose the problem into overlapping subproblems using a **DP Table / Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `target = [5,1,3], `arr` = [9,4,2,3,4]`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** You can add 5 and 1 in such a way that makes `arr` = [ 5 ,9,4, 1 ,2,3,4], then target will be a subsequence of `arr`.

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
from bisect import bisect_left
from typing import List

class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        pos = {v: i for i, v in enumerate(target)}
        tails = []

        for v in arr:
            if v in pos:
                p = pos[v]
                k = bisect_left(tails, p)
                if k == len(tails):
                    tails.append(p)
                else:
                    tails[k] = p

        return len(target) - len(tails)
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
- [2835. Minimum Operations to Form Subsequence With Target Sum](../../2501-3000/2835-minimum-operations-to-form-subsequence-with-target-sum/)
- [1551. Minimum Operations to Make Array Equal](../../1501-2000/1551-minimum-operations-to-make-array-equal/)
- [1611. Minimum One Bit Operations to Make Integers Zero](../../1501-2000/1611-minimum-one-bit-operations-to-make-integers-zero/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-operations-to-make-a-subsequence/)
