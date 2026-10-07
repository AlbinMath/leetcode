class Solution {
    function isPalindrome($s) {
        $left = 0;
        $right = strlen($s) - 1;

        while ($left < $right) {

            // Skip non-alphanumeric characters from left
            while ($left < $right && !ctype_alnum($s[$left])) {
                $left++;
            }

            // Skip non-alphanumeric characters from right
            while ($left < $right && !ctype_alnum($s[$right])) {
                $right--;
            }

            // Compare characters ignoring case
            if (strtolower($s[$left]) !== strtolower($s[$right])) {
                return false;
            }

            $left++;
            $right--;
        }

        return true;
    }
}
