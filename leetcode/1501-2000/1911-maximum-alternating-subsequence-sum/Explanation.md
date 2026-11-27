# LeetCode 1911: Maximum Alternating Subsequence Sum

**LeetCode Problem #1911 — Maximum Alternating Subsequence Sum**
Solve LeetCode Maximum Alternating Subsequence Sum using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Alternating Subsequence Sum |
| LeetCode | #1911 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
The **alternating sum** of a **0-indexed** array is defined as the **sum** of the elements at **even** indices **minus** the **sum** of the elements at **odd** indices.

For example, the alternating sum of `[4,2,5,3]` is `(4 + 5) - (2 + 3) = 4`.

Given an array `nums`, return *the **maximum alternating sum** of any subsequence of *`nums`* (after **reindexing** the elements of the subsequence)*.

A **subsequence** of an array is a new array generated from the original array by deleting some elements (possibly none) without changing the remaining elements' relative order. For example, `[2,7,4]` is a subsequence of `[4, 2 ,3, 7 ,2,1, 4 ]` (the underlined elements), while `[2,4,2]` is not.

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^5`

## Examples
### Example 1
- **Input:** `nums = [ 4 , 2 , 5 ,3]`
- **Output:** `7`
- **Explanation:** It is optimal to choose the subsequence [4,2,5] with alternating sum (4 + 5) - 2 = 7.

### Example 2
- **Input:** `nums = [5,6,7, 8 ]`
- **Output:** `8`
- **Explanation:** It is optimal to choose the subsequence [8] with alternating sum 8.

### Example 3
- **Input:** `nums = [ 6 ,2, 1 ,2,4, 5 ]`
- **Output:** `10`
- **Explanation:** It is optimal to choose the subsequence [6,1,5] with alternating sum (6 + 5) - 1 = 10.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Maximum Alternating Subsequence Sum**, we observe the problem requirements and utilize the **Dynamic Programming** technique. We decompose the problem into overlapping subproblems using a **DP Table / Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [ 4 , 2 , 5 ,3]`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `7`.
4. **Verification:** It is optimal to choose the subsequence [4,2,5] with alternating sum (4 + 5) - 2 = 7.

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
    def maxAlternatingSum(self, nums: list[int]) -> int:
        even = 0  
        odd = 0  
        
        for x in nums:
            even, odd = max(even, odd + x), max(odd, even - x)
            
        return even
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
- [3727. Maximum Alternating Sum of Squares](../../3501-4000/3727-maximum-alternating-sum-of-squares/)
- [2926. Maximum Balanced Subsequence Sum](../../2501-3000/2926-maximum-balanced-subsequence-sum/)
- [3165. Maximum Sum of Subsequence With Non-adjacent Elements](../../3001-3500/3165-maximum-sum-of-subsequence-with-non-adjacent-elements/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-alternating-subsequence-sum/)
