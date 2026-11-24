# LeetCode 2660: Determine the Winner of a Bowling Game

**LeetCode Problem #2660 — Determine the Winner of a Bowling Game**
Solve LeetCode Determine the Winner of a Bowling Game using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Determine the Winner of a Bowling Game |
| LeetCode | #2660 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two **0-indexed** integer arrays ` player1 ` and `player2`, representing the number of pins that player 1 and player 2 hit in a bowling game, respectively.

The bowling game consists of `n` turns, and the number of pins in each turn is exactly 10.

Assume a player hits `x_i` pins in the i^th turn. The value of the i^th turn for the player is:

`2x_i` if the player hits 10 pins in either (i - 1)^th or (i - 2)^th turn . 
 Otherwise, it is `x_i`.

The **score** of the player is the sum of the values of their `n` turns.

Return

1 if the score of player 1 is more than the score of player 2, 
 2 if the score of player 2 is more than the score of player 1, and 
 0 in case of a draw.

## Constraints
- `n == player1.length == player2.length`
- `1 <= n <= 1000`
- `0 <= player1[i], player2[i] <= 10`

## Examples
### Example 1
- **Input:** `player1 = [5,10,3,2], player2 = [6,5,7,3]`
- **Output:** `1`
- **Explanation:** The score of player 1 is 5 + 10 + 2*3 + 2*2 = 25. 

 The score of player 2 is 6 + 5 + 7 + 3 = 21.

### Example 2
- **Input:** `player1 = [3,5,7,6], player2 = [8,10,10,2]`
- **Output:** `2`
- **Explanation:** The score of player 1 is 3 + 5 + 7 + 6 = 21. 

 The score of player 2 is 8 + 10 + 2*10 + 2*2 = 42.

### Example 3
- **Input:** `player1 = [2,3], player2 = [4,1]`
- **Output:** `0`
- **Explanation:** The score of player1 is 2 + 3 = 5. 

 The score of player2 is 4 + 1 = 5.

### Example 4
- **Input:** `player1 = [1,1,1,10,10,10,10], player2 = [10,10,10,10,1,1,1]`
- **Output:** `2`
- **Explanation:** The score of player1 is 1 + 1 + 1 + 10 + 2*10 + 2*10 + 2*10 = 73. 

 The score of player2 is 10 + 2*10 + 2*10 + 2*10 + 2*1 + 2*1 + 1 = 75.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Determine the Winner of a Bowling Game**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `player1 = [5,10,3,2], player2 = [6,5,7,3]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** The score of player 1 is 5 + 10 + 2*3 + 2*2 = 25. 

 The score of player 2 is 6 + 5 + 7 + 3 = 21.

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
var isWinner = function(player1, player2) {
    const calcScore = (pins) => {
        let total = 0;
        for (let i = 0; i < pins.length; i++) {
            const hasStrikeBonus = (i >= 1 && pins[i - 1] === 10) || (i >= 2 && pins[i - 2] === 10);
            total += hasStrikeBonus ? 2 * pins[i] : pins[i];
        }
        return total;
    };

    const score1 = calcScore(player1);
    const score2 = calcScore(player2);

    if (score1 > score2) return 1;
    if (score2 > score1) return 2;
    return 0;
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
- [1275. Find Winner on a Tic Tac Toe Game](../../1001-1500/1275-find-winner-on-a-tic-tac-toe-game/)
- [1535. Find the Winner of an Array Game](../../1501-2000/1535-find-the-winner-of-an-array-game/)
- [1823. Find the Winner of the Circular Game](../../1501-2000/1823-find-the-winner-of-the-circular-game/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/determine-the-winner-of-a-bowling-game/)
