class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function findMissingElements($nums) {
        $min = min($nums);
        $max = max($nums);

        $present = array_flip($nums);
        $result = [];

        for ($i = $min; $i <= $max; $i++) {
            if (!isset($present[$i])) {
                $result[] = $i;
            }
        }

        return $result;
    }
}
