# LeetCode 3332: Maximum Points Tourist Can Earn

**LeetCode Problem #3332 — Maximum Points Tourist Can Earn**
Solve LeetCode Maximum Points Tourist Can Earn using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Points Tourist Can Earn |
| LeetCode | #3332 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given two integers, `n` and `k`, along with two 2D integer arrays, `stayScore` and `travelScore`.

A tourist is visiting a country with `n` cities, where each city is **directly** connected to every other city. The tourist's journey consists of **exactly** `k` **0-indexed** days, and they can choose **any** city as their starting point.

Each day, the tourist has two choices:

**Stay in the current city**: If the tourist stays in their current city `curr` during day `i`, they will earn `stayScore[i][curr]` points. 
 **Move to another city**: If the tourist moves from their current city `curr` to city `dest`, they will earn `travelScore[curr][dest]` points.

Return the **maximum** possible points the tourist can earn.

## Constraints
- `1 <= n <= 200`
- `1 <= k <= 200`
- `n == travelScore.length == travelScore[i].length == stayScore[i].length`
- `k == stayScore.length`
- `1 <= stayScore[i][j] <= 100`
- `0 <= travelScore[i][j] <= 100`
- `travelScore[i][i] == 0`

## Examples
### Example 1
- **Input:** `n = 2, k = 1, stayScore = [[2,3]], travelScore = [[0,2],[1,0]]`
- **Output:** `3`
- **Explanation:** The tourist earns the maximum number of points by starting in city 1 and staying in that city.

### Example 2
- **Input:** `n = 3, k = 2, stayScore = [[3,4,2],[2,1,2]], travelScore = [[0,2,1],[2,0,4],[3,2,0]]`
- **Output:** `8`
- **Explanation:** The tourist earns the maximum number of points by starting in city 1, staying in that city on day 0, and traveling to city 2 on day 1.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Maximum Points Tourist Can Earn**, we observe the problem requirements and utilize the **Array / General** technique. We decompose the problem into overlapping subproblems using a **Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 2, k = 1, stayScore = [[2,3]], travelScore = [[0,2],[1,0]]`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** The tourist earns the maximum number of points by starting in city 1 and staying in that city.

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
    def maxScore(self, n: int, k: int, stayScore: List[List[int]], travelScore: List[List[int]]) -> int:
        dp = [0] * n

        for day in range(k):
            new = [0] * n
            for c in range(n):
                best = dp[c] + stayScore[day][c]
                for p in range(n):
                    if p != c:
                        best = max(best, dp[p] + travelScore[p][c])
                new[c] = best
            dp = new

        return max(dp)
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
- [3418. Maximum Amount of Money Robot Can Earn](../../3001-3500/3418-maximum-amount-of-money-robot-can-earn/)
- [1423. Maximum Points You Can Obtain from Cards](../../1001-1500/1423-maximum-points-you-can-obtain-from-cards/)
- [1298. Maximum Candies You Can Get from Boxes](../../1001-1500/1298-maximum-candies-you-can-get-from-boxes/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-points-tourist-can-earn/)
