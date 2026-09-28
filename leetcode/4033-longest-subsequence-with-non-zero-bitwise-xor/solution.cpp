class Solution {
public:
    int longestSubsequence(vector<int>& nums) {
        int xr = 0;

        for (int x : nums) {
            xr ^= x;
        }

        // If total XOR is non-zero, use the entire array
        if (xr != 0)
            return nums.size();

        // Total XOR is zero.
        // Remove one non-zero element to make XOR non-zero.
        for (int x : nums) {
            if (x != 0)
                return nums.size() - 1;
        }

        // All elements are zero
        return 0;
    }
};
