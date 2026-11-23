# LeetCode 3742: Maximum Path Score in a Grid

**LeetCode Problem #3742 — Maximum Path Score in a Grid**
Solve LeetCode Maximum Path Score in a Grid using C++ and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Path Score in a Grid |
| LeetCode | #3742 |
| Difficulty | Medium |
| Language | C++ |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an `m x n` grid where each cell contains one of the values 0, 1, or 2. You are also given an integer `k`.

You start from the top-left corner `(0, 0)` and want to reach the bottom-right corner `(m - 1, n - 1)` by moving only **right** or **down**.

Each cell contributes a specific score and incurs an associated cost, according to their cell values:

0: adds 0 to your score and costs 0. 
 1: adds 1 to your score and costs 1. 
 2: adds 2 to your score and costs 1. ​​​​​​​

Return the **maximum** score achievable without exceeding a total cost of `k`, or -1 if no valid path exists.

**Note:** If you reach the last cell but the total cost exceeds `k`, the path is invalid.

## Constraints
- `1 <= m, n <= 200`
- `0 <= k <= 10^3​​​​​​​`
- `^​​​​​​​grid[0][0] == 0`
- `0 <= grid[i][j] <= 2`

## Examples
### Example 1
- **Input:** `grid = [[0, 1],[2, 0]], k = 1`
- **Output:** `2`
- **Explanation:** ​​​​​​​ 

 The optimal path is: 

 
 
 
 Cell 
 grid[i][j] 
 Score 
 Total 
 Score 
 Cost 
 Total 
 Cost 
 
 
 
 
 (0, 0) 
 0 
 0 
 0 
 0 
 0 
 
 
 (1, 0) 
 2 
 2 
 2 
 1 
 1 
 
 
 (1, 1) 
 0 
 0 
 2 
 0 
 1 
 
 
 

 Thus, the maximum possible score is 2.

### Example 2
- **Input:** `grid = [[0, 1],[1, 2]], k = 1`
- **Output:** `-1`
- **Explanation:** There is no path that reaches cell `(1, 1)`​​​​​​​ without exceeding cost k. Thus, the answer is -1.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Maximum Path Score in a Grid**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [[0, 1],[2, 0]], k = 1`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** ​​​​​​​ 

 The optimal path is: 

 
 
 
 Cell 
 grid[i][j] 
 Score 
 Total 
 Score 
 Cost 
 Total 
 Cost 
 
 
 
 
 (0, 0) 
 0 
 0 
 0 
 0 
 0 
 
 
 (1, 0) 
 2 
 2 
 2 
 1 
 1 
 
 
 (1, 1) 
 0 
 0 
 2 
 0 
 1 
 
 
 

 Thus, the maximum possible score is 2.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)


```cpp
class Solution {
public:
    int maxPathScore(vector<vector<int>>& grid, int k) {
        int m = grid.size();
        int n = grid[0].size();

        int K = min(k, m + n - 1);

        // dp[j][c] = maximum score at column j
        // using exactly cost c.
        vector<vector<int>> dp(n, vector<int>(K + 1, -1));

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {

                int value = grid[i][j];
                int cost = (value == 0 ? 0 : 1);
                int score = value;

                vector<int> cur(K + 1, -1);

                // Starting cell
                if (i == 0 && j == 0) {
                    if (cost <= K)
                        cur[cost] = score;
                } 
                else {
                    // From top
                    for (int c = cost; c <= K; c++) {
                        if (dp[j][c - cost] != -1) {
                            cur[c] = max(
                                cur[c],
                                dp[j][c - cost] + score
                            );
                        }
                    }

                    // From left
                    if (j > 0) {
                        for (int c = cost; c <= K; c++) {
                            if (dp[j - 1][c - cost] != -1) {
                                cur[c] = max(
                                    cur[c],
                                    dp[j - 1][c - cost] + score
                                );
                            }
                        }
                    }
                }

                dp[j] = move(cur);
            }
        }

        int ans = -1;

        for (int c = 0; c <= K; c++) {
            ans = max(ans, dp[n - 1][c]);
        }

        return ans;
    }
};
```

## Why This Works
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [3276. Select Cells in Grid With Maximum Score](../../3501-4000/3563-select-cells-in-grid-with-maximum-score/)
- [1255. Maximum Score Words Formed by Letters](../../1001-1500/1381-maximum-score-words-formed-by-letters/)
- [1422. Maximum Score After Splitting a String](../../1501-2000/1537-maximum-score-after-splitting-a-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-path-score-in-a-grid/)
