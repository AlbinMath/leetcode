class Solution {

    /**
     * @param Integer[] $stoneValue
     * @return String
     */
    function stoneGameIII($stoneValue) {
        $n = count($stoneValue);

        // dp[i] = maximum score difference
        // current player can achieve starting from i
        $dp = array_fill(0, $n + 1, 0);

        // Base case: no stones left
        $dp[$n] = 0;

        for ($i = $n - 1; $i >= 0; $i--) {

            $take = 0;
            $best = PHP_INT_MIN;

            // Take 1, 2, or 3 stones
            for ($j = 0; $j < 3 && $i + $j < $n; $j++) {

                $take += $stoneValue[$i + $j];

                // Current player's gain minus opponent's best result
                $best = max(
                    $best,
                    $take - $dp[$i + $j + 1]
                );
            }

            $dp[$i] = $best;
        }

        if ($dp[0] > 0) {
            return "Alice";
        } elseif ($dp[0] < 0) {
            return "Bob";
        } else {
            return "Tie";
        }
    }
}
