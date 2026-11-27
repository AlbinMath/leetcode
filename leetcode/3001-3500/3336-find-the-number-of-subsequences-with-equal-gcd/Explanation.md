# LeetCode 3336: Find the Number of Subsequences With Equal GCD

**LeetCode Problem #3336 — Find the Number of Subsequences With Equal GCD**
Solve LeetCode Find the Number of Subsequences With Equal GCD using PHP and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find the Number of Subsequences With Equal GCD |
| LeetCode | #3336 |
| Difficulty | Hard |
| Language | PHP |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `nums`.

Your task is to find the number of pairs of **non-empty** subsequences `(seq1, seq2)` of `nums` that satisfy the following conditions:

The subsequences `seq1` and `seq2` are **disjoint**, meaning **no index** of `nums` is common between them. 
 The GCD of the elements of `seq1` is equal to the GCD of the elements of `seq2`.

Return the total number of such pairs.

Since the answer may be very large, return it **modulo** `10^9 + 7`.

## Constraints
- `1 <= nums.length <= 200`
- `1 <= nums[i] <= 200`

## Examples
### Example 1
- **Input:** `nums = [1,2,3,4]`
- **Output:** `10`
- **Explanation:** The subsequence pairs which have the GCD of their elements equal to 1 are: 

 
 ([

### Example 2
- **Input:** `nums = [10,20,30]`
- **Output:** `2`
- **Explanation:** The subsequence pairs which have the GCD of their elements equal to 10 are: 

 
 ([

### Example 3
- **Input:** `nums = [1,1,1,1]`
- **Output:** `50`

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Find the Number of Subsequences With Equal GCD**, we observe the problem requirements and utilize the **Dynamic Programming** technique. We decompose the problem into overlapping subproblems using a **DP Table / Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,3,4]`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `10`.
4. **Verification:** The subsequence pairs which have the GCD of their elements equal to 1 are: 

 
 ([

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
     * @param Integer[] $nums
     * @return Integer
     */
    function subsequencePairCount($nums) {
        $MOD = 1000000007;
        $MAX = 200;
        $SIZE = 201;

        /*
         * gcdTable[x * SIZE + g] = gcd(x, g)
         */
        $gcdTable = array_fill(0, $SIZE * $SIZE, 0);

        for ($x = 1; $x <= $MAX; $x++) {
            for ($g = 0; $g <= $MAX; $g++) {
                $a = $x;
                $b = $g;

                while ($b != 0) {
                    $t = $a % $b;
                    $a = $b;
                    $b = $t;
                }

                $gcdTable[$x * $SIZE + $g] = $a;
            }
        }

        /*
         * dp[g1][g2] stored as:
         *
         * dp[g1 * SIZE + g2]
         *
         * 0 means the corresponding subsequence is empty.
         */
        $dp = array_fill(0, $SIZE * $SIZE, 0);
        $dp[0] = 1;

        /*
         * List of currently reachable states.
         * This avoids scanning all 40,401 states unnecessarily.
         */
        $states = [0];

        foreach ($nums as $x) {

            $next = array_fill(0, $SIZE * $SIZE, 0);
            $nextStates = [];

            $gxBase = $x * $SIZE;

            foreach ($states as $idx) {

                $ways = $dp[$idx];

                if ($ways == 0) {
                    continue;
                }

                $g1 = intdiv($idx, $SIZE);
                $g2 = $idx - $g1 * $SIZE;

                /*
                 * Option 1: Don't use x.
                 */
                if ($next[$idx] == 0) {
                    $nextStates[] = $idx;
                }

                $value = $next[$idx] + $ways;

                if ($value >= $MOD) {
                    $value -= $MOD;
                }

                $next[$idx] = $value;

                /*
                 * Option 2: Put x into subsequence 1.
                 */
                $newG1 = $gcdTable[$gxBase + $g1];
                $idx1 = $newG1 * $SIZE + $g2;

                if ($next[$idx1] == 0) {
                    $nextStates[] = $idx1;
                }

                $value = $next[$idx1] + $ways;

                if ($value >= $MOD) {
                    $value -= $MOD;
                }

                $next[$idx1] = $value;

                /*
                 * Option 3: Put x into subsequence 2.
                 */
                $newG2 = $gcdTable[$gxBase + $g2];
                $idx2 = $g1 * $SIZE + $newG2;

                if ($next[$idx2] == 0) {
                    $nextStates[] = $idx2;
                }

                $value = $next[$idx2] + $ways;

                if ($value >= $MOD) {
                    $value -= $MOD;
                }

                $next[$idx2] = $value;
            }

            $dp = $next;
            $states = $nextStates;
        }

        /*
         * Both subsequences must be non-empty and
         * must have the same GCD.
         */
        $answer = 0;

        for ($g = 1; $g <= $MAX; $g++) {
            $answer += $dp[$g * $SIZE + $g];

            if ($answer >= $MOD) {
                $answer -= $MOD;
            }
        }

        return $answer;
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
- [2447. Number of Subarrays With GCD Equal to K](../../2001-2500/2447-number-of-subarrays-with-gcd-equal-to-k/)
- [287. Find the Duplicate Number](../../0001-0500/0287-find-the-duplicate-number/)
- [1295. Find Numbers with Even Number of Digits](../../1001-1500/1295-find-numbers-with-even-number-of-digits/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-the-number-of-subsequences-with-equal-gcd/)
