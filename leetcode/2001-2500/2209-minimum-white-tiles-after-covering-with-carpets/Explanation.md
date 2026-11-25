# LeetCode 2209: Minimum White Tiles After Covering With Carpets

**LeetCode Problem #2209 — Minimum White Tiles After Covering With Carpets**
Solve LeetCode Minimum White Tiles After Covering With Carpets using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum White Tiles After Covering With Carpets |
| LeetCode | #2209 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed binary** string `floor`, which represents the colors of tiles on a floor:

`floor[i] = '0'` denotes that the `i^th` tile of the floor is colored **black**. 
 On the other hand, `floor[i] = '1'` denotes that the `i^th` tile of the floor is colored **white**.

You are also given `numCarpets` and `carpetLen`. You have `numCarpets` **black** carpets, each of length `carpetLen` tiles. Cover the tiles with the given carpets such that the number of **white** tiles still visible is **minimum**. Carpets may overlap one another.

Return *the **minimum** number of white tiles still visible.*

## Constraints
- `1 <= carpetLen <= floor.length <= 1000`
- `floor[i]` is either `'0'` or `'1'`.
- `1 <= numCarpets <= 1000`

## Examples
### Example 1
- **Input:** `floor = "10110101", numCarpets = 2, carpetLen = 2`
- **Output:** `2`
- **Explanation:** The figure above shows one way of covering the tiles with the carpets such that only 2 white tiles are visible.
No other way of covering the tiles with the carpets can leave less than 2 white tiles visible.

### Example 2
- **Input:** `floor = "11111", numCarpets = 2, carpetLen = 3`
- **Output:** `0`
- **Explanation:** The figure above shows one way of covering the tiles with the carpets such that no white tiles are visible.
Note that the carpets are able to overlap one another.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum White Tiles After Covering With Carpets**, we observe the problem requirements and utilize the **Array / General** technique. We decompose the problem into overlapping subproblems using a **Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `floor = "10110101", numCarpets = 2, carpetLen = 2`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** The figure above shows one way of covering the tiles with the carpets such that only 2 white tiles are visible.
No other way of covering the tiles with the carpets can leave less than 2 white tiles visible.

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
var minimumWhiteTiles = function(floor, numCarpets, carpetLen) {
    const n = floor.length;
    const dp = Array.from(
        { length: n + 1 },
        () => Array(numCarpets + 1).fill(0)
    );
    for (let i = 1; i <= n; i++) {
        dp[i][0] = dp[i - 1][0] + (floor[i - 1] === '1' ? 1 : 0);
    }
    for (let i = 1; i <= n; i++) {
        for (let k = 1; k <= numCarpets; k++) {
            let noCarpet = dp[i - 1][k];

            if (floor[i - 1] === '1') {
                noCarpet++;
            }
            let useCarpet = dp[Math.max(0, i - carpetLen)][k - 1];
            dp[i][k] = Math.min(noCarpet, useCarpet);
        }
    }

    return dp[n][numCarpets];
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
- [1505. Minimum Possible Integer After at Most K Adjacent Swaps On Digits](../../1501-2000/1505-minimum-possible-integer-after-at-most-k-adjacent-swaps-on-digits/)
- [1750. Minimum Length of String After Deleting Similar Ends](../../1501-2000/1750-minimum-length-of-string-after-deleting-similar-ends/)
- [2322. Minimum Score After Removals on a Tree](../../2001-2500/2322-minimum-score-after-removals-on-a-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-white-tiles-after-covering-with-carpets/)
