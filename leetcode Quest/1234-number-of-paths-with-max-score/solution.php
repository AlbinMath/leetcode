class Solution {

    /**
     * @param String[] $board
     * @return Integer[]
     */
    function pathsWithMaxScore($board) {
        $MOD = 1000000007;
        $n = count($board);

        // -1 means unreachable
        $score = array_fill(0, $n, array_fill(0, $n, -1));
        $ways  = array_fill(0, $n, array_fill(0, $n, 0));

        // Start at S
        $score[$n - 1][$n - 1] = 0;
        $ways[$n - 1][$n - 1] = 1;

        /*
         * Process from S -> E.
         *
         * From (i,j), the possible next cells toward E are:
         *   down       (i+1, j)
         *   right      (i, j+1)
         *   diagonal   (i+1, j+1)
         */
        for ($i = $n - 1; $i >= 0; $i--) {
            for ($j = $n - 1; $j >= 0; $j--) {

                // S is already initialized
                if ($i == $n - 1 && $j == $n - 1) {
                    continue;
                }

                // Obstacle
                if ($board[$i][$j] === 'X') {
                    continue;
                }

                $best = -1;
                $count = 0;

                // Down
                if ($i + 1 < $n && $score[$i + 1][$j] != -1) {
                    $best = $score[$i + 1][$j];
                    $count = $ways[$i + 1][$j];
                }

                // Right
                if ($j + 1 < $n && $score[$i][$j + 1] != -1) {
                    $v = $score[$i][$j + 1];

                    if ($v > $best) {
                        $best = $v;
                        $count = $ways[$i][$j + 1];
                    } elseif ($v == $best) {
                        $count += $ways[$i][$j + 1];

                        if ($count >= $MOD) {
                            $count -= $MOD;
                        }
                    }
                }

                // Diagonal
                if (
                    $i + 1 < $n &&
                    $j + 1 < $n &&
                    $score[$i + 1][$j + 1] != -1
                ) {
                    $v = $score[$i + 1][$j + 1];

                    if ($v > $best) {
                        $best = $v;
                        $count = $ways[$i + 1][$j + 1];
                    } elseif ($v == $best) {
                        $count += $ways[$i + 1][$j + 1];

                        if ($count >= $MOD) {
                            $count -= $MOD;
                        }
                    }
                }

                // No path to S
                if ($best == -1) {
                    continue;
                }

                // Add current cell's digit
                $value = 0;

                if (
                    $board[$i][$j] !== 'E' &&
                    $board[$i][$j] !== 'S'
                ) {
                    $value = ord($board[$i][$j]) - 48;
                }

                $score[$i][$j] = $best + $value;
                $ways[$i][$j] = $count;
            }
        }

        /*
         * IMPORTANT:
         * Check score, not ways.
         *
         * ways can be 0 because the count is modulo 1e9+7.
         */
        if ($score[0][0] == -1) {
            return [0, 0];
        }

        return [
            $score[0][0],
            $ways[0][0]
        ];
    }
}
