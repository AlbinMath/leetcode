class Solution {
    function titleToNumber($columnTitle) {
        $result = 0;

        for ($i = 0; $i < strlen($columnTitle); $i++) {
            $value = ord($columnTitle[$i]) - ord('A') + 1;

            $result = $result * 26 + $value;
        }

        return $result;
    }
}
