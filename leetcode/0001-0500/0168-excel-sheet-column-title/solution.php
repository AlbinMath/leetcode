class Solution {
    function convertToTitle($columnNumber) {
        $result = "";

        while ($columnNumber > 0) {
            // Convert 1-26 into 0-25
            $columnNumber--;

            // Get character A-Z
            $remainder = $columnNumber % 26;
            $result = chr(ord('A') + $remainder) . $result;

            // Move to the next position
            $columnNumber = intdiv($columnNumber, 26);
        }

        return $result;
    }
}
