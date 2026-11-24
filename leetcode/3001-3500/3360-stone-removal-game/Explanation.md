# LeetCode 3360: Stone Removal Game

**LeetCode Problem #3360 — Stone Removal Game**
Solve LeetCode Stone Removal Game using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Stone Removal Game |
| LeetCode | #3360 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Alice and Bob are playing a game where they take turns removing stones from a pile, with *Alice going first*.

Alice starts by removing **exactly** 10 stones on her first turn. 
 For each subsequent turn, each player removes **exactly** 1 fewer** **stone** **than the previous opponent.

The player who cannot make a move loses the game.

Given a positive integer `n`, return `true` if Alice wins the game and `false` otherwise.

## Constraints
- `1 <= n <= 50`

## Examples
### Example 1
- **Input:** `n = 12`
- **Output:** `true`
- **Explanation:** Alice removes 10 stones on her first turn, leaving 2 stones for Bob. 
 Bob cannot remove 9 stones, so Alice wins.

### Example 2
- **Input:** `n = 1`
- **Output:** `false`
- **Explanation:** Alice cannot remove 10 stones, so Alice loses.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Stone Removal Game**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 12`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** Alice removes 10 stones on her first turn, leaving 2 stones for Bob. 
 Bob cannot remove 9 stones, so Alice wins.

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
var canAliceWin = function(n) {
    let stonesNeeded = 10;
    let isAliceTurn = true;

    while (n >= stonesNeeded && stonesNeeded > 0) {
        n -= stonesNeeded;
        stonesNeeded--;
        isAliceTurn = !isAliceTurn;
    }

    return !isAliceTurn;
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
- [877. Stone Game](../../0501-1000/0877-stone-game/)
- [1140. Stone Game II](../../1001-1500/1140-stone-game-ii/)
- [1406. Stone Game III](../../1001-1500/1406-stone-game-iii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/stone-removal-game/)
