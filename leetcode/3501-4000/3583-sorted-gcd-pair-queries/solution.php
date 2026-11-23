class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer[] $queries
     * @return Integer[]
     */
    function gcdValues($nums, $queries) {

        $n = count($nums);
        $maxVal = max($nums);

        // Frequency of each value
        $freq = array_fill(0, $maxVal + 1, 0);

        foreach ($nums as $x) {
            $freq[$x]++;
        }

        /*
         * exact[g] = number of pairs whose GCD is exactly g.
         *
         * We calculate from large gcd to small gcd.
         */
        $exact = array_fill(0, $maxVal + 1, 0);

        for ($g = $maxVal; $g >= 1; $g--) {

            // Number of elements divisible by g
            $count = 0;

            for ($x = $g; $x <= $maxVal; $x += $g) {
                $count += $freq[$x];
            }

            // Number of pairs whose GCD is a multiple of g
            $pairs = intdiv($count * ($count - 1), 2);

            /*
             * Remove pairs whose exact GCD is 2g, 3g, ...
             */
            for ($multiple = $g + $g; $multiple <= $maxVal; $multiple += $g) {
                $pairs -= $exact[$multiple];
            }

            $exact[$g] = $pairs;
        }

        /*
         * Prefix sums:
         *
         * prefix[g] = number of pairs with GCD <= g
         */
        $prefix = 0;

        for ($g = 1; $g <= $maxVal; $g++) {
            $prefix += $exact[$g];
            $exact[$g] = $prefix;
        }

        /*
         * For each query q, find the smallest g such that
         *
         * prefix[g] > q
         *
         * because queries use 0-based indexing.
         */
        $answer = [];

        foreach ($queries as $q) {

            $lo = 1;
            $hi = $maxVal;

            while ($lo < $hi) {
                $mid = intdiv($lo + $hi, 2);

                if ($exact[$mid] > $q) {
                    $hi = $mid;
                } else {
                    $lo = $mid + 1;
                }
            }

            $answer[] = $lo;
        }

        return $answer;
    }
}
