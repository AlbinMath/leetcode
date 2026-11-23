class Solution {
    function getRow($rowIndex) {
        $row = array_fill(0, $rowIndex + 1, 0);
        $row[0] = 1;

        for ($i = 1; $i <= $rowIndex; $i++) {
            // Traverse backwards so previous values
            // are not overwritten before they are used.
            for ($j = $i; $j >= 1; $j--) {
                $row[$j] = $row[$j] + $row[$j - 1];
            }
        }

        return $row;
    }
}
