# LeetCode 3518: Smallest Palindromic Rearrangement II

**LeetCode Problem #3518 — Smallest Palindromic Rearrangement II**
Solve LeetCode Smallest Palindromic Rearrangement II using PHP and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Smallest Palindromic Rearrangement II |
| LeetCode | #3518 |
| Difficulty | Hard |
| Language | PHP |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a ** palindromic ** string `s` and an integer `k`.

Return the **k-th** ** lexicographically smallest ** palindromic permutation of `s`. If there are fewer than `k` distinct palindromic permutations, return an empty string.

**Note:** Different rearrangements that yield the same palindromic string are considered identical and are counted once.

## Constraints
- `1 <= s.length <= 10^4`
- `s` consists of lowercase English letters.
- `s` is guaranteed to be palindromic.
- `1 <= k <= 10^6`

## Examples
### Example 1
- **Input:** `s = "abba", k = 2`
- **Output:** `"baab"`
- **Explanation:** The two distinct palindromic rearrangements of `"abba"` are `"abba"` and `"baab"`. 
 Lexicographically, `"abba"` comes before `"baab"`. Since `k = 2`, the output is `"baab"`.

### Example 2
- **Input:** `s = "aa", k = 2`
- **Output:** `""`
- **Explanation:** There is only one palindromic rearrangement: "aa" . 
 The output is an empty string since `k = 2` exceeds the number of possible rearrangements.

### Example 3
- **Input:** `s = "bacab", k = 1`
- **Output:** `"abcba"`
- **Explanation:** The two distinct palindromic rearrangements of `"bacab"` are `"abcba"` and `"bacab"`. 
 Lexicographically, `"abcba"` comes before `"bacab"`. Since `k = 1`, the output is `"abcba"`.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Smallest Palindromic Rearrangement II**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "abba", k = 2`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"baab"`.
4. **Verification:** The two distinct palindromic rearrangements of `"abba"` are `"abba"` and `"baab"`. 
 Lexicographically, `"abba"` comes before `"baab"`. Since `k = 2`, the output is `"baab"`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

## Language
PHP

## Source Code
- [solution.php](./solution.php)


```php
class Solution {

    /**
     * @param String $s
     * @param Integer $k
     * @return String
     */
    function smallestPalindrome($s, $k) {

        $n = strlen($s);

        // Count characters
        $freq = array_fill(0, 26, 0);

        for ($i = 0; $i < $n; $i++) {
            $freq[ord($s[$i]) - 97]++;
        }

        // We only need to arrange the left half.
        $half = array_fill(0, 26, 0);
        $halfLen = intdiv($n, 2);

        for ($i = 0; $i < 26; $i++) {
            $half[$i] = intdiv($freq[$i], 2);
        }

        /*
         * Returns the number of distinct permutations of $cnt,
         * capped at $limit.
         *
         * Example:
         * [2,1] -> 3
         * [3,2,1] -> 60
         */
        $countWays = function ($cnt, $limit) {

            $ways = 1;
            $total = 0;

            for ($c = 0; $c < 26; $c++) {

                $r = $cnt[$c];

                if ($r == 0) {
                    continue;
                }

                /*
                 * Add this character group.
                 *
                 * New ways:
                 *
                 * oldWays * C(total + r, r)
                 */
                $newTotal = $total + $r;

                $comb = 1;

                for ($i = 1; $i <= $r; $i++) {

                    $numerator = $newTotal - $r + $i;

                    /*
                     * Check whether:
                     *
                     * comb * numerator / i >= limit
                     *
                     * before multiplying.
                     */
                    if (
                        $comb >
                        intdiv($limit * $i, $numerator)
                    ) {
                        $comb = $limit;
                        break;
                    }

                    $comb = intdiv(
                        $comb * $numerator,
                        $i
                    );

                    if ($comb >= $limit) {
                        $comb = $limit;
                        break;
                    }
                }

                /*
                 * ways * comb >= limit
                 */
                if (
                    $ways >
                    intdiv($limit, max(1, $comb))
                ) {
                    return $limit;
                }

                $ways *= $comb;

                if ($ways >= $limit) {
                    return $limit;
                }

                $total = $newTotal;
            }

            return $ways;
        };

        /*
         * IMPORTANT:
         * Check whether k-th permutation exists at all.
         *
         * For s = "a":
         * half = []
         * total ways = 1
         * k = 2
         * => return ""
         */
        if ($countWays($half, $k) < $k) {
            return "";
        }

        /*
         * Construct the k-th lexicographically smallest
         * permutation of the left half.
         */
        $left = '';

        for ($pos = 0; $pos < $halfLen; $pos++) {

            for ($c = 0; $c < 26; $c++) {

                if ($half[$c] == 0) {
                    continue;
                }

                // Try placing this character.
                $half[$c]--;

                // Number of permutations after choosing it.
                $ways = $countWays($half, $k);

                if ($ways >= $k) {

                    // k-th answer is inside this block.
                    $left .= chr(97 + $c);

                    break;

                } else {

                    // Skip this entire block.
                    $k -= $ways;

                    // Restore the character.
                    $half[$c]++;
                }
            }
        }

        /*
         * Middle character for odd length.
         */
        $middle = '';

        if ($n % 2 == 1) {

            for ($i = 0; $i < 26; $i++) {

                if ($freq[$i] % 2 == 1) {
                    $middle = chr(97 + $i);
                    break;
                }
            }
        }

        /*
         * Mirror the left half.
         */
        return $left . $middle . strrev($left);
    }
}
```

## Why This Works
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [3517. Smallest Palindromic Rearrangement I](../../3501-4000/3517-smallest-palindromic-rearrangement-i/)
- [3734. Lexicographically Smallest Palindromic Permutation Greater Than Target](../../3501-4000/3734-lexicographically-smallest-palindromic-permutation-greater-than-target/)
- [230. Kth Smallest Element in a BST](../../0001-0500/0230-kth-smallest-element-in-a-bst/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/smallest-palindromic-rearrangement-ii/)
