class Solution {
    function summaryRanges($nums) {
        $result = [];
        $n = count($nums);

        if ($n == 0) {
            return $result;
        }

        $start = 0;

        for ($i = 1; $i <= $n; $i++) {
            // Range ends if we reach the end
            // or the numbers are no longer consecutive
            if ($i == $n || $nums[$i] != $nums[$i - 1] + 1) {
                if ($start == $i - 1) {
                    // Single number
                    $result[] = (string)$nums[$start];
                } else {
                    // Range
                    $result[] = $nums[$start] . "->" . $nums[$i - 1];
                }

                // Start a new range
                $start = $i;
            }
        }

        return $result;
    }
}
