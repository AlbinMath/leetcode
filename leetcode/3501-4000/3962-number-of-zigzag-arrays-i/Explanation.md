# LeetCode 3699: Number of ZigZag Arrays I

**LeetCode Problem #3699 — Number of ZigZag Arrays I**
Solve LeetCode Number of ZigZag Arrays I using PHP and Prefix Sum. This solution finds the optimal result using Prefix Sum Precomputation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of ZigZag Arrays I |
| LeetCode | #3699 |
| Difficulty | Hard |
| Language | PHP |
| Algorithm | Prefix Sum Precomputation |
| Data Structure | Prefix Array |
| Pattern | Prefix Sum |
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
- `3 <= n <= 2000`
- `1 <= l < r <= 2000`

## Examples
### Example 1
- **Input:** `n = 3, l = 4, r = 5`
- **Output:** `2`
- **Explanation:** There are only 2 valid ZigZag arrays of length `n = 3` using values in the range `[4, 5]`: 

 
 `[4, 5, 4]` 
 `[5, 4, 5]`​​​​​​​

### Example 2
- **Input:** `n = 3, l = 1, r = 3`
- **Output:** `10`
- **Explanation:** There are 10 valid ZigZag arrays of length `n = 3` using values in the range `[1, 3]`: 

 
 `[1, 2, 1]`, `[1, 3, 1]`, `[1, 3, 2]` 
 `[2, 1, 2]`, `[2, 1, 3]`, `[2, 3, 1]`, `[2, 3, 2]` 
 `[3, 1, 2]`, `[3, 1, 3]`, `[3, 2, 3]` 
 

 All arrays meet the ZigZag conditions.

## Key Insight
Leverage **Prefix Sum** with **Prefix Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Number of ZigZag Arrays I**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 3, l = 4, r = 5`.
2. **Processing Steps:** We apply **Prefix Sum Precomputation** using our **Prefix Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** There are only 2 valid ZigZag arrays of length `n = 3` using values in the range `[4, 5]`: 

 
 `[4, 5, 4]` 
 `[5, 4, 5]`​​​​​​​

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Prefix Array.

## Pattern
**Prefix Sum**

## Topics
- Prefix Sum
- Array

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
         * For length 1, every value can be chosen.
         *
         * We keep two arrays:
         * up[x]   = last comparison was increasing
         * down[x] = last comparison was decreasing
         *
         * For the first element, either state is effectively
         * one possible starting sequence.
         */
        $up = array_fill(0, $m, 1);
        $down = array_fill(0, $m, 1);

        /*
         * Build sequences of length 2 ... n.
         */
        for ($len = 2; $len <= $n; $len++) {

            $newUp = array_fill(0, $m, 0);
            $newDown = array_fill(0, $m, 0);

            /*
             * Prefix sums of down[].
             *
             * newUp[x] = down[0] + ... + down[x-1]
             */
            $prefix = 0;

            for ($x = 0; $x < $m; $x++) {
                $newUp[$x] = $prefix;

                $prefix += $down[$x];

                if ($prefix >= $MOD) {
                    $prefix -= $MOD;
                }
            }

            /*
             * Suffix sums of up[].
             *
             * newDown[x] = up[x+1] + ... + up[m-1]
             */
            $suffix = 0;

            for ($x = $m - 1; $x >= 0; $x--) {
                $newDown[$x] = $suffix;

                $suffix += $up[$x];

                if ($suffix >= $MOD) {
                    $suffix -= $MOD;
                }
            }

            $up = $newUp;
            $down = $newDown;
        }

        /*
         * Every valid sequence ends either with an increasing
         * or decreasing step.
         */
        $answer = 0;

        for ($x = 0; $x < $m; $x++) {
            $answer += $up[$x];

            if ($answer >= $MOD) {
                $answer -= $MOD;
            }

            $answer += $down[$x];

            if ($answer >= $MOD) {
                $answer -= $MOD;
            }
        }

        return $answer;
    }
}
```

## Why This Works
By utilizing **Prefix Sum**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [3700. Number of ZigZag Arrays II](../../3501-4000/3964-number-of-zigzag-arrays-ii/)
- [996. Number of Squareful Arrays](../../1001-1500/1038-number-of-squareful-arrays/)
- [1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold](../../1001-1500/1445-number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-zigzag-arrays-i/)
