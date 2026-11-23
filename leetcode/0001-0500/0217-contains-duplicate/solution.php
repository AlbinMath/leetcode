class Solution {
    function containsDuplicate($nums) {
        $seen = [];

        foreach ($nums as $num) {
            if (isset($seen[$num])) {
                return true;
            }

            $seen[$num] = true;
        }

        return false;
    }
}
