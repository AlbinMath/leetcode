# LeetCode 1871: Jump Game VII

**LeetCode Problem #1871 — Jump Game VII**
Solve LeetCode Jump Game VII using C++ and Prefix Sum. This solution finds the optimal result using Prefix Sum Precomputation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Jump Game VII |
| LeetCode | #1871 |
| Difficulty | Medium |
| Language | C++ |
| Algorithm | Prefix Sum Precomputation |
| Data Structure | Prefix Array |
| Pattern | Prefix Sum |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a **0-indexed** binary string `s` and two integers `minJump` and `maxJump`. In the beginning, you are standing at index `0`, which is equal to `'0'`. You can move from index `i` to index `j` if the following conditions are fulfilled:

`i + minJump <= j <= min(i + maxJump, s.length - 1)`, and 
 `s[j] == '0'`.

Return `true` if you can reach index `s.length - 1` in `s`*, or *`false`* otherwise.*

## Constraints
- `2 <= s.length <= 10^5`
- `s[i]` is either `'0'` or `'1'`.
- `s[0] == '0'`
- `1 <= minJump <= maxJump < s.length`

## Examples
### Example 1
- **Input:** `s = " 0 11 0 1 0 ", minJump = 2, maxJump = 3`
- **Output:** `true`
- **Explanation:** In the first step, move from index 0 to index 3. 
In the second step, move from index 3 to index 5.

### Example 2
- **Input:** `s = "01101110", minJump = 2, maxJump = 3`
- **Output:** `false`

## Key Insight
Leverage **Prefix Sum** with **Prefix Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code uses **BFS/DP with a sliding window** to avoid redundant checks. It maintains a window of reachable positions and uses a prefix sum or queue to efficiently determine which new positions can be reached within the `[minJump, maxJump]` range.

Time complexity is $O(N)$ and space complexity is $O(N)$.

## Algorithm
1. Initialize state variables / data structure (**Prefix Array**).
2. Process elements sequentially using **Prefix Sum Precomputation**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `s = " 0 11 0 1 0 ", minJump = 2, maxJump = 3`.
2. **Processing Steps:** We apply **Prefix Sum Precomputation** using our **Prefix Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** In the first step, move from index 0 to index 3. 
In the second step, move from index 3 to index 5.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Prefix Array.

## Pattern
**Prefix Sum**

## Topics
- Prefix Sum
- Array

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)


```cpp
class Solution {
public:
    bool canReach(string s, int minJump, int maxJump) {
        int n = s.size();

        vector<bool> dp(n, false);
        dp[0] = true;

        int reachable = 0;

        for (int i = 1; i < n; i++) {

            // Add the new index entering the window
            int add = i - minJump;
            if (add >= 0 && dp[add])
                reachable++;

            // Remove the index leaving the window
            int remove = i - maxJump - 1;
            if (remove >= 0 && dp[remove])
                reachable--;
            if (s[i] == '0' && reachable > 0)
                dp[i] = true;
        }

        return dp[n - 1];
    }
};
```

## Why This Works
By utilizing **Prefix Sum**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [45. Jump Game II](../../0001-0500/0045-jump-game-ii/)
- [55. Jump Game](../../0001-0500/0055-jump-game/)
- [1306. Jump Game III](../../1001-1500/1306-jump-game-iii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/jump-game-vii/)
