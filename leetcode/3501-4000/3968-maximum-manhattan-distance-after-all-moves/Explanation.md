# LeetCode 3968: Maximum Manhattan Distance After All Moves

**LeetCode Problem #3968 — Maximum Manhattan Distance After All Moves**
Solve LeetCode Maximum Manhattan Distance After All Moves using JavaScript and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Manhattan Distance After All Moves |
| LeetCode | #3968 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string `moves` consisting of the characters `'U'`, `'D'`, `'L'`, `'R'`, and `'_'`.

Starting from the origin `(0, 0)`, each character represents one move on a 2D plane:

`'U'`: Move up by 1 unit. 
 `'D'`: Move down by 1 unit. 
 `'L'`: Move left by 1 unit. 
 `'R'`: Move right by 1 unit. 
 `'_'`: Can be independently replaced with any one of `'U'`, `'D'`, `'L'`, or `'R'`.

Return the maximum **Manhattan distance** from the origin that can be achieved after all moves have been performed.

## Constraints
- `1 <= moves.length <= 10^5`
- `moves` consists of only `'U'`, `'D'`, `'L'`, `'R'`, and `'_'`.

## Examples
### Example 1
- **Input:** `moves = "L_D_"`
- **Output:** `4`
- **Explanation:** One optimal choice is: 

 
 `'L'`: `(0, 0) -> (-1, 0)` 
 `'_'` treated as `'D'`: `(-1, 0) -> (-1, -1)` 
 `'D'`: `(-1, -1) -> (-1, -2)` 
 `'_'` treated as `'L'`: `(-1, -2) -> (-2, -2)` 
 

 The final Manhattan distance from the origin is `|0 - (-2)| + |0 - (-2)| = 4`.

### Example 2
- **Input:** `moves = "U_R"`
- **Output:** `3`
- **Explanation:** One optimal choice is: 

 
 `'U'`: `(0, 0) -> (0, 1)` 
 `'_'` treated as `'U'`: `(0, 1) -> (0, 2)` 
 `'R'`: `(0, 2) -> (1, 2)` 
 

 The final Manhattan distance from the origin is `|0 - 1| + |0 - 2| = 3`.

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Manhattan Distance After All Moves**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `moves = "L_D_"`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** One optimal choice is: 

 
 `'L'`: `(0, 0) -> (-1, 0)` 
 `'_'` treated as `'D'`: `(-1, 0) -> (-1, -1)` 
 `'D'`: `(-1, -1) -> (-1, -2)` 
 `'_'` treated as `'L'`: `(-1, -2) -> (-2, -2)` 
 

 The final Manhattan distance from the origin is `|0 - (-2)| + |0 - (-2)| = 4`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Primitive Types.

## Pattern
**Math & Logic**

## Topics
- Math
- Simulation

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var maxDistance = function(moves) {
    let x = 0;
    let y = 0;
    let wildcards = 0;

    for (const move of moves) {
        if (move === 'U') {
            y++;
        } else if (move === 'D') {
            y--;
        } else if (move === 'R') {
            x++;
        } else if (move === 'L') {
            x--;
        } else {
            wildcards++;
        }
    }

    return Math.abs(x) + Math.abs(y) + wildcards;
};
```

## Why This Works
By utilizing **Math & Logic**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [3443. Maximum Manhattan Distance After K Changes](../../3001-3500/3443-maximum-manhattan-distance-after-k-changes/)
- [2920. Maximum Points After Collecting Coins From All Nodes](../../2501-3000/2920-maximum-points-after-collecting-coins-from-all-nodes/)
- [3283. Maximum Number of Moves to Kill All Pawns](../../3001-3500/3283-maximum-number-of-moves-to-kill-all-pawns/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-manhattan-distance-after-all-moves/)
