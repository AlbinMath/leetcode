class Solution {
    function removeDuplicates(&$nums) {
        $n = count($nums);

        if ($n <= 2) {
            return $n;
        }

        $k = 2;

        for ($i = 2; $i < $n; $i++) {

            // Allow nums[i] if it is different
            // from the element two positions behind.
            if ($nums[$i] != $nums[$k - 2]) {
                $nums[$k] = $nums[$i];
                $k++;
            }
        }

        return $k;
    }
}
