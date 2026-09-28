class Solution {

    /**
     * @param String $s
     * @param Integer[][] $queries
     * @return Integer[]
     */
    function maxActiveSectionsAfterTrade($s, $queries) {
        $n = strlen($s);
        $ones = substr_count($s, '1');

        // [start, length] for every zero group
        $zeroGroups = [];

        // For every position, store the index of the latest zero group.
        $zeroGroupIndex = array_fill(0, $n, -1);

        for ($i = 0; $i < $n; $i++) {

            if ($s[$i] === '0') {
                if ($i > 0 && $s[$i - 1] === '0') {
                    $idx = count($zeroGroups) - 1;
                    $zeroGroups[$idx][1]++;
                } else {
                    $zeroGroups[] = [$i, 1];
                }
            }

            // IMPORTANT:
            // Even if s[i] == '1', keep the latest zero-group index.
            $zeroGroupIndex[$i] = count($zeroGroups) - 1;
        }

        $g = count($zeroGroups);

        // Need at least two zero groups to perform a trade.
        if ($g < 2) {
            return array_fill(0, count($queries), $ones);
        }

        /*
         * merge[i] = size of zero group i + zero group i+1
         *
         * Choosing the 1-block between these two zero groups
         * allows the two zero groups to be merged and then
         * converted into 1s.
         */
        $merge = [];

        for ($i = 0; $i < $g - 1; $i++) {
            $merge[$i] =
                $zeroGroups[$i][1] +
                $zeroGroups[$i + 1][1];
        }

        /*
         * Sparse table for range maximum query.
         */
        $m = count($merge);

        $log = array_fill(0, $m + 1, 0);

        for ($i = 2; $i <= $m; $i++) {
            $log[$i] = $log[intdiv($i, 2)] + 1;
        }

        $K = $log[$m] + 1;

        $st = array_fill(0, $K, []);
        $st[0] = $merge;

        for ($k = 1; $k < $K; $k++) {
            $len = 1 << $k;
            $half = $len >> 1;
            $limit = $m - $len + 1;

            $row = [];

            for ($i = 0; $i < $limit; $i++) {
                $row[$i] = max(
                    $st[$k - 1][$i],
                    $st[$k - 1][$i + $half]
                );
            }

            $st[$k] = $row;
        }

        // Range maximum query on merge[]
        $rangeMax = function ($l, $r) use (&$st, &$log) {
            if ($l > $r) {
                return 0;
            }

            $len = $r - $l + 1;
            $k = $log[$len];
            $block = 1 << $k;

            return max(
                $st[$k][$l],
                $st[$k][$r - $block + 1]
            );
        };

        $answer = [];

        foreach ($queries as $query) {

            $l = $query[0];
            $r = $query[1];

            // No trade
            $best = $ones;

            $leftGroup = $zeroGroupIndex[$l];
            $rightGroup = $zeroGroupIndex[$r];

            /*
             * Portion of the left zero group inside [l, r].
             */
            $left = -1;

            if ($leftGroup !== -1) {
                $start = $zeroGroups[$leftGroup][0];
                $length = $zeroGroups[$leftGroup][1];

                $left = $length - ($l - $start);
            }

            /*
             * Portion of the right zero group inside [l, r].
             */
            $right = -1;

            if ($rightGroup !== -1) {
                $start = $zeroGroups[$rightGroup][0];

                $right = $r - $start + 1;
            }

            /*
             * Determine zero-group pairs completely usable
             * inside the query.
             */
            $startGroup = $leftGroup + 1;

            $endGroup = ($s[$r] === '1')
                ? $rightGroup
                : $rightGroup - 1;

            /*
             * Case 1:
             * Query begins and ends inside zero groups,
             * and those are adjacent zero groups.
             */
            if (
                $s[$l] === '0' &&
                $s[$r] === '0' &&
                $leftGroup + 1 === $rightGroup
            ) {
                $best = max(
                    $best,
                    $ones + $left + $right
                );
            }

            /*
             * Case 2:
             * Choose any completely contained pair of zero groups.
             */
            else {
                $mergeL = $startGroup;
                $mergeR = $endGroup - 1;

                if ($mergeL <= $mergeR) {
                    $best = max(
                        $best,
                        $ones + $rangeMax($mergeL, $mergeR)
                    );
                }
            }

            /*
             * Case 3:
             * Use the left partial zero group together
             * with the next complete zero group.
             */
            if (
                $s[$l] === '0' &&
                $leftGroup + 1 <=
                (($s[$r] === '1')
                    ? $rightGroup
                    : $rightGroup - 1)
            ) {
                $best = max(
                    $best,
                    $ones +
                    $left +
                    $zeroGroups[$leftGroup + 1][1]
                );
            }

            /*
             * Case 4:
             * Use the right partial zero group together
             * with the previous complete zero group.
             */
            if (
                $s[$r] === '0' &&
                $leftGroup < $rightGroup - 1
            ) {
                $best = max(
                    $best,
                    $ones +
                    $right +
                    $zeroGroups[$rightGroup - 1][1]
                );
            }

            $answer[] = $best;
        }

        return $answer;
    }
}
