class Solution {
    function combine($n, $k) {
        $result = [];
        $current = [];

        $this->backtrack(1, $n, $k, $current, $result);

        return $result;
    }

    function backtrack($start, $n, $k, &$current, &$result) {
        // Combination is complete
        if (count($current) == $k) {
            $result[] = $current;
            return;
        }

        for ($i = $start; $i <= $n; $i++) {
            // Choose
            $current[] = $i;

            // Explore
            $this->backtrack(
                $i + 1,
                $n,
                $k,
                $current,
                $result
            );

            // Backtrack
            array_pop($current);
        }
    }
}
