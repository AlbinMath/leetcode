class Solution {

    /**
     * @param Integer[][] $edges
     * @param Boolean[] $online
     * @param Integer $k
     * @return Integer
     */
    function findMaxPathScore($edges, $online, $k) {
        $n = count($online);

        /*
         * Build graph using only online nodes.
         * An offline intermediate node can never be part
         * of a valid path.
         */
        $graph = array_fill(0, $n, []);
        $indegree = array_fill(0, $n, 0);

        $maxCost = 0;

        foreach ($edges as $edge) {
            $u = $edge[0];
            $v = $edge[1];
            $cost = $edge[2];

            if (!$online[$u] || !$online[$v]) {
                continue;
            }

            $graph[$u][] = [$v, $cost];
            $indegree[$v]++;

            if ($cost > $maxCost) {
                $maxCost = $cost;
            }
        }

        /*
         * Topological sort (Kahn's algorithm).
         */
        $queue = [];
        $head = 0;

        for ($i = 0; $i < $n; $i++) {
            if ($indegree[$i] == 0) {
                $queue[] = $i;
            }
        }

        $topo = [];

        while ($head < count($queue)) {
            $u = $queue[$head++];
            $topo[] = $u;

            foreach ($graph[$u] as $edge) {
                $v = $edge[0];

                $indegree[$v]--;

                if ($indegree[$v] == 0) {
                    $queue[] = $v;
                }
            }
        }

        /*
         * Check whether a path exists whose:
         *
         * 1. Every edge cost >= $threshold
         * 2. Total cost <= k
         */
        $check = function ($threshold) use (
            &$graph,
            &$topo,
            $n,
            $k
        ) {
            $INF = PHP_INT_MAX;

            $dist = array_fill(0, $n, $INF);
            $dist[0] = 0;

            foreach ($topo as $u) {

                if ($dist[$u] === $INF) {
                    continue;
                }

                /*
                 * No need to continue paths already over budget.
                 */
                if ($dist[$u] > $k) {
                    continue;
                }

                foreach ($graph[$u] as $edge) {
                    $v = $edge[0];
                    $cost = $edge[1];

                    /*
                     * This edge would make the path score
                     * smaller than the threshold.
                     */
                    if ($cost < $threshold) {
                        continue;
                    }

                    $newCost = $dist[$u] + $cost;

                    /*
                     * We only care about paths within budget.
                     */
                    if ($newCost <= $k && $newCost < $dist[$v]) {
                        $dist[$v] = $newCost;
                    }
                }
            }

            return $dist[$n - 1] <= $k;
        };

        /*
         * No path at all.
         */
        if (!$check(0)) {
            return -1;
        }

        /*
         * Binary search for the maximum possible
         * minimum edge cost.
         */
        $left = 0;
        $right = $maxCost;

        while ($left < $right) {
            $mid = intdiv($left + $right + 1, 2);

            if ($check($mid)) {
                $left = $mid;
            } else {
                $right = $mid - 1;
            }
        }

        return $left;
    }
}
