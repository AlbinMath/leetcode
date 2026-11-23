# LeetCode 3222: Find the Winning Player in Coin Game

**LeetCode Problem #3222 — Find the Winning Player in Coin Game**
Solve LeetCode Find the Winning Player in Coin Game using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find the Winning Player in Coin Game |
| LeetCode | #3222 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two **positive** integers `x` and `y`, denoting the number of coins with values 75 and 10 *respectively*.

Alice and Bob are playing a game. Each turn, starting with **Alice**, the player must pick up coins with a **total** value 115. If the player is unable to do so, they **lose** the game.

Return the *name* of the player who wins the game if both players play **optimally**.

## Constraints
- `1 <= x, y <= 100`

## Examples
### Example 1
- **Input:** `x = 2, y = 7`
- **Output:** `"Alice"`
- **Explanation:** The game ends in a single turn: 

 
 Alice picks 1 coin with a value of 75 and 4 coins with a value of 10.

### Example 2
- **Input:** `x = 4, y = 11`
- **Output:** `"Bob"`
- **Explanation:** The game ends in 2 turns: 

 
 Alice picks 1 coin with a value of 75 and 4 coins with a value of 10. 
 Bob picks 1 coin with a value of 75 and 4 coins with a value of 10.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Find the Winning Player in Coin Game**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `x = 2, y = 7`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"Alice"`.
4. **Verification:** The game ends in a single turn: 

 
 Alice picks 1 coin with a value of 75 and 4 coins with a value of 10.

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
class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        return "Alice" if min(x, y // 4) % 2 else "Bob"
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
- [1275. Find Winner on a Tic Tac Toe Game](../../1001-1500/1400-find-winner-on-a-tic-tac-toe-game/)
- [1535. Find the Winner of an Array Game](../../1501-2000/1657-find-the-winner-of-an-array-game/)
- [1823. Find the Winner of the Circular Game](../../1501-2000/1951-find-the-winner-of-the-circular-game/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-the-winning-player-in-coin-game/)
