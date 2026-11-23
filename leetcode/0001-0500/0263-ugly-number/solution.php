class Solution {
    function isUgly($n) {
        // Ugly numbers must be positive
        if ($n <= 0) {
            return false;
        }

        // Remove all factors of 2, 3, and 5
        while ($n % 2 == 0) {
            $n = intdiv($n, 2);
        }

        while ($n % 3 == 0) {
            $n = intdiv($n, 3);
        }

        while ($n % 5 == 0) {
            $n = intdiv($n, 5);
        }

        // No other prime factors should remain
        return $n == 1;
    }
}
