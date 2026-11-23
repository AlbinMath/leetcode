class Solution {
    function generate($numRows) {
        $result = [];

        for ($i = 0; $i < $numRows; $i++) {
            $row = [];

            // First element
            $row[] = 1;

            // Middle elements
            for ($j = 1; $j < $i; $j++) {
                $row[] = $result[$i - 1][$j - 1]
                       + $result[$i - 1][$j];
            }

            // Last element
            if ($i > 0) {
                $row[] = 1;
            }

            $result[] = $row;
        }

        return $result;
    }
}
