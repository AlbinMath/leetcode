# LeetCode 1140: Stone Game II

**LeetCode Problem #1140 — Stone Game II**
Solve LeetCode Stone Game II using C++ and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Stone Game II |
| LeetCode | #1140 |
| Difficulty | Medium |
| Language | C++ |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Alice and Bob continue their games with piles of stones. There are a number of piles **arranged in a row**, and each pile has a positive integer number of stones `piles[i]`. The objective of the game is to end with the most stones.

Alice and Bob take turns, with Alice starting first.

On each player's turn, that player can take **all the stones** in the **first** `X` remaining piles, where `1 <= X <= 2M`. Then, we set `M = max(M, X)`. Initially, M = 1.

The game continues until all the stones have been taken.

Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.

## Constraints
- `1 <= piles.length <= 100`
- `1 <= piles[i] <= 10^4`

## Examples
### Example 1
- **Input:** `piles = [2,7,9,4,4]`
- **Output:** `10`
- **Explanation:** If Alice takes one pile at the beginning, Bob takes two piles, then Alice takes 2 piles again. Alice can get `2 + 4 + 4 = 10` stones in total. 
 If Alice takes two piles at the beginning, then Bob can take all three piles left. In this case, Alice get `2 + 7 = 9` stones in total. 
 

 So we return 10 since it's larger.

### Example 2
- **Input:** `piles = [1,2,3,4,5,100]`
- **Output:** `104`

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
The code uses **Bottom-Up DP** with a suffix sum optimization.

1. **Suffix Sum:** `suffix[i]` is the total stones from pile `i` to the end.
2. **DP Definition:** `dp[i][M]` = maximum stones the current player can take from pile `i` onward with the given `M`.
3. **Base Case:** If `i + 2*M >= n`, the player takes all remaining piles: `dp[i][M] = suffix[i]`.
4. **Transition:** Try each valid `X` from `1` to `2*M`:
   - The current player gets `suffix[i] - dp[i+X][max(M,X)]`. This works because `suffix[i]` is the total remaining and `dp[i+X][...]` is what the *opponent* will optimally take.
   - Maximize over all choices of `X`.
5. **Answer:** `dp[0][1]` — Alice starts at pile 0 with M = 1.

Time complexity is $O(N^3)$ and space complexity is $O(N^2)$.

## Algorithm
1. Initialize state variables / data structure (**DP Table / Array**).
2. Process elements sequentially using **Memoization & State Transition**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `piles = [2,7,9,4,4]`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `10`.
4. **Verification:** If Alice takes one pile at the beginning, Bob takes two piles, then Alice takes 2 piles again. Alice can get `2 + 4 + 4 = 10` stones in total. 
 If Alice takes two piles at the beginning, then Bob can take all three piles left. In this case, Alice get `2 + 7 = 9` stones in total. 
 

 So we return 10 since it's larger.

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
    int stoneGameII(vector<int>& piles) {
        int n = piles.size();

        // suffix[i] = sum of piles from i to n-1
        vector<int> suffix(n + 1, 0);

        for (int i = n - 1; i >= 0; i--) {
            suffix[i] = suffix[i + 1] + piles[i];
        }

        vector<vector<int>> dp(n, vector<int>(n + 1, 0));

        // Process from the end
        for (int i = n - 1; i >= 0; i--) {
            for (int M = 1; M <= n; M++) {

                // Can take all remaining piles
                if (i + 2 * M >= n) {
                    dp[i][M] = suffix[i];
                    continue;
                }

                int best = 0;

                // Try taking X piles
                for (int X = 1; X <= 2 * M; X++) {
                    int nextM = max(M, X);

                    // Current player gets X piles,
                    // then opponent gets dp[i+X][nextM].
                    int current =
                        suffix[i] - dp[i + X][nextM];

                    best = max(best, current);
                }

                dp[i][M] = best;
            }
        }

        return dp[0][1];
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
- [877. Stone Game](../../0501-1000/0909-stone-game/)
- [1406. Stone Game III](../../1501-2000/1522-stone-game-iii/)
- [1510. Stone Game IV](../../1501-2000/1617-stone-game-iv/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/stone-game-ii/)
