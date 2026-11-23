# LeetCode 486: Predict the Winner

**LeetCode Problem #486 — Predict the Winner**
Solve LeetCode Predict the Winner using C++ and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Predict the Winner |
| LeetCode | #486 |
| Difficulty | Medium |
| Language | C++ |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `nums`.

Two players are playing a game with this array: Player 1 and Player 2.

Player 1 and Player 2 take turns, with Player 1 starting first. Both players start the game with a score of 0.

At each turn, the current player takes the number at **either end** of the array (i.e., `nums[0]` or `nums[nums.length - 1]`), **removing** it from the array and adding it to their own score. The game ends when there are no more elements in the array.

Return `true` if Player 1's final score is **greater than or equal** to Player 2's final score, and `false` otherwise.

**Note** that a tie counts as a win for Player 1. You may assume that both players play optimally.

## Constraints
- `1 <= nums.length <= 20`
- `0 <= nums[i] <= 10^7`

## Examples
### Example 1
- **Input:** `nums = [1,5,2]`
- **Output:** `false`
- **Explanation:** Player 1 must open by taking either 1 or 2, and both choices lead to the same result. 
 If Player 1 takes 1, the array becomes `[5,2]`. Player 2 takes 5, leaving 2 for Player 1. 
 If Player 1 takes 2, the array becomes `[1,5]`. Player 2 takes 5, leaving 1 for Player 1. 
 Either way, Player 1 finishes with `1 + 2 = 3` and Player 2 finishes with `5`. Player 1 can never win, so return `false`.

### Example 2
- **Input:** `nums = [1,5,233,7]`
- **Output:** `true`
- **Explanation:** Player 1 first takes 1, leaving `[5,233,7]`. Player 2 must then choose between 5 and 7, and no matter which number Player 2 chooses, Player 1 can take 233 on the next turn. 
 Player 1 finishes with a higher score (234) than Player 2 (12), so return `true`.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
The code uses **Interval DP** where `dp[i][j]` represents the maximum score advantage the current player can achieve from the subarray `nums[i..j]`.

1. **Base Case:** `dp[i][i] = nums[i]` — if only one number is left, the current player takes it.
2. **Transition:** For each subarray of length `len` from `2` to `n`:
   - `dp[i][j] = max(nums[i] - dp[i+1][j], nums[j] - dp[i][j-1])`
   - The current player picks either the left (`nums[i]`) or right (`nums[j]`) element. After picking, the opponent becomes the "current player" for the remaining subarray, so we subtract `dp` of the remaining range (since that represents the opponent's advantage).
3. **Result:** `dp[0][n-1] >= 0` means Player 1's advantage over the entire array is non-negative, so Player 1 wins or ties.

Time complexity is $O(N^2)$ and space complexity is $O(N^2)$.

## Algorithm
1. Initialize state variables / data structure (**DP Table / Array**).
2. Process elements sequentially using **Memoization & State Transition**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,5,2]`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `false`.
4. **Verification:** Player 1 must open by taking either 1 or 2, and both choices lead to the same result. 
 If Player 1 takes 1, the array becomes `[5,2]`. Player 2 takes 5, leaving 2 for Player 1. 
 If Player 1 takes 2, the array becomes `[1,5]`. Player 2 takes 5, leaving 1 for Player 1. 
 Either way, Player 1 finishes with `1 + 2 = 3` and Player 2 finishes with `5`. Player 1 can never win, so return `false`.

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
    bool predictTheWinner(vector<int>& nums) {
        int n = nums.size();
        vector<vector<int>> dp(n, vector<int>(n));

        for (int i = 0; i < n; i++)
            dp[i][i] = nums[i];

        for (int len = 2; len <= n; len++) {
            for (int i = 0; i + len - 1 < n; i++) {
                int j = i + len - 1;

                dp[i][j] = max(
                    nums[i] - dp[i + 1][j],
                    nums[j] - dp[i][j - 1]
                );
            }
        }

        return dp[0][n - 1] >= 0;
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
- [1275. Find Winner on a Tic Tac Toe Game](../../1001-1500/1400-find-winner-on-a-tic-tac-toe-game/)
- [1535. Find the Winner of an Array Game](../../1501-2000/1657-find-the-winner-of-an-array-game/)
- [1823. Find the Winner of the Circular Game](../../1501-2000/1951-find-the-winner-of-the-circular-game/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/predict-the-winner/)
