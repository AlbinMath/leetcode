class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Integer
     */
    function countMajoritySubarrays($nums, $target) {
        $n = count($nums);

        /*
         * Prefix sums can range from -n to n.
         * Shift by n so they become valid Fenwick indices.
         */
        $OFFSET = $n + 2;
        $SIZE = 2 * $n + 5;

        $bit = array_fill(0, $SIZE, 0);

        // Add a prefix sum to Fenwick tree.
        $add = function ($idx) use (&$bit, $SIZE) {
            while ($idx < $SIZE) {
                $bit[$idx]++;
                $idx += $idx & (-$idx);
            }
        };

        // Count prefix sums with index <= idx.
        $query = function ($idx) use (&$bit) {
            $sum = 0;

            while ($idx > 0) {
                $sum += $bit[$idx];
                $idx -= $idx & (-$idx);
            }

            return $sum;
        };

        /*
         * Empty prefix has sum 0.
         */
        $prefix = 0;
        $add($OFFSET);

        $answer = 0;

        foreach ($nums as $x) {

            if ($x == $target) {
                $prefix++;
            } else {
                $prefix--;
            }

            /*
             * Need previousPrefix < currentPrefix.
             *
             * Prefix sum p is stored at:
             * p + OFFSET
             *
             * So we query up to:
             * currentPrefix + OFFSET - 1
             */
            $index = $prefix + $OFFSET;

            $answer += $query($index - 1);

            // Store current prefix.
            $add($index);
        }

        return $answer;
    }
}
