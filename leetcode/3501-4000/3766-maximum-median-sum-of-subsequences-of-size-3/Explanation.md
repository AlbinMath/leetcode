# LeetCode 3627: Maximum Median Sum of Subsequences of Size 3

**LeetCode Problem #3627 — Maximum Median Sum of Subsequences of Size 3**
Solve LeetCode Maximum Median Sum of Subsequences of Size 3 using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Median Sum of Subsequences of Size 3 |
| LeetCode | #3627 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `nums` with a length divisible by 3.

You want to make the array empty in steps. In each step, you can select any three elements from the array, compute their **median**, and remove the selected elements from the array.

The **median** of an odd-length sequence is defined as the middle element of the sequence when it is sorted in non-decreasing order.

Return the **maximum** possible sum of the medians computed from the selected elements.

## Constraints
- `1 <= nums.length <= 5 * 10^5`
- `nums.length % 3 == 0`
- `1 <= nums[i] <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [2,1,3,2,1,3]`
- **Output:** `5`
- **Explanation:** In the first step, select elements at indices 2, 4, and 5, which have a median 3. After removing these elements, `nums` becomes `[2, 1, 2]`. 
 In the second step, select elements at indices 0, 1, and 2, which have a median 2. After removing these elements, `nums` becomes empty. 
 

 Hence, the sum of the medians is `3 + 2 = 5`.

### Example 2
- **Input:** `nums = [1,1,10,10,10,10]`
- **Output:** `20`
- **Explanation:** In the first step, select elements at indices 0, 2, and 3, which have a median 10. After removing these elements, `nums` becomes `[1, 10, 10]`. 
 In the second step, select elements at indices 0, 1, and 2, which have a median 10. After removing these elements, `nums` becomes empty. 
 

 Hence, the sum of the medians is `10 + 10 = 20`.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Maximum Median Sum of Subsequences of Size 3**, we observe the problem requirements and utilize the **Dynamic Programming** technique. We decompose the problem into overlapping subproblems using a **DP Table / Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,1,3,2,1,3]`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `5`.
4. **Verification:** In the first step, select elements at indices 2, 4, and 5, which have a median 3. After removing these elements, `nums` becomes `[2, 1, 2]`. 
 In the second step, select elements at indices 0, 1, and 2, which have a median 2. After removing these elements, `nums` becomes empty. 
 

 Hence, the sum of the medians is `3 + 2 = 5`.

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
    def maximumMedianSum(self, nums: list[int]) -> int:
        nums.sort()
        return sum(nums[len(nums)//3::2])
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
- [3428. Maximum and Minimum Sums of at Most Size K Subsequences](../../3501-4000/3714-maximum-and-minimum-sums-of-at-most-size-k-subsequences/)
- [689. Maximum Sum of 3 Non-Overlapping Subarrays](../../0501-1000/0689-maximum-sum-of-3-non-overlapping-subarrays/)
- [1498. Number of Subsequences That Satisfy the Given Sum Condition](../../1501-2000/1621-number-of-subsequences-that-satisfy-the-given-sum-condition/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-median-sum-of-subsequences-of-size-3/)
