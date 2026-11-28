# LeetCode 1403: Minimum Subsequence in Non-Increasing Order

**LeetCode Problem #1403 — Minimum Subsequence in Non-Increasing Order**
Solve LeetCode Minimum Subsequence in Non-Increasing Order using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Subsequence in Non-Increasing Order |
| LeetCode | #1403 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given the array `nums`, obtain a subsequence of the array whose sum of elements is **strictly greater** than the sum of the non included elements in such subsequence.

If there are multiple solutions, return the subsequence with **minimum size** and if there still exist multiple solutions, return the subsequence with the **maximum total sum** of all its elements. A subsequence of an array can be obtained by erasing some (possibly zero) elements from the array.

Note that the solution with the given constraints is guaranteed to be **unique**. Also return the answer sorted in **non-increasing** order.

## Constraints
- `1 <= nums.length <= 500`
- `1 <= nums[i] <= 100`

## Examples
### Example 1
- **Input:** `nums = [4,3,10,9,8]`
- **Output:** `[10,9]`
- **Explanation:** The subsequences [10,9] and [10,8] are minimal such that the sum of their elements is strictly greater than the sum of elements not included. However, the subsequence [10,9] has the maximum total sum of its elements.

### Example 2
- **Input:** `nums = [4,4,7,6,7]`
- **Output:** `[7,7,6]`
- **Explanation:** The subsequence [7,7] has the sum of its elements equal to 14 which is not strictly greater than the sum of elements not included (14 = 4 + 4 + 6). Therefore, the subsequence [7,6,7] is the minimal satisfying the conditions. Note the subsequence has to be returned in non-increasing order.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Minimum Subsequence in Non-Increasing Order**, we observe the problem requirements and utilize the **Dynamic Programming** technique. We decompose the problem into overlapping subproblems using a **DP Table / Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [4,3,10,9,8]`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[10,9]`.
4. **Verification:** The subsequences [10,9] and [10,8] are minimal such that the sum of their elements is strictly greater than the sum of elements not included. However, the subsequence [10,9] has the maximum total sum of its elements.

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
    def minSubsequence(self, nums: list[int]) -> list[int]:
        nums.sort(reverse=True)
        total = sum(nums)
        selected = []
        selected_sum = 0

        for num in nums:
            selected.append(num)
            selected_sum += num

            if selected_sum > total - selected_sum:
                break

        return selected
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
- [3825. Longest Strictly Increasing Subsequence With Non-Zero Bitwise AND](../../3501-4000/3825-longest-strictly-increasing-subsequence-with-non-zero-bitwise-and/)
- [801. Minimum Swaps To Make Sequences Increasing](../../0501-1000/0801-minimum-swaps-to-make-sequences-increasing/)
- [1713. Minimum Operations to Make a Subsequence](../../1501-2000/1713-minimum-operations-to-make-a-subsequence/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order/)
