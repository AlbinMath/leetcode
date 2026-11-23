class Solution {
    function majorityElement($nums) {
        $candidate = 0;
        $count = 0;

        foreach ($nums as $num) {
            // Choose a new candidate when count becomes 0
            if ($count == 0) {
                $candidate = $num;
            }

            // Vote for or against the candidate
            if ($num == $candidate) {
                $count++;
            } else {
                $count--;
            }
        }

        return $candidate;
    }
}
