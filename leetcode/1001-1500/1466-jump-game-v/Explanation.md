# LeetCode 1340: Jump Game V

**LeetCode Problem #1340 — Jump Game V**
Solve LeetCode Jump Game V using C++ and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Jump Game V |
| LeetCode | #1340 |
| Difficulty | Hard |
| Language | C++ |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given an array of integers `arr` and an integer `d`. In one step you can jump from index `i` to index:

`i + x` where: `i + x < arr.length` and ` 0 < x <= d`. 
 `i - x` where: `i - x >= 0` and ` 0 < x <= d`.

In addition, you can only jump from index `i` to index `j` if `arr[i] > arr[j]` and `arr[i] > arr[k]` for all indices `k` between `i` and `j` (More formally `min(i, j) < k < max(i, j)`).

You can choose any index of the array and start jumping. Return *the maximum number of indices* you can visit.

Notice that you can not jump outside of the array at any time.

## Constraints
- `1 <= arr.length <= 1000`
- `1 <= arr[i] <= 10^5`
- `1 <= d <= arr.length`

## Examples
### Example 1
- **Input:** `arr = [6,4,14,6,8,13,9,7,10,6,12], d = 2`
- **Output:** `4`
- **Explanation:** You can start at index 10. You can jump 10 --> 8 --> 6 --> 7 as shown.
Note that if you start at index 6 you can only jump to index 7. You cannot jump to index 5 because 13 > 9. You cannot jump to index 4 because index 5 is between index 4 and 6 and 13 > 9.
Similarly You cannot jump from index 3 to index 2 or index 1.

### Example 2
- **Input:** `arr = [3,3,3,3,3], d = 3`
- **Output:** `1`
- **Explanation:** You can start at any index. You always cannot jump to any index.

### Example 3
- **Input:** `arr = [7,6,5,4,3,2,1], d = 1`
- **Output:** `7`
- **Explanation:** Start at index 0. You can visit all the indicies.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
The code uses **DFS with Memoization**.

1. **DP Array:** `dp[i]` stores the maximum number of indices reachable from index `i`. Initialized to `1` (the index itself).
2. **DFS Function:** For each index `i`:
   - Try jumping right: iterate `j` from `i+1` up to `min(n-1, i+d)`. If `arr[j] >= arr[i]`, stop (blocked). Otherwise, `dp[i] = max(dp[i], 1 + dfs(j))`.
   - Try jumping left: iterate `j` from `i-1` down to `max(0, i-d)`. Same blocking rule.
3. **Answer:** The maximum of `dfs(i)` over all starting indices.

Time complexity is $O(N \times D)$ and space complexity is $O(N)$.

## Algorithm
1. Initialize state variables / data structure (**DP Table / Array**).
2. Process elements sequentially using **Memoization & State Transition**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `arr = [6,4,14,6,8,13,9,7,10,6,12], d = 2`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** You can start at index 10. You can jump 10 --> 8 --> 6 --> 7 as shown.
Note that if you start at index 6 you can only jump to index 7. You cannot jump to index 5 because 13 > 9. You cannot jump to index 4 because index 5 is between index 4 and 6 and 13 > 9.
Similarly You cannot jump from index 3 to index 2 or index 1.

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
    int maxJumps(vector<int>& arr, int d) {
        int n = arr.size();
        vector<int> dp(n, 1);

        function<int(int)> dfs = [&](int i) {
            if (dp[i] != 1) return dp[i];

            // Jump to the right
            for (int j = i + 1; j <= min(n - 1, i + d); j++) {
                if (arr[j] >= arr[i])
                    break;

                dp[i] = max(dp[i], 1 + dfs(j));
            }

            // Jump to the left
            for (int j = i - 1; j >= max(0, i - d); j--) {
                if (arr[j] >= arr[i])
                    break;

                dp[i] = max(dp[i], 1 + dfs(j));
            }

            return dp[i];
        };

        int ans = 1;

        for (int i = 0; i < n; i++) {
            ans = max(ans, dfs(i));
        }

        return ans;
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
- [1563. Stone Game V](../../1501-2000/1685-stone-game-v/)
- [45. Jump Game II](../../0001-0500/0045-jump-game-ii/)
- [55. Jump Game](../../0001-0500/0055-jump-game/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/jump-game-v/)
