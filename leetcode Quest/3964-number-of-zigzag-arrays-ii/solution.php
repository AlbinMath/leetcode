class Solution {

    /**
     * @param Integer $n
     * @param Integer $l
     * @param Integer $r
     * @return Integer
     */
    function zigZagArrays($n, $l, $r) {
        $MOD = 1000000007;

        $m = $r - $l + 1;

        /*
         * Matrix M:
         *
         * M[i][j] = 1 if i + j < m - 1
         *
         * This represents one alternating transition.
         */
        $M = array_fill(0, $m * $m, 0);

        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $m - 1 - $i; $j++) {
                $M[$i * $m + $j] = 1;
            }
        }

        /*
         * Initially every value can be the first element.
         *
         * We need M^(n-1) * [1,1,...,1].
         */
        $vec = array_fill(0, $m, 1);

        $power = $n - 1;
        $base = $M;

        /*
         * Instead of calculating the complete M^(n-1),
         * apply matrix powers directly to the vector.
         */
        while ($power > 0) {

            if ($power & 1) {
                $vec = $this->multiplyMatrixVector(
                    $base,
                    $vec,
                    $m,
                    $MOD
                );
            }

            $power >>= 1;

            if ($power > 0) {
                $base = $this->multiplyMatrices(
                    $base,
                    $base,
                    $m,
                    $MOD
                );
            }
        }

        /*
         * The DP above counts one direction.
         *
         * Every valid zigzag has a symmetric opposite
         * direction, so multiply by 2.
         */
        $answer = 0;

        foreach ($vec as $value) {
            $answer += $value;

            if ($answer >= $MOD) {
                $answer -= $MOD;
            }
        }

        return (int)(($answer * 2) % $MOD);
    }

    /**
     * Matrix × vector
     */
    private function multiplyMatrixVector($A, $v, $m, $MOD) {
        $result = array_fill(0, $m, 0);

        for ($i = 0; $i < $m; $i++) {
            $sum = 0;
            $offset = $i * $m;

            for ($j = 0; $j < $m; $j++) {
                $a = $A[$offset + $j];

                if ($a != 0 && $v[$j] != 0) {
                    $sum = ($sum + $a * $v[$j]) % $MOD;
                }
            }

            $result[$i] = $sum;
        }

        return $result;
    }

    /**
     * Matrix × Matrix
     */
    private function multiplyMatrices($A, $B, $m, $MOD) {
        $C = array_fill(0, $m * $m, 0);

        for ($i = 0; $i < $m; $i++) {
            $row = $i * $m;

            for ($k = 0; $k < $m; $k++) {
                $a = $A[$row + $k];

                if ($a == 0) {
                    continue;
                }

                $bRow = $k * $m;

                for ($j = 0; $j < $m; $j++) {
                    $b = $B[$bRow + $j];

                    if ($b == 0) {
                        continue;
                    }

                    $idx = $row + $j;

                    $C[$idx] =
                        ($C[$idx] + $a * $b) % $MOD;
                }
            }
        }

        return $C;
    }
}
