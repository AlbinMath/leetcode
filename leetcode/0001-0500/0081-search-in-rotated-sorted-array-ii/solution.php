class Solution {
    function search($nums, $target) {
        $left = 0;
        $right = count($nums) - 1;

        while ($left <= $right) {
            $mid = intdiv($left + $right, 2);

            // Target found
            if ($nums[$mid] == $target) {
                return true;
            }

            // Duplicates make it impossible to determine
            // which side is sorted
            if ($nums[$left] == $nums[$mid] &&
                $nums[$mid] == $nums[$right]) {
                $left++;
                $right--;
                continue;
            }

            // Left half is sorted
            if ($nums[$left] <= $nums[$mid]) {

                if ($nums[$left] <= $target &&
                    $target < $nums[$mid]) {

                    $right = $mid - 1;
                } else {
                    $left = $mid + 1;
                }

            // Right half is sorted
            } else {

                if ($nums[$mid] < $target &&
                    $target <= $nums[$right]) {

                    $left = $mid + 1;
                } else {
                    $right = $mid - 1;
                }
            }
        }

        return false;
    }
}
