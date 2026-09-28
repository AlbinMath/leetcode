class Solution {

    /**
     * @param Integer $n
     * @param Integer[] $nums
     * @param Integer $maxDiff
     * @param Integer[][] $queries
     * @return Integer[]
     */
    function pathExistenceQueries($n, $nums, $maxDiff, $queries) {

        /*
         * Sort [value, originalIndex]
         */
        $arr = [];

        for ($i = 0; $i < $n; $i++) {
            $arr[] = [$nums[$i], $i];
        }

        usort($arr, function ($a, $b) {
            return $a[0] <=> $b[0];
        });

        /*
         * sortedValues[i] = value at sorted position i
         * position[originalIndex] = sorted position
         */
        $sortedValues = array_fill(0, $n, 0);
        $position = array_fill(0, $n, 0);

        for ($i = 0; $i < $n; $i++) {
            $sortedValues[$i] = $arr[$i][0];
            $position[$arr[$i][1]] = $i;
        }

        /*
         * far[i] = farthest sorted position reachable
         * from i in ONE jump.
         */
        $far = array_fill(0, $n, 0);

        $right = 0;

        for ($i = 0; $i < $n; $i++) {

            if ($right < $i) {
                $right = $i;
            }

            while (
                $right + 1 < $n &&
                $sortedValues[$right + 1] - $sortedValues[$i] <= $maxDiff
            ) {
                $right++;
            }

            $far[$i] = $right;
        }

        /*
         * Binary lifting.
         *
         * up[k][i] =
         * position reached after 2^k greedy jumps from i.
         */
        $LOG = 1;

        while ((1 << $LOG) <= $n) {
            $LOG++;
        }

        $up = [];

        $up[0] = $far;

        for ($k = 1; $k < $LOG; $k++) {

            $prev = $up[$k - 1];
            $cur = array_fill(0, $n, 0);

            for ($i = 0; $i < $n; $i++) {
                $cur[$i] = $prev[$prev[$i]];
            }

            $up[$k] = $cur;
        }

        /*
         * Answer queries.
         */
        $answer = [];

        foreach ($queries as $query) {

            $u = $query[0];
            $v = $query[1];

            $a = $position[$u];
            $b = $position[$v];

            /*
             * We always move from smaller sorted position
             * to larger sorted position.
             */
            if ($a > $b) {
                $tmp = $a;
                $a = $b;
                $b = $tmp;
            }

            /*
             * Same node.
             */
            if ($a === $b) {
                $answer[] = 0;
                continue;
            }

            /*
             * Direct edge.
             */
            if ($far[$a] >= $b) {
                $answer[] = 1;
                continue;
            }

            /*
             * Greedily make the largest possible jumps
             * while staying strictly before b.
             */
            $current = $a;
            $steps = 0;

            for ($k = $LOG - 1; $k >= 0; $k--) {

                $next = $up[$k][$current];

                if ($next < $b) {
                    $current = $next;
                    $steps += (1 << $k);
                }
            }

            /*
             * One final jump must reach b.
             *
             * If it cannot, there is no path.
             */
            if ($far[$current] >= $b) {
                $answer[] = $steps + 1;
            } else {
                $answer[] = -1;
            }
        }

        return $answer;
    }
}
