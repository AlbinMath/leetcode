class Solution {
    function minWindow($s, $t) {
        // Count required characters from t
        $need = [];

        for ($i = 0; $i < strlen($t); $i++) {
            $char = $t[$i];

            if (isset($need[$char])) {
                $need[$char]++;
            } else {
                $need[$char] = 1;
            }
        }

        $left = 0;
        $right = 0;

        $required = count($need);
        $formed = 0;

        $window = [];

        $minLength = PHP_INT_MAX;
        $minLeft = 0;

        $sLength = strlen($s);

        while ($right < $sLength) {
            $char = $s[$right];

            // Add current character to window
            if (isset($window[$char])) {
                $window[$char]++;
            } else {
                $window[$char] = 1;
            }

            // Character requirement is now satisfied
            if (isset($need[$char]) &&
                $window[$char] == $need[$char]) {
                $formed++;
            }

            // Try shrinking the window
            while ($left <= $right && $formed == $required) {

                $currentLength = $right - $left + 1;

                if ($currentLength < $minLength) {
                    $minLength = $currentLength;
                    $minLeft = $left;
                }

                $leftChar = $s[$left];

                $window[$leftChar]--;

                // Removing this character breaks a requirement
                if (isset($need[$leftChar]) &&
                    $window[$leftChar] < $need[$leftChar]) {
                    $formed--;
                }

                $left++;
            }

            $right++;
        }

        if ($minLength == PHP_INT_MAX) {
            return "";
        }

        return substr($s, $minLeft, $minLength);
    }
}
