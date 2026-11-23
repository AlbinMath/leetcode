class Solution {
    function containsNearbyDuplicate($nums, $k) {
        $lastIndex = [];

        for ($i = 0; $i < count($nums); $i++) {
            $num = $nums[$i];

            // Number appeared before
            if (isset($lastIndex[$num])) {
                if ($i - $lastIndex[$num] <= $k) {
                    return true;
                }
            }

            // Store the latest index
            $lastIndex[$num] = $i;
        }

        return false;
    }
}
