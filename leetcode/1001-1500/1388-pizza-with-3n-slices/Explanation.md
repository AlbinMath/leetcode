# LeetCode 1388: Pizza With 3n Slices

**LeetCode Problem #1388 — Pizza With 3n Slices**
Solve LeetCode Pizza With 3n Slices using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Pizza With 3n Slices |
| LeetCode | #1388 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There is a pizza with `3n` slices of varying size, you and your friends will take slices of pizza as follows:

You will pick **any** pizza slice. 
 Your friend Alice will pick the next slice in the anti-clockwise direction of your pick. 
 Your friend Bob will pick the next slice in the clockwise direction of your pick. 
 Repeat until there are no more slices of pizzas.

Given an integer array `slices` that represent the sizes of the pizza slices in a clockwise direction, return *the maximum possible sum of slice sizes that you can pick*.

## Constraints
- `3 * n == slices.length`
- `1 <= slices.length <= 500`
- `1 <= slices[i] <= 1000`

## Examples
### Example 1
- **Input:** `slices = [1,2,3,4,5,6]`
- **Output:** `10`
- **Explanation:** Pick pizza slice of size 4, Alice and Bob will pick slices with size 3 and 5 respectively. Then Pick slices with size 6, finally Alice and Bob will pick slice of size 2 and 1 respectively. Total = 4 + 6.

### Example 2
- **Input:** `slices = [8,9,8,6,1,1]`
- **Output:** `16`
- **Explanation:** Pick pizza slice of size 8 in each turn. If you pick slice with size 9 your partners will pick slices of size 8.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Pizza With 3n Slices**, we observe the problem requirements and utilize the **Array / General** technique. We decompose the problem into overlapping subproblems using a **Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `slices = [1,2,3,4,5,6]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `10`.
4. **Verification:** Pick pizza slice of size 4, Alice and Bob will pick slices with size 3 and 5 respectively. Then Pick slices with size 6, finally Alice and Bob will pick slice of size 2 and 1 respectively. Total = 4 + 6.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List

class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        m = len(slices)
        n = m // 3

        def solve(a: List[int]) -> int:
            L = len(a)
            NEG = float('-inf')
            # dp[i][j]: first i slices, exactly j chosen, no two adjacent
            dp = [[NEG] * (n + 1) for _ in range(L + 1)]
            for i in range(L + 1):
                dp[i][0] = 0
            for i in range(1, L + 1):
                for j in range(1, n + 1):
                    best = dp[i - 1][j]
                    prev = dp[i - 2][j - 1] if i >= 2 else (0 if j == 1 else NEG)
                    if prev != NEG:
                        best = max(best, prev + a[i - 1])
                    dp[i][j] = best
            return dp[L][n]

        return max(solve(slices[:-1]), solve(slices[1:]))
```

## Why This Works
By utilizing **Array / General**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1444. Number of Ways of Cutting a Pizza](../../1001-1500/1444-number-of-ways-of-cutting-a-pizza/)
- [413. Arithmetic Slices](../../0001-0500/0413-arithmetic-slices/)
- [446. Arithmetic Slices II - Subsequence](../../0001-0500/0446-arithmetic-slices-ii-subsequence/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/pizza-with-3n-slices/)
