class Solution {
    function isHappy($n) {
        $slow = $n;
        $fast = $this->sumOfSquares($n);

        while ($fast != 1 && $slow != $fast) {
            $slow = $this->sumOfSquares($slow);
            
            $fast = $this->sumOfSquares(
                $this->sumOfSquares($fast)
            );
        }

        return $fast == 1;
    }

    function sumOfSquares($n) {
        $sum = 0;

        while ($n > 0) {
            $digit = $n % 10;
            $sum += $digit * $digit;
            $n = intdiv($n, 10);
        }

        return $sum;
    }
}
