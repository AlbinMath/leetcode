# LeetCode 1301: Number of Paths with Max Score

**LeetCode Problem #1301 — Number of Paths with Max Score**
Solve LeetCode Number of Paths with Max Score using PHP and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Paths with Max Score |
| LeetCode | #1301 |
| Difficulty | Hard |
| Language | PHP |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a square `board` of characters. You can move on the board starting at the bottom right square marked with the character `'S'`.

You need to reach the top left square marked with the character `'E'`. The rest of the squares are labeled either with a numeric character `1, 2, ..., 9` or with an obstacle `'X'`. In one move you can go up, left or up-left (diagonally) only if there is no obstacle there.

Return a list of two integers: the first integer is the maximum sum of numeric characters you can collect, and the second is the number of such paths that you can take to get that maximum sum, **taken modulo `10^9 + 7`**.

In case there is no path, return `[0, 0]`.

## Constraints
- `2 <= board.length == board[i].length <= 100`

## Examples
### Example 1
- **Input:** `board = ["E23","2X2","12S"]`
- **Output:** `[7,1]`

### Example 2
- **Input:** `board = ["E12","1X1","21S"]`
- **Output:** `[4,2]`

### Example 3
- **Input:** `board = ["E11","XXX","11S"]`
- **Output:** `[0,0]`

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
The code uses **2D Dynamic Programming** processing from `S` toward `E`.

1. **Two DP Tables:** `score[i][j]` stores the maximum score reachable from `(i,j)` to `S`. `ways[i][j]` stores the number of paths achieving that score. `-1` means unreachable.
2. **Base Case:** `score[n-1][n-1] = 0`, `ways[n-1][n-1] = 1` (at `S`).
3. **Transition:** For each cell `(i,j)` processed right-to-left, bottom-to-top:
   - Skip obstacles (`X`).
   - Check three neighbors: down `(i+1,j)`, right `(i,j+1)`, diagonal `(i+1,j+1)`.
   - Take the neighbor with the highest score. If multiple neighbors tie, sum their path counts.
   - Add the current cell's digit value to the best score.
4. **Result:** `[score[0][0], ways[0][0]]`, or `[0, 0]` if unreachable.

Time complexity is $O(N^2)$ and space complexity is $O(N^2)$.

## Algorithm
1. Initialize state variables / data structure (**DP Table / Array**).
2. Process elements sequentially using **Memoization & State Transition**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `board = ["E23","2X2","12S"]`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[7,1]`.

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
     * @param String[] $board
     * @return Integer[]
     */
    function pathsWithMaxScore($board) {
        $MOD = 1000000007;
        $n = count($board);

        // -1 means unreachable
        $score = array_fill(0, $n, array_fill(0, $n, -1));
        $ways  = array_fill(0, $n, array_fill(0, $n, 0));

        // Start at S
        $score[$n - 1][$n - 1] = 0;
        $ways[$n - 1][$n - 1] = 1;

        /*
         * Process from S -> E.
         *
         * From (i,j), the possible next cells toward E are:
         *   down       (i+1, j)
         *   right      (i, j+1)
         *   diagonal   (i+1, j+1)
         */
        for ($i = $n - 1; $i >= 0; $i--) {
            for ($j = $n - 1; $j >= 0; $j--) {

                // S is already initialized
                if ($i == $n - 1 && $j == $n - 1) {
                    continue;
                }

                // Obstacle
                if ($board[$i][$j] === 'X') {
                    continue;
                }

                $best = -1;
                $count = 0;

                // Down
                if ($i + 1 < $n && $score[$i + 1][$j] != -1) {
                    $best = $score[$i + 1][$j];
                    $count = $ways[$i + 1][$j];
                }

                // Right
                if ($j + 1 < $n && $score[$i][$j + 1] != -1) {
                    $v = $score[$i][$j + 1];

                    if ($v > $best) {
                        $best = $v;
                        $count = $ways[$i][$j + 1];
                    } elseif ($v == $best) {
                        $count += $ways[$i][$j + 1];

                        if ($count >= $MOD) {
                            $count -= $MOD;
                        }
                    }
                }

                // Diagonal
                if (
                    $i + 1 < $n &&
                    $j + 1 < $n &&
                    $score[$i + 1][$j + 1] != -1
                ) {
                    $v = $score[$i + 1][$j + 1];

                    if ($v > $best) {
                        $best = $v;
                        $count = $ways[$i + 1][$j + 1];
                    } elseif ($v == $best) {
                        $count += $ways[$i + 1][$j + 1];

                        if ($count >= $MOD) {
                            $count -= $MOD;
                        }
                    }
                }

                // No path to S
                if ($best == -1) {
                    continue;
                }

                // Add current cell's digit
                $value = 0;

                if (
                    $board[$i][$j] !== 'E' &&
                    $board[$i][$j] !== 'S'
                ) {
                    $value = ord($board[$i][$j]) - 48;
                }

                $score[$i][$j] = $best + $value;
                $ways[$i][$j] = $count;
            }
        }

        /*
         * IMPORTANT:
         * Check score, not ways.
         *
         * ways can be 0 because the count is modulo 1e9+7.
         */
        if ($score[0][0] == -1) {
            return [0, 0];
        }

        return [
            $score[0][0],
            $ways[0][0]
        ];
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
- [1579. Remove Max Number of Edges to Keep Graph Fully Traversable](../../1501-2000/1701-remove-max-number-of-edges-to-keep-graph-fully-traversable/)
- [1593. Split a String Into the Max Number of Unique Substrings](../../1501-2000/1715-split-a-string-into-the-max-number-of-unique-substrings/)
- [1679. Max Number of K-Sum Pairs](../../1501-2000/1798-max-number-of-k-sum-pairs/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-paths-with-max-score/)
