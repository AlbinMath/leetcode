import java.util.Arrays;

class Solution {
    public int maximumElementAfterDecrementingAndRearranging(int[] arr) {
        Arrays.sort(arr);

        int max = 0;

        for (int num : arr) {
            max = Math.min(num, max + 1);
        }

        return max;
    }
}
