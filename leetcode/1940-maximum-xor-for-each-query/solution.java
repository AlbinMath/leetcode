class Solution {
    public int[] getMaximumXor(int[] nums, int maximumBit) {
        int n = nums.length;
        int maxMask = (1 << maximumBit) - 1;
        int xorSum = 0;
        for (int num : nums) {
            xorSum ^= num;
        }

        int[] ans = new int[n];
        for (int i = 0; i < n; i++) {
            ans[i] = xorSum ^ maxMask;
            xorSum ^= nums[n - 1 - i];
        }
        return ans;
    }
}
