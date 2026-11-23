# LeetCode 1406: Stone Game III

**LeetCode Problem #1406 — Stone Game III**
Solve LeetCode Stone Game III using PHP and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Stone Game III |
| LeetCode | #1406 |
| Difficulty | Hard |
| Language | PHP |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Alice and Bob continue their games with piles of stones. There are several stones **arranged in a row**, and each stone has an associated value which is an integer given in the array `stoneValue`.

Alice and Bob take turns, with Alice starting first. On each player's turn, that player can take `1`, `2`, or `3` stones from the **first** remaining stones in the row.

The score of each player is the sum of the values of the stones taken. The score of each player is `0` initially.

The objective of the game is to end with the highest score, and the winner is the player with the highest score and there could be a tie. The game continues until all the stones have been taken.

Assume Alice and Bob **play optimally**.

Return `"Alice"`* if Alice will win, *`"Bob"`* if Bob will win, or *`"Tie"`* if they will end the game with the same score*.

## Constraints
- `1 <= stoneValue.length <= 5 * 10^4`
- `-1000 <= stoneValue[i] <= 1000`

## Examples
### Example 1
- **Input:** `stoneValue = [1,2,3,7]`
- **Output:** `"Bob"`
- **Explanation:** Alice will always lose. Her best move will be to take three piles and the score become 6. Now the score of Bob is 7 and Bob wins.

### Example 2
- **Input:** `stoneValue = [1,2,3,-9]`
- **Output:** `"Alice"`
- **Explanation:** Alice must choose all the three piles at the first move to win and leave Bob with negative score.
If Alice chooses one pile her score will be 1 and the next move Bob's score becomes 5. In the next move, Alice will take the pile with value = -9 and lose.
If Alice chooses two piles her score will be 3 and the next move Bob's score becomes 3. In the next move, Alice will take the pile with value = -9 and also lose.
Remember that both play optimally so here Alice will choose the scenario that makes her win.

### Example 3
- **Input:** `stoneValue = [1,2,3,6]`
- **Output:** `"Tie"`
- **Explanation:** Alice cannot win this game. She can end the game in a draw if she decided to choose all the first three piles, otherwise she will lose.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
The code uses **Dynamic Programming** where `dp[i]` = max stones the current player can score from piles `i` onward.

1. Process from the last pile backwards.
2. For each position `i`, try taking 1, 2, or 3 piles. The current player gets `suffix[i] - dp[i + take]` (total remaining minus what the opponent gets).
3. Compare `dp[0]` (Alice's score) with `suffix[0] - dp[0]` (Bob's score).

Time complexity is $O(N)$ and space complexity is $O(N)$.

## Algorithm
1. Initialize state variables / data structure (**DP Table / Array**).
2. Process elements sequentially using **Memoization & State Transition**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `stoneValue = [1,2,3,7]`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"Bob"`.
4. **Verification:** Alice will always lose. Her best move will be to take three piles and the score become 6. Now the score of Bob is 7 and Bob wins.

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
PHP

## Source Code
- [solution.php](./solution.php)


```php
class Solution {

    /**
     * @param Integer[] $stoneValue
     * @return String
     */
    function stoneGameIII($stoneValue) {
        $n = count($stoneValue);

        // dp[i] = maximum score difference
        // current player can achieve starting from i
        $dp = array_fill(0, $n + 1, 0);

        // Base case: no stones left
        $dp[$n] = 0;

        for ($i = $n - 1; $i >= 0; $i--) {

            $take = 0;
            $best = PHP_INT_MIN;

            // Take 1, 2, or 3 stones
            for ($j = 0; $j < 3 && $i + $j < $n; $j++) {

                $take += $stoneValue[$i + $j];

                // Current player's gain minus opponent's best result
                $best = max(
                    $best,
                    $take - $dp[$i + $j + 1]
                );
            }

            $dp[$i] = $best;
        }

        if ($dp[0] > 0) {
            return "Alice";
        } elseif ($dp[0] < 0) {
            return "Bob";
        } else {
            return "Tie";
        }
    }
}
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
- [877. Stone Game](../../0501-1000/0909-stone-game/)
- [1140. Stone Game II](../../1001-1500/1240-stone-game-ii/)
- [1510. Stone Game IV](../../1501-2000/1617-stone-game-iv/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/stone-game-iii/)
