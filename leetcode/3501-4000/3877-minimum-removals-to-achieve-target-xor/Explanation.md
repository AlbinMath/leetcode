# LeetCode 3877: Minimum Removals to Achieve Target XOR

**LeetCode Problem #3877 — Minimum Removals to Achieve Target XOR**
Solve LeetCode Minimum Removals to Achieve Target XOR using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Removals to Achieve Target XOR |
| LeetCode | #3877 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `nums` and an integer `target`.

You may remove **any** number of elements from `nums` (possibly zero).

Return the **minimum** number of removals required so that the **bitwise XOR** of the remaining elements equals `target`. If it is impossible to achieve `target`, return -1.

The bitwise XOR of an empty array is 0.

## Constraints
- `1 <= nums.length <= 40`
- `0 <= nums[i] <= 10^4`
- `0 <= target <= 10^4`

## Examples
### Example 1
- **Input:** `nums = [1,2,3], target = 2`
- **Output:** `1`
- **Explanation:** Removing `nums[1] = 2` leaves `[nums[0], nums[2]] = [1, 3]`. 
 The XOR of `[1, 3]` is 2, which equals `target`. 
 It is not possible to achieve XOR = 2 in less than one removal, therefore the answer is 1.

### Example 2
- **Input:** `nums = [2,4], target = 1`
- **Output:** `-1`
- **Explanation:** It is impossible to remove elements to achieve `target`. Thus, the answer is -1.

### Example 3
- **Input:** `nums = [7], target = 7`
- **Output:** `0`
- **Explanation:** The XOR of all elements is `nums[0] = 7`, which equals `target`. Thus, no removal is needed.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Minimum Removals to Achieve Target XOR**, we observe the problem requirements and utilize the **Tree & Graph** technique. We decompose the problem into overlapping subproblems using a **Tree / Graph / Grid**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,3], target = 2`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** Removing `nums[1] = 2` leaves `[nums[0], nums[2]] = [1, 3]`. 
 The XOR of `[1, 3]` is 2, which equals `target`. 
 It is not possible to achieve XOR = 2 in less than one removal, therefore the answer is 1.

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
    def minRemovals(self, nums, target):
        SIZE = 1 << 14
        if target >= SIZE:
            return -1
        NEG = -1
        dp = [NEG] * SIZE
        dp[0] = 0
        for v in nums:
            new = dp[:]
            for x in range(SIZE):
                if dp[x] != NEG:
                    y = x ^ v
                    if dp[x] + 1 > new[y]:
                        new[y] = dp[x] + 1
            dp = new
        if dp[target] == NEG:
            return -1
        return len(nums) - dp[target]
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
- [1879. Minimum XOR Sum of Two Arrays](../../1501-2000/1879-minimum-xor-sum-of-two-arrays/)
- [2997. Minimum Number of Operations to Make Array XOR Equal to K](../../2501-3000/2997-minimum-number-of-operations-to-make-array-xor-equal-to-k/)
- [3882. Minimum XOR Path in a Grid](../../3501-4000/3882-minimum-xor-path-in-a-grid/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-removals-to-achieve-target-xor/)
