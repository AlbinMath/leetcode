class Solution {
    function sortColors(&$nums) {
        $low = 0;
        $mid = 0;
        $high = count($nums) - 1;

        while ($mid <= $high) {

            if ($nums[$mid] == 0) {
                // Swap 0 to the beginning
                $temp = $nums[$low];
                $nums[$low] = $nums[$mid];
                $nums[$mid] = $temp;

                $low++;
                $mid++;

            } elseif ($nums[$mid] == 1) {
                // 1 is already in the correct middle region
                $mid++;

            } else {
                // Swap 2 to the end
                $temp = $nums[$mid];
                $nums[$mid] = $nums[$high];
                $nums[$high] = $temp;

                $high--;
            }
        }
    }
}
