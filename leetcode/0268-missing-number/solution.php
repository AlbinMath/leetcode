class Solution {
    function missingNumber($nums) {
        $n = count($nums);
        $missing = $n;

        for ($i = 0; $i < $n; $i++) {
            $missing ^= $i;
            $missing ^= $nums[$i];
        }

        return $missing;
    }
}
