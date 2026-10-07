class Solution {
    function isAnagram($s, $t) {
        if (strlen($s) !== strlen($t)) {
            return false;
        }

        $count = array_fill(0, 26, 0);

        // Count characters in s
        for ($i = 0; $i < strlen($s); $i++) {
            $index = ord($s[$i]) - ord('a');
            $count[$index]++;
        }

        // Remove characters using t
        for ($i = 0; $i < strlen($t); $i++) {
            $index = ord($t[$i]) - ord('a');
            $count[$index]--;

            // More occurrences in t than in s
            if ($count[$index] < 0) {
                return false;
            }
        }

        return true;
    }
}
