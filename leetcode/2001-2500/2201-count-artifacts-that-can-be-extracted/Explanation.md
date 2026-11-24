# LeetCode 2201: Count Artifacts That Can Be Extracted

**LeetCode Problem #2201 — Count Artifacts That Can Be Extracted**
Solve LeetCode Count Artifacts That Can Be Extracted using JavaScript and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Artifacts That Can Be Extracted |
| LeetCode | #2201 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
There is an `n x n` **0-indexed** grid with some artifacts buried in it. You are given the integer `n` and a **0-indexed **2D integer array `artifacts` describing the positions of the rectangular artifacts where `artifacts[i] = [r1_i, c1_i, r2_i, c2_i]` denotes that the `i^th` artifact is buried in the subgrid where:

`(r1_i, c1_i)` is the coordinate of the **top-left** cell of the `i^th` artifact and 
 `(r2_i, c2_i)` is the coordinate of the **bottom-right** cell of the `i^th` artifact.

You will excavate some cells of the grid and remove all the mud from them. If the cell has a part of an artifact buried underneath, it will be uncovered. If all the parts of an artifact are uncovered, you can extract it.

Given a **0-indexed** 2D integer array `dig` where `dig[i] = [r_i, c_i]` indicates that you will excavate the cell `(r_i, c_i)`, return *the number of artifacts that you can extract*.

The test cases are generated such that:

No two artifacts overlap. 
 Each artifact only covers at most `4` cells. 
 The entries of `dig` are unique.

## Constraints
- `1 <= n <= 1000`
- `1 <= artifacts.length, dig.length <= min(n^2, 10^5)`
- `artifacts[i].length == 4`
- `dig[i].length == 2`
- `0 <= r1_i, c1_i, r2_i, c2_i, r_i, c_i <= n - 1`
- `r1_i <= r2_i`
- `c1_i <= c2_i`
- No two artifacts will overlap.
- The number of cells covered by an artifact is **at most** `4`.
- The entries of `dig` are unique.

## Examples
### Example 1
- **Input:** `n = 2, artifacts = [[0,0,0,0],[0,1,1,1]], dig = [[0,0],[0,1]]`
- **Output:** `1`
- **Explanation:** The different colors represent different artifacts. Excavated cells are labeled with a 'D' in the grid.
There is 1 artifact that can be extracted, namely the red artifact.
The blue artifact has one part in cell (1,1) which remains uncovered, so we cannot extract it.
Thus, we return 1.

### Example 2
- **Input:** `n = 2, artifacts = [[0,0,0,0],[0,1,1,1]], dig = [[0,0],[0,1],[1,1]]`
- **Output:** `2`
- **Explanation:** Both the red and blue artifacts have all parts uncovered (labeled with a 'D') and can be extracted, so we return 2.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Count Artifacts That Can Be Extracted**, we observe the problem requirements and utilize the **Array / General** technique. We decompose the problem into overlapping subproblems using a **Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 2, artifacts = [[0,0,0,0],[0,1,1,1]], dig = [[0,0],[0,1]]`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** The different colors represent different artifacts. Excavated cells are labeled with a 'D' in the grid.
There is 1 artifact that can be extracted, namely the red artifact.
The blue artifact has one part in cell (1,1) which remains uncovered, so we cannot extract it.
Thus, we return 1.

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
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var digArtifacts = function(n, artifacts, dig) {
    // Encode 2D coordinates (r, c) into a unique 1D integer: r * n + c
    const dugCells = new Set();
    for (const [r, c] of dig) {
        dugCells.add(r * n + c);
    }

    let extractableCount = 0;

    for (const [r1, c1, r2, c2] of artifacts) {
        let canExtract = true;

        for (let r = r1; r <= r2; r++) {
            for (let c = c1; c <= c2; c++) {
                if (!dugCells.has(r * n + c)) {
                    canExtract = false;
                    break;
                }
            }
            if (!canExtract) break;
        }

        if (canExtract) {
            extractableCount++;
        }
    }

    return extractableCount;
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
- [3297. Count Substrings That Can Be Rearranged to Contain a String I](../../3001-3500/3297-count-substrings-that-can-be-rearranged-to-contain-a-string-i/)
- [3298. Count Substrings That Can Be Rearranged to Contain a String II](../../3001-3500/3298-count-substrings-that-can-be-rearranged-to-contain-a-string-ii/)
- [1442. Count Triplets That Can Form Two Arrays of Equal XOR](../../1001-1500/1442-count-triplets-that-can-form-two-arrays-of-equal-xor/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-artifacts-that-can-be-extracted/)
