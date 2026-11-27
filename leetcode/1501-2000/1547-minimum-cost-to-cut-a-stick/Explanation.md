# LeetCode 1547: Minimum Cost to Cut a Stick

**LeetCode Problem #1547 — Minimum Cost to Cut a Stick**
Solve LeetCode Minimum Cost to Cut a Stick using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Cost to Cut a Stick |
| LeetCode | #1547 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a wooden stick of length `n` units. The stick is labelled from `0` to `n`. For example, a stick of length **6** is labelled as follows:

Given an integer array `cuts` where `cuts[i]` denotes a position you should perform a cut at.

You should perform the cuts in order, you can change the order of the cuts as you wish.

The cost of one cut is the length of the stick to be cut, the total cost is the sum of costs of all cuts. When you cut a stick, it will be split into two smaller sticks (i.e. the sum of their lengths is the length of the stick before the cut). Please refer to the first example for a better explanation.

Return *the minimum total cost* of the cuts.

## Constraints
- `2 <= n <= 10^6`
- `1 <= cuts.length <= min(n - 1, 100)`
- `1 <= cuts[i] <= n - 1`
- All the integers in `cuts` array are **distinct**.

## Examples
### Example 1
- **Input:** `n = 7, cuts = [1,3,4,5]`
- **Output:** `16`
- **Explanation:** Using cuts order = [1, 3, 4, 5] as in the input leads to the following scenario:
 
The first cut is done to a rod of length 7 so the cost is 7. The second cut is done to a rod of length 6 (i.e. the second part of the first cut), the third is done to a rod of length 4 and the last cut is to a rod of length 3. The total cost is 7 + 6 + 4 + 3 = 20.
Rearranging the cuts to be [3, 5, 1, 4] for example will lead to a scenario with total cost = 16 (as shown in the example photo 7 + 4 + 3 + 2 = 16).

### Example 2
- **Input:** `n = 9, cuts = [5,6,1,4,2]`
- **Output:** `22`
- **Explanation:** If you try the given cuts ordering the cost will be 25.
There are much ordering with total cost <= 25, for example, the order [4, 6, 5, 2, 1] has total cost = 22 which is the minimum possible.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Cost to Cut a Stick**, we observe the problem requirements and utilize the **Array / General** technique. We decompose the problem into overlapping subproblems using a **Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 7, cuts = [1,3,4,5]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `16`.
4. **Verification:** Using cuts order = [1, 3, 4, 5] as in the input leads to the following scenario:
 
The first cut is done to a rod of length 7 so the cost is 7. The second cut is done to a rod of length 6 (i.e. the second part of the first cut), the third is done to a rod of length 4 and the last cut is to a rod of length 3. The total cost is 7 + 6 + 4 + 3 = 20.
Rearranging the cuts to be [3, 5, 1, 4] for example will lead to a scenario with total cost = 16 (as shown in the example photo 7 + 4 + 3 + 2 = 16).

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var minCost = function(n, cuts) {
    cuts.push(0, n);

    cuts.sort((a, b) => a - b);

    const m = cuts.length;

    const dp = Array.from({ length: m }, () =>
        new Array(m).fill(0)
    );
    for (let len = 2; len < m; len++) {
        for (let i = 0; i + len < m; i++) {
            const j = i + len;

            dp[i][j] = Infinity;
            for (let k = i + 1; k < j; k++) {
                const cost = cuts[j] - cuts[i]
                           + dp[i][k]
                           + dp[k][j];

                dp[i][j] = Math.min(dp[i][j], cost);
            }
        }
    }

    return dp[0][m - 1];
};
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
- [857. Minimum Cost to Hire K Workers](../../0501-1000/0857-minimum-cost-to-hire-k-workers/)
- [1000. Minimum Cost to Merge Stones](../../0501-1000/1000-minimum-cost-to-merge-stones/)
- [1130. Minimum Cost Tree From Leaf Values](../../1001-1500/1130-minimum-cost-tree-from-leaf-values/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-cost-to-cut-a-stick/)
