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
