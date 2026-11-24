# LeetCode 2555: Maximize Win From Two Segments

**LeetCode Problem #2555 — Maximize Win From Two Segments**
Solve LeetCode Maximize Win From Two Segments using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximize Win From Two Segments |
| LeetCode | #2555 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
There are some prizes on the **X-axis**. You are given an integer array `prizePositions` that is **sorted in non-decreasing order**, where `prizePositions[i]` is the position of the `i^th` prize. There could be different prizes at the same position on the line. You are also given an integer `k`.

You are allowed to select two segments with integer endpoints. The length of each segment must be `k`. You will collect all prizes whose position falls within at least one of the two selected segments (including the endpoints of the segments). The two selected segments may intersect.

For example if `k = 2`, you can choose segments `[1, 3]` and `[2, 4]`, and you will win any prize i that satisfies `1 <= prizePositions[i] <= 3` or `2 <= prizePositions[i] <= 4`.

Return *the **maximum** number of prizes you can win if you choose the two segments optimally*.

## Constraints
- `1 <= prizePositions.length <= 10^5`
- `1 <= prizePositions[i] <= 10^9`
- `0 <= k <= 10^9 `
- `prizePositions` is sorted in non-decreasing order.

## Examples
### Example 1
- **Input:** `prizePositions = [1,1,2,2,3,3,5], k = 2`
- **Output:** `7`
- **Explanation:** In this example, you can win all 7 prizes by selecting two segments [1, 3] and [3, 5].

### Example 2
- **Input:** `prizePositions = [1,2,3,4], k = 0`
- **Output:** `2`
- **Explanation:** For this example,

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Maximize Win From Two Segments**, we observe the problem requirements and utilize the **Dynamic Programming** technique. We decompose the problem into overlapping subproblems using a **DP Table / Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `prizePositions = [1,1,2,2,3,3,5], k = 2`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `7`.
4. **Verification:** In this example, you can win all 7 prizes by selecting two segments [1, 3] and [3, 5].

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
from typing import List

class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        n = len(prizePositions)
        best_prefix = [0] * (n + 1)
        
        left = 0
        max_prizes = 0
        
        for right, pos in enumerate(prizePositions):
            while pos - prizePositions[left] > k:
                left += 1
                
            curr_win = right - left + 1
            if curr_win + best_prefix[left] > max_prizes:
                max_prizes = curr_win + best_prefix[left]
                
            best_prefix[right + 1] = max(best_prefix[right], curr_win)
            
        return max_prizes
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
- [884. Uncommon Words from Two Sentences](../../0501-1000/0920-uncommon-words-from-two-sentences/)
- [1771. Maximize Palindrome Length From Subsequences](../../1501-2000/1897-maximize-palindrome-length-from-subsequences/)
- [2259. Remove Digit From Number to Maximize Result](../../2001-2500/2337-remove-digit-from-number-to-maximize-result/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximize-win-from-two-segments/)
