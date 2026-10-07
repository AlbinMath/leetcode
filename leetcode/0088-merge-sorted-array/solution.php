class Solution {
    function merge(&$nums1, $m, $nums2, $n) {
        $i = $m - 1;          // Last element in nums1
        $j = $n - 1;          // Last element in nums2
        $k = $m + $n - 1;     // Last position in nums1

        while ($j >= 0) {

            if ($i >= 0 && $nums1[$i] > $nums2[$j]) {
                $nums1[$k] = $nums1[$i];
                $i--;
            } else {
                $nums1[$k] = $nums2[$j];
                $j--;
            }

            $k--;
        }
    }
}
