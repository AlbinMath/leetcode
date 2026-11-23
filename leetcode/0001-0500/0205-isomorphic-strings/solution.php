class Solution {
    function isIsomorphic($s, $t) {
        $mapST = [];
        $mapTS = [];

        $length = strlen($s);

        for ($i = 0; $i < $length; $i++) {
            $charS = $s[$i];
            $charT = $t[$i];

            // Check s -> t mapping
            if (isset($mapST[$charS])) {
                if ($mapST[$charS] !== $charT) {
                    return false;
                }
            } else {
                $mapST[$charS] = $charT;
            }

            // Check t -> s mapping
            if (isset($mapTS[$charT])) {
                if ($mapTS[$charT] !== $charS) {
                    return false;
                }
            } else {
                $mapTS[$charT] = $charS;
            }
        }

        return true;
    }
}
