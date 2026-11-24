# LeetCode 3175: Find The First Player to win K Games in a Row

**LeetCode Problem #3175 — Find The First Player to win K Games in a Row**
Solve LeetCode Find The First Player to win K Games in a Row using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find The First Player to win K Games in a Row |
| LeetCode | #3175 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
A competition consists of `n` players numbered from `0` to `n - 1`.

You are given an integer array `skills` of size `n` and a **positive** integer `k`, where `skills[i]` is the skill level of player `i`. All integers in `skills` are **unique**.

All players are standing in a queue in order from player `0` to player `n - 1`.

The competition process is as follows:

The first two players in the queue play a game, and the player with the **higher** skill level wins. 
 After the game, the winner stays at the beginning of the queue, and the loser goes to the end of it.

The winner of the competition is the **first** player who wins `k` games **in a row**.

Return the initial index of the *winning* player.

## Constraints
- `n == skills.length`
- `2 <= n <= 10^5`
- `1 <= k <= 10^9`
- `1 <= skills[i] <= 10^6`
- All integers in `skills` are unique.

## Examples
### Example 1
- **Input:** `skills = [4,2,6,3,9], k = 2`
- **Output:** `2`
- **Explanation:** Initially, the queue of players is `[0,1,2,3,4]`. The following process happens: 

 
 Players 0 and 1 play a game, since the skill of player 0 is higher than that of player 1, player 0 wins. The resulting queue is `[0,2,3,4,1]`. 
 Players 0 and 2 play a game, since the skill of player 2 is higher than that of player 0, player 2 wins. The resulting queue is `[2,3,4,1,0]`. 
 Players 2 and 3 play a game, since the skill of player 2 is higher than that of player 3, player 2 wins. The resulting queue is `[2,4,1,0,3]`. 
 

 Player 2 won `k = 2` games in a row, so the winner is player 2.

### Example 2
- **Input:** `skills = [2,5,4], k = 3`
- **Output:** `1`
- **Explanation:** Initially, the queue of players is `[0,1,2]`. The following process happens: 

 
 Players 0 and 1 play a game, since the skill of player 1 is higher than that of player 0, player 1 wins. The resulting queue is `[1,2,0]`. 
 Players 1 and 2 play a game, since the skill of player 1 is higher than that of player 2, player 1 wins. The resulting queue is `[1,0,2]`. 
 Players 1 and 0 play a game, since the skill of player 1 is higher than that of player 0, player 1 wins. The resulting queue is `[1,2,0]`. 
 

 Player 1 won `k = 3` games in a row, so the winner is player 1.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Find The First Player to win K Games in a Row**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `skills = [4,2,6,3,9], k = 2`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** Initially, the queue of players is `[0,1,2,3,4]`. The following process happens: 

 
 Players 0 and 1 play a game, since the skill of player 0 is higher than that of player 1, player 0 wins. The resulting queue is `[0,2,3,4,1]`. 
 Players 0 and 2 play a game, since the skill of player 2 is higher than that of player 0, player 2 wins. The resulting queue is `[2,3,4,1,0]`. 
 Players 2 and 3 play a game, since the skill of player 2 is higher than that of player 3, player 2 wins. The resulting queue is `[2,4,1,0,3]`. 
 

 Player 2 won `k = 2` games in a row, so the winner is player 2.

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
var findWinningPlayer = function(skills, k) {
    let champion = 0;
    let streak = 0;

    for (let i = 1; i < skills.length; i++) {
        if (skills[i] > skills[champion]) {
            champion = i;
            streak = 1;
        } else {
            streak++;
        }

        if (streak === k) {
            return champion;
        }
    }

    return champion;
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
- [515. Find Largest Value in Each Tree Row](../../0501-1000/0515-find-largest-value-in-each-tree-row/)
- [3222. Find the Winning Player in Coin Game](../../3001-3500/3222-find-the-winning-player-in-coin-game/)
- [373. Find K Pairs with Smallest Sums](../../0001-0500/0373-find-k-pairs-with-smallest-sums/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-the-first-player-to-win-k-games-in-a-row/)
