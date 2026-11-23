# LeetCode 2770: Maximum Number of Jumps to Reach the Last Index

**LeetCode Problem #2770 — Maximum Number of Jumps to Reach the Last Index**
Solve LeetCode Maximum Number of Jumps to Reach the Last Index using C++ and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Number of Jumps to Reach the Last Index |
| LeetCode | #2770 |
| Difficulty | Medium |
| Language | C++ |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a **0-indexed** array `nums` of `n` integers and an integer `target`.

You are initially positioned at index `0`. In one step, you can jump from index `i` to any index `j` such that:

`0 <= i < j < n` 
 `-target <= nums[j] - nums[i] <= target`

Return *the **maximum number of jumps** you can make to reach index* `n - 1`.

If there is no way to reach index `n - 1`, return `-1`.

## Constraints
- `2 <= nums.length == n <= 1000`
- `-10^9 <= nums[i] <= 10^9`
- `0 <= target <= 2 * 10^9`

## Examples
### Example 1
- **Input:** `nums = [1,3,6,4,1,2], target = 2`
- **Output:** `3`
- **Explanation:** To go from index 0 to index n - 1 with the maximum number of jumps, you can perform the following jumping sequence:
- Jump from index 0 to index 1. 
- Jump from index 1 to index 3.
- Jump from index 3 to index 5.
It can be proven that there is no other jumping sequence that goes from 0 to n - 1 with more than 3 jumps. Hence, the answer is 3.

### Example 2
- **Input:** `nums = [1,3,6,4,1,2], target = 3`
- **Output:** `5`
- **Explanation:** To go from index 0 to index n - 1 with the maximum number of jumps, you can perform the following jumping sequence:
- Jump from index 0 to index 1.
- Jump from index 1 to index 2.
- Jump from index 2 to index 3.
- Jump from index 3 to index 4.
- Jump from index 4 to index 5.
It can be proven that there is no other jumping sequence that goes from 0 to n - 1 with more than 5 jumps. Hence, the answer is 5.

### Example 3
- **Input:** `nums = [1,3,6,4,1,2], target = 0`
- **Output:** `-1`
- **Explanation:** It can be proven that there is no jumping sequence that goes from 0 to n - 1. Hence, the answer is -1.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
Uses **DP** where `dp[i]` = max jumps to reach index `i`. For each `i`, check all `j < i` where the jump is valid and update `dp[i] = max(dp[i], dp[j] + 1)`. Return `dp[n-1]` or -1 if unreachable.

## Algorithm
1. Initialize state variables / data structure (**DP Table / Array**).
2. Process elements sequentially using **Memoization & State Transition**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,3,6,4,1,2], target = 2`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** To go from index 0 to index n - 1 with the maximum number of jumps, you can perform the following jumping sequence:
- Jump from index 0 to index 1. 
- Jump from index 1 to index 3.
- Jump from index 3 to index 5.
It can be proven that there is no other jumping sequence that goes from 0 to n - 1 with more than 3 jumps. Hence, the answer is 3.

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
    int maximumJumps(vector<int>& nums, int target) {
        int n = nums.size();

        vector<int> dp(n, -1);
        dp[0] = 0;

        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                long long diff = (long long)nums[i] - nums[j];

                if (dp[j] != -1 && abs(diff) <= target) {
                    dp[i] = max(dp[i], dp[j] + 1);
                }
            }
        }

        return dp[n - 1];
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
- [1654. Minimum Jumps to Reach Home](../../1501-2000/1757-minimum-jumps-to-reach-home/)
- [3629. Minimum Jumps to Reach End via Prime Teleportation](../../3501-4000/3933-minimum-jumps-to-reach-end-via-prime-teleportation/)
- [321. Create Maximum Number](../../0001-0500/0321-create-maximum-number/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index/)
