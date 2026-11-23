# LeetCode 3702: Longest Subsequence With Non-Zero Bitwise XOR

**LeetCode Problem #3702 — Longest Subsequence With Non-Zero Bitwise XOR**
Solve LeetCode Longest Subsequence With Non-Zero Bitwise XOR using C++ and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest Subsequence With Non-Zero Bitwise XOR |
| LeetCode | #3702 |
| Difficulty | Medium |
| Language | C++ |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `nums`.

Return the length of the **longest subsequence ** in `nums` whose bitwise **XOR** is **non-zero**. If no such **subsequence** exists, return 0.

## Constraints
- `1 <= nums.length <= 10^5`
- `0 <= nums[i] <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [1,2,3]`
- **Output:** `2`
- **Explanation:** One longest subsequence is `[2, 3]`. The bitwise XOR is computed as `2 XOR 3 = 1`, which is non-zero.

### Example 2
- **Input:** `nums = [2,3,4]`
- **Output:** `3`
- **Explanation:** The longest subsequence is `[2, 3, 4]`. The bitwise XOR is computed as `2 XOR 3 XOR 4 = 5`, which is non-zero.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Longest Subsequence With Non-Zero Bitwise XOR**, we observe the problem requirements and utilize the **Dynamic Programming** technique. We decompose the problem into overlapping subproblems using a **DP Table / Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

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
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** One longest subsequence is `[2, 3]`. The bitwise XOR is computed as `2 XOR 3 = 1`, which is non-zero.

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
C++

## Source Code
- [solution.cpp](./solution.cpp)


```cpp
class Solution {
public:
    int longestSubsequence(vector<int>& nums) {
        int xr = 0;

        for (int x : nums) {
            xr ^= x;
        }

        // If total XOR is non-zero, use the entire array
        if (xr != 0)
            return nums.size();

        // Total XOR is zero.
        // Remove one non-zero element to make XOR non-zero.
        for (int x : nums) {
            if (x != 0)
                return nums.size() - 1;
        }

        // All elements are zero
        return 0;
    }
};
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
- [3825. Longest Strictly Increasing Subsequence With Non-Zero Bitwise AND](../../4001-4500/4032-longest-strictly-increasing-subsequence-with-non-zero-bitwise-and/)
- [1787. Make the XOR of All Segments Equal to Zero](../../1501-2000/1913-make-the-xor-of-all-segments-equal-to-zero/)
- [1835. Find XOR Sum of All Pairs Bitwise AND](../../1501-2000/1963-find-xor-sum-of-all-pairs-bitwise-and/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longest-subsequence-with-non-zero-bitwise-xor/)
