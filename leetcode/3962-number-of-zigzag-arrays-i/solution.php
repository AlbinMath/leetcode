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
