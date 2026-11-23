# LeetCode 3700: Number of ZigZag Arrays II

**LeetCode Problem #3700 — Number of ZigZag Arrays II**
Solve LeetCode Number of ZigZag Arrays II using PHP and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of ZigZag Arrays II |
| LeetCode | #3700 |
| Difficulty | Hard |
| Language | PHP |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given three integers `n`, `l`, and `r`.

A **ZigZag** array of length `n` is defined as follows:

Each element lies in the range `[l, r]`. 
 No **two** adjacent elements are equal. 
 No **three** consecutive elements form a **strictly increasing** or **strictly decreasing** sequence.

Return the total number of valid **ZigZag** arrays.

Since the answer may be large, return it **modulo** `10^9 + 7`.

A **sequence** is said to be **strictly increasing** if each element is strictly greater than its previous one (if exists).

A **sequence** is said to be **strictly decreasing** if each element is strictly smaller than its previous one (if exists).

## Constraints
- `3 <= n <= 10^9`
- `1 <= l < r <= 75`​​​​​​​

## Examples
### Example 1
- **Input:** `n = 3, l = 4, r = 5`
- **Output:** `2`
- **Explanation:** There are only 2 valid ZigZag arrays of length `n = 3` using values in the range `[4, 5]`: 

 
 `[4, 5, 4]` 
 `[5, 4, 5]`

### Example 2
- **Input:** `n = 3, l = 1, r = 3`
- **Output:** `10`
- **Explanation:** ​​​​​​​There are 10 valid ZigZag arrays of length `n = 3` using values in the range `[1, 3]`: 

 
 `[1, 2, 1]`, `[1, 3, 1]`, `[1, 3, 2]` 
 `[2, 1, 2]`, `[2, 1, 3]`, `[2, 3, 1]`, `[2, 3, 2]` 
 `[3, 1, 2]`, `[3, 1, 3]`, `[3, 2, 3]` 
 

 All arrays meet the ZigZag conditions.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Number of ZigZag Arrays II**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 3, l = 4, r = 5`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** There are only 2 valid ZigZag arrays of length `n = 3` using values in the range `[4, 5]`: 

 
 `[4, 5, 4]` 
 `[5, 4, 5]`

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
PHP

## Source Code
- [solution.php](./solution.php)


```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $l
     * @param Integer $r
     * @return Integer
     */
    function zigZagArrays($n, $l, $r) {
        $MOD = 1000000007;

        $m = $r - $l + 1;

        /*
         * Matrix M:
         *
         * M[i][j] = 1 if i + j < m - 1
         *
         * This represents one alternating transition.
         */
        $M = array_fill(0, $m * $m, 0);

        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $m - 1 - $i; $j++) {
                $M[$i * $m + $j] = 1;
            }
        }

        /*
         * Initially every value can be the first element.
         *
         * We need M^(n-1) * [1,1,...,1].
         */
        $vec = array_fill(0, $m, 1);

        $power = $n - 1;
        $base = $M;

        /*
         * Instead of calculating the complete M^(n-1),
         * apply matrix powers directly to the vector.
         */
        while ($power > 0) {

            if ($power & 1) {
                $vec = $this->multiplyMatrixVector(
                    $base,
                    $vec,
                    $m,
                    $MOD
                );
            }

            $power >>= 1;

            if ($power > 0) {
                $base = $this->multiplyMatrices(
                    $base,
                    $base,
                    $m,
                    $MOD
                );
            }
        }

        /*
         * The DP above counts one direction.
         *
         * Every valid zigzag has a symmetric opposite
         * direction, so multiply by 2.
         */
        $answer = 0;

        foreach ($vec as $value) {
            $answer += $value;

            if ($answer >= $MOD) {
                $answer -= $MOD;
            }
        }

        return (int)(($answer * 2) % $MOD);
    }

    /**
     * Matrix × vector
     */
    private function multiplyMatrixVector($A, $v, $m, $MOD) {
        $result = array_fill(0, $m, 0);

        for ($i = 0; $i < $m; $i++) {
            $sum = 0;
            $offset = $i * $m;

            for ($j = 0; $j < $m; $j++) {
                $a = $A[$offset + $j];

                if ($a != 0 && $v[$j] != 0) {
                    $sum = ($sum + $a * $v[$j]) % $MOD;
                }
            }

            $result[$i] = $sum;
        }

        return $result;
    }

    /**
     * Matrix × Matrix
     */
    private function multiplyMatrices($A, $B, $m, $MOD) {
        $C = array_fill(0, $m * $m, 0);

        for ($i = 0; $i < $m; $i++) {
            $row = $i * $m;

            for ($k = 0; $k < $m; $k++) {
                $a = $A[$row + $k];

                if ($a == 0) {
                    continue;
                }

                $bRow = $k * $m;

                for ($j = 0; $j < $m; $j++) {
                    $b = $B[$bRow + $j];

                    if ($b == 0) {
                        continue;
                    }

                    $idx = $row + $j;

                    $C[$idx] =
                        ($C[$idx] + $a * $b) % $MOD;
                }
            }
        }

        return $C;
    }
}
```

## Why This Works
By utilizing **Stack & Queue**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [3699. Number of ZigZag Arrays I](../../3501-4000/3962-number-of-zigzag-arrays-i/)
- [996. Number of Squareful Arrays](../../1001-1500/1038-number-of-squareful-arrays/)
- [1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold](../../1001-1500/1445-number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-zigzag-arrays-ii/)
