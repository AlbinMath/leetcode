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
