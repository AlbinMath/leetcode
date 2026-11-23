class Solution {
    function subsets($nums) {
        $result = [];
        $current = [];

        $this->backtrack(0, $nums, $current, $result);

        return $result;
    }

    function backtrack($index, $nums, &$current, &$result) {
        // Every current selection is a valid subset
        $result[] = $current;

        for ($i = $index; $i < count($nums); $i++) {
            // Choose
            $current[] = $nums[$i];

            // Explore
            $this->backtrack(
                $i + 1,
                $nums,
                $current,
                $result
            );

            // Backtrack
            array_pop($current);
        }
    }
}
